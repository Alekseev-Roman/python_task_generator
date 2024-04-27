import templater as tem


class TaskCreator:
    def __init__(self, db_api):
        self.__db_API = db_api
        self.__task_for_templater = None
        
    def set_type_id(self, type_id):
        self.__db_API.__type_id = type_id
        
    def set_task_for_template(self, task):
        self.__task_for_templater = task

    def fill_template_of_task(self, name='task.xml'):
        """
        Fill to the template of a task
        :return: File Moodle XML with a task
        """
        if int(self.__task_for_templater['task_id']) >= 0:
            if self.__db_API.is_multichoice():
                file_name = 'multichoice_template.xml'
                templater = tem.Templater(f'./templates/{file_name}')
                templater.set_data(self.__task_for_templater)
                templater.fill_multichoice_template_file(name)
            else:
                file_name = 'coderunner_template.xml'
                templater = tem.Templater(f'./templates/{file_name}')
                templater.set_data(self.__task_for_templater)
                templater.fill_code_runner_template_file(name)

    def create_task(self, topic, type_task, difficulty):
        """
        Create task with topic, difficulty and type
        :return: dictionary with task or None
        """
        self.__db_API.__topic_id = topic
        self.__db_API.__type_id = type_task
        self.__db_API.__difficulty = difficulty

        if self.__db_API.get_data(type_task, topic, difficulty):
            task_df_dict = self.__db_API.task.iloc[0]
            task = {'question_name': task_df_dict['question_name'],
                    'question_text': task_df_dict['question_text'],
                    'task_id': str(task_df_dict['task_id'])}

            if self.__db_API.is_multichoice():
                task['penalty'] = self.__db_API.multichoice_task['penalty']
                task['answers'] = {'answer_fraction': [],
                                   'answer': []}

                for i in range(len(self.__db_API.multichoice_answers['answer_fraction'])):
                    task['answers']['answer_fraction'].append(self.__db_API.multichoice_answers['answer_fraction'][i])
                    task['answers']['answer'].append(self.__db_API.multichoice_answers['answer'][i])
            else:
                coderunners = self.__db_API.get_coderunners()
                task['template'] = self.__db_API.coderunner_task['template'].replace("''", "'")
                task['template_params'] = self.__db_API.coderunner_task['template_params']
                task['answer_preload'] = self.__db_API.coderunner_task['answer_preload']
                task['coderunner_type'] = coderunners[self.__db_API.coderunner_task['coderunner_id']]
                task['test_cases'] = {'use_as_example': [],
                                      'test_code': [],
                                      'stdin': [],
                                      'expected': []}
                for i in range(len(self.__db_API.test_cases['test_code'])):
                    task['test_cases']['use_as_example'].append(self.__db_API.test_cases['use_as_example'][i])
                    task['test_cases']['test_code'].append(self.__db_API.test_cases['test_code'][i])
                    task['test_cases']['stdin'].append(self.__db_API.test_cases['stdin'][i])
                    task['test_cases']['expected'].append(self.__db_API.test_cases['expected'][i])

            self.__task_for_templater = task

            return task
        return None

    def create_task_by_id(self, task_id):
        """
        Create task by ID in DB
        :return: dictionary with task or None
        """
        if self.__db_API.get_data_by_id(task_id):
            task_df_dict = self.__db_API.task.iloc[0]
            task = {'question_name': task_df_dict['question_name'],
                    'question_text': task_df_dict['question_text'],
                    'task_id': str(task_df_dict['task_id']),
                    'type_id': str(task_df_dict['type_id']),
                    'difficulty': str(task_df_dict['difficulty'])}

            if self.__db_API.is_multichoice():
                task['penalty'] = self.__db_API.multichoice_task['penalty']
                task['answers'] = {'answer_fraction': [],
                                   'answer': []}

                for i in range(len(self.__db_API.multichoice_answers['answer_fraction'])):
                    task['answers']['answer_fraction'].append(self.__db_API.multichoice_answers['answer_fraction'][i])
                    task['answers']['answer'].append(self.__db_API.multichoice_answers['answer'][i])
            else:
                coderunners = self.__db_API.get_coderunners()
                task['template'] = self.__db_API.coderunner_task['template'].replace("''", "'")
                task['template_params'] = self.__db_API.coderunner_task['template_params']
                task['answer_preload'] = self.__db_API.coderunner_task['answer_preload']
                task['coderunner_type'] = coderunners[self.__db_API.coderunner_task['coderunner_id']]
                task['test_cases'] = {'use_as_example': [],
                                      'test_code': [],
                                      'stdin': [],
                                      'expected': []}
                for i in range(len(self.__db_API.test_cases['test_code'])):
                    task['test_cases']['use_as_example'].append(self.__db_API.test_cases['use_as_example'][i])
                    task['test_cases']['test_code'].append(self.__db_API.test_cases['test_code'][i])
                    task['test_cases']['stdin'].append(self.__db_API.test_cases['stdin'][i])
                    task['test_cases']['expected'].append(self.__db_API.test_cases['expected'][i])

            self.__task_for_templater = task

            return task
        return None

    def create_and_fill_task(self, topic, type_task, difficulty):
        """
        Create and fill task to template file
        :param topic:
        :param type_task:
        :param difficulty:
        :return:
        """
        self.__task_for_templater = self.create_task(topic, type_task, difficulty)
        if self.__task_for_templater:
            self.fill_template_of_task()

    def create_and_fill_task_by_id(self, task_id):
        self.__task_for_templater = self.create_task_by_id(task_id)
        if self.__task_for_templater:
            self.fill_template_of_task()
