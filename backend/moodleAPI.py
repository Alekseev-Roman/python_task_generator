import requests
import json

from moodleHTMLParser import MoodleHTMLParser
from bs4 import BeautifulSoup


class MoodleAPI:
    def __init__(self):
        self.payload = {}
        self.__session = None

        self.__read_payload()

    def __read_payload(self):
        """
        Read data for login on Moodle from payload.json
        :return: None
        """
        try:
            with open('payload.json', 'r') as file:
                self.payload = json.loads(file.read())
        except FileNotFoundError:
            print("File payload.json not found.")

    def connect(self):
        """
        Create session
        :return: None
        """
        self.__session = requests.Session()

    def login(self):
        """
        Login on Moodle by data from payload.json
        :return: None
        """
        if not self.__session:
            self.connect()

        login_page = self.__session.post('https://e.moevm.info/login/index.php')
        parser = MoodleHTMLParser()
        parser.feed(login_page.text)
        self.payload['logintoken'] = parser.get_logintoken()
        self.__session.post('https://e.moevm.info/login/index.php', data=self.payload)

    def get_task_from_moodle(self, url: str):
        """
        Get task data from Moodle page on url
        :param url: url of a task page
        :return: Dict with task data
        """
        answer = self.__session.get(url)
        soup = BeautifulSoup(answer.text, 'lxml')

        task = {}
        testcase_id = 0
        answer_id = 0

        for traverse_tags in soup.recursiveChildGenerator():
            if traverse_tags.name and 'id' in traverse_tags.attrs:
                if traverse_tags.attrs['id'] == 'id_name':
                    task['question_name'] = [traverse_tags.attrs['value']]
                if traverse_tags.attrs['id'] == 'id_questiontext':
                    task['question_text'] = [traverse_tags.text]

                if traverse_tags.attrs['id'] == 'id_coderunnertype':
                    for option in traverse_tags.contents:
                        if hasattr(option, 'attrs') and 'selected' in option.attrs:
                            task['coderunner_name'] = [option.attrs['value']]
                if traverse_tags.attrs['id'] == 'id_templateparams':
                    task['template_params'] = [traverse_tags.text]
                if traverse_tags.attrs['id'] == 'id_template':
                    task['template'] = [traverse_tags.text]
                if traverse_tags.attrs['id'] == 'id_answerpreload':
                    task['answer_preload'] = [traverse_tags.text]
                if traverse_tags.attrs['id'] == f'id_testcode_{testcase_id}':
                    if testcase_id == 0:
                        task['test_case'] = []
                    task['test_case'].append({
                        'test_code': [traverse_tags.text],
                        'stdin': '',
                        'expected': '',
                        'use_as_example': 0
                    })
                if traverse_tags.attrs['id'] == f'id_stdin_{testcase_id}':
                    task['test_case'][-1]['stdin'] = [traverse_tags.text]
                if traverse_tags.attrs['id'] == f'id_expected_{testcase_id}':
                    task['test_case'][-1]['expected'] = [traverse_tags.text]
                if traverse_tags.attrs['id'] == f'id_useasexample_{testcase_id}':
                    task['test_case'][-1]['use_as_example'] = [traverse_tags.attrs['value']]
                    testcase_id += 1

                if traverse_tags.attrs['id'] == 'id_penalty':
                    for option in traverse_tags.contents:
                        if hasattr(option, 'attrs') and 'selected' in option.attrs:
                            task['penalty'] = [option.attrs['value']]
                if traverse_tags.attrs['id'] == f'id_answer_{answer_id}':
                    if answer_id == 0:
                        task['answers'] = []
                    task['answers'].append({
                        'answer_fraction': '',
                        'answer': [traverse_tags.text]
                    })
                if traverse_tags.attrs['id'] == f'id_fraction_{answer_id}':
                    for option in traverse_tags.contents:
                        if hasattr(option, 'attrs') and 'selected' in option.attrs:
                            task['answers'][-1]['answer_fraction'] = [int(option.text[:-1])]
                    answer_id += 1

        return task

