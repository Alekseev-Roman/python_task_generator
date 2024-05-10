import os
import xml.etree.ElementTree as ET

import dataProcessor as dp


class Parser:
    def __init__(self):
        self.data_processor = dp.DataProcessor()

    def open_and_read_file(self, root_dir, difficulty, topic, file, topics, types):
        task = {
            'topic_id': topics[topic],
            'difficulty': [difficulty]
        }
        coderunner = None

        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(f'{root_dir}/{difficulty}/{topic}/{file}', parser=parser)
        root = tree.getroot()
        task['type_id'] = [types[root.find('question').attrib['type']][0]]
        task['question_name'] = [root.find('question').find('name').find('text').text]
        task['question_text'] = [root.find('question').find('questiontext').find('text').text.replace('\'', '\'\'')]
        if task['type_id'][0] == 1:
            coderunner = [root.find('question').find('coderunnertype').text][0]
            task['answer_preload'] = [''] if root.find('question').find('answerpreload').text is None \
                else [root.find('question').find('answerpreload').text.replace('\'', '\'\'')]
            task['template_params'] = [''] if root.find('question').find('templateparams').text is None \
                else [root.find('question').find('templateparams').text.replace('\'', '\'\'')]
            task['template'] = [''] if root.find('question').find('template').text is None \
                else [root.find('question').find('template').text.replace('\'', '\'\'')]
            task['test_case'] = []
            testcases = root.find('question').find('testcases').findall('testcase')
            for i in range(len(testcases)):
                task['test_case'].append({
                    'use_as_example': [testcases[i].attrib['useasexample']],
                    'test_code': [''] if testcases[i].find('testcode').find('text').text is None
                    else [testcases[i].find('testcode').find('text').text.replace('\'', '\'\'')],
                    'stdin': [''] if testcases[i].find('stdin').find('text').text is None
                    else [testcases[i].find('stdin').find('text').text.replace('\'', '\'\'')],
                    'expected': [''] if testcases[i].find('expected').find('text').text is None
                    else [testcases[i].find('expected').find('text').text.replace('\'', '\'\'')]
                })
        elif task['type_id'][0] == 2:
            task['penalty'] = [root.find('question').find('penalty').text]
            task['answers'] = []
            answers = root.find('question').findall('answer')
            for i in range(len(answers)):
                task['answers'].append({
                    'answer_fraction': [answers[i].attrib['fraction']],
                    'answer': [answers[i].find('text').text.replace('\'', '\'\'')]
                })
        else:
            print(f'Error in file {root_dir}/{difficulty}/{topic}/{file}. Not exist such type_id: {task["type_id"][0]}')
            return None

        return task, coderunner

    def finish_pushing(self, template):
        template.replace(',{{insert_task}}', ';')
        template.replace(',{{insert_coderunner_task}}', ';')
        template.replace(',{{insert_test_case}}', ';')
        template.replace(',{{insert_multichoice_task}}', ';')
        template.replace(',{{insert_multichoice_answer}}', ';')

        return template

    def insert(self, root_dir, task_params, topics):
        types = {
            'coderunner': [1],
            'multichoice': [2]
        }
        coderunners = {}

        for task_type in types:
            self.data_processor.insert_type(task_type)
        for topic in topics:
            self.data_processor.insert_topic(topic)
        for params in task_params:
            task, coderunner = self.open_and_read_file(root_dir, params[0], params[1], params[2], topics, types)
            if coderunner is not None:
                if coderunner not in coderunners:
                    coderunners[coderunner] = len(coderunners.values()) + 1
                    self.data_processor.insert_coderunner(coderunner)
                task['coderunner_id'] = coderunners[coderunner]
            if task is not None:
                self.data_processor.insert_task(task)

    def parse_directory(self, root_dir="DB/tasks"):
        tasks = {}
        topics = {}
        topic_id = 1

        for directory in os.listdir(root_dir):
            for sub_dir in os.listdir(f'{root_dir}/{directory}'):
                for file in os.listdir(f'{root_dir}/{directory}/{sub_dir}'):
                    if sub_dir not in topics:
                        topics[sub_dir] = [topic_id]
                        topic_id += 1
                    with open(f'{root_dir}/{directory}/{sub_dir}/{file}', 'r') as f:
                        text = f.read()
                        if text in tasks:
                            os.remove(f'{root_dir}/{directory}/{sub_dir}/{file}')
                        else:
                            tasks[text] = [directory, sub_dir, file]

        self.insert(root_dir, tasks.values(), topics)

    def parse_xml_dict(self, xml, topic_id, difficulty):
        task = {
            'topic_id': topic_id,
            'difficulty': difficulty
        }
        types = {
            'coderunner': [1],
            'multichoice': [2]
        }
        coderunners = self.data_processor.get_coderunners()

        task['type_id'] = [types[xml['quiz']['question']['@type']][0]]
        task['question_name'] = [xml['quiz']['question']['name']['text']]
        task['question_text'] = [xml['quiz']['question']['questiontext']['text'].replace('\'', '\'\'')]
        if task['type_id'][0] == 1:
            coderunner = xml['quiz']['question']['coderunnertype']
            task['answer_preload'] = [''] if xml['quiz']['question']['answerpreload'] is None \
                else [xml['quiz']['question']['answerpreload'].replace('\'', '\'\'')]
            task['template_params'] = [''] if xml['quiz']['question']['templateparams'] is None \
                else [xml['quiz']['question']['templateparams'].replace('\'', '\'\'')]
            task['template'] = [''] if xml['quiz']['question']['template'] is None \
                else [xml['quiz']['question']['template'].replace('\'', '\'\'')]
            task['test_case'] = []
            testcases = xml['quiz']['question']['testcases']['testcase']
            for i in range(len(testcases)):
                task['test_case'].append({
                    'use_as_example': [testcases[i]['@useasexample']],
                    'test_code': [''] if testcases[i]['testcode']['text'] is None
                    else [testcases[i]['stdin']['text'].replace('\'', '\'\'')],
                    'stdin': [''] if testcases[i]['testcode']['text'] is None
                    else [testcases[i]['stdin']['text'].replace('\'', '\'\'')],
                    'expected': [''] if testcases[i]['expected']['text'] is None
                    else [testcases[i]['expected']['text'].replace('\'', '\'\'')]
                })
            if coderunner not in coderunners.values():
                self.data_processor.insert_coderunner(coderunner)
                coderunners = self.data_processor.get_coderunners()
            coderunner_id = 0
            for id in coderunners.keys():
                if coderunner == coderunners[id]:
                    coderunner_id = id
                    break
            task['coderunner_id'] = [coderunner_id]
        elif task['type_id'][0] == 2:
            task['penalty'] = [xml['quiz']['question']['penalty']]
            task['answers'] = []
            answers = xml['quiz']['question']['answer']
            for i in range(len(answers)):
                task['answers'].append({
                    'answer_fraction': [answers[i]['@fraction']],
                    'answer': [answers[i]['text'].replace('\'', '\'\'')]
                })
        self.data_processor.insert_task(task)
