import pandas as pd
from sqlalchemy import create_engine, URL
import json
import sys

import templater as tem


class DataProcessor:
    def __init__(self):
        """
        Initialize the Data class for storing and processing data from DB
        """
        self._conn = None
        self._params_dic = None

        # Data
        self._topics = None
        self._types = None
        self._tasks = None
        self._coderunner_task = None
        self._test_cases = None
        self._multichoice_task = None
        self._multichoice_answers = None

        # IDs
        self._topic_id = None
        self._type_id = None
        self._task_id = None

        self._difficulty = None
        self._task = None

    def read_connect_data(self):
        """
        Read data for connecting to DB from file params.json
        :return: None
        """
        try:
            with open('params.json', 'r') as file:
                self._params_dic = json.loads(file.read())
        except FileNotFoundError:
            print("File params.json not found.")

    def connecting_to_db(self):
        """
        Connect to the DataBase and return the connection
        :return conn:
        """
        try:
            self.read_connect_data()
            url_obj = URL.create(**self._params_dic)
            self._conn = create_engine(url_obj)
        except Exception as error:
            print("Can't connect to DB")
            print(error)
            sys.exit(1)
        return self._conn

    def get_data(self):
        """
        Get data from DataBase
        :return : flag True or False depending on result of getting data
        """

        self._tasks = pd.read_sql(
            f"SELECT * "
            f"FROM task "
            f"WHERE type_id = {self._type_id} AND topic_id = {self._topic_id}"
            f" AND difficulty = {self._difficulty};",
            self._conn
        )

        if self._tasks.shape[0] > 0:
            self._task = self._tasks.sample()
            self._task_id = self._task.iloc[0]['task_id']
            self._type_id = self._task.iloc[0]['type_id']

            if self.is_multichoice():
                self._multichoice_task = pd.read_sql(
                    f"SELECT * "
                    f"FROM multichoice_task "
                    f"WHERE task_id = {self._task_id};",
                    self._conn
                ).to_dict()
                self._multichoice_answers = pd.read_sql(
                    f"SELECT * "
                    f"FROM multichoice_answer "
                    f"WHERE task_id = {self._task_id};",
                    self._conn
                ).to_dict()

            else:
                self._coderunner_task = pd.read_sql(
                    f"SELECT * "
                    f"FROM coderunner_task "
                    f"WHERE task_id = {self._task_id};",
                    self._conn
                ).iloc[0]
                self._test_cases = pd.read_sql(
                    f"SELECT * "
                    f"FROM test_case "
                    f"WHERE task_id = {self._task_id};",
                    self._conn
                ).to_dict()

            return True

        print("Such task not exist")
        return False

    def get_topics(self):
        """
        Get topics from DB and save to self.topics
        :return: False or True
        """
        try:
            self._topics = pd.read_sql(
                f"SELECT * "
                f"FROM topic;",
                self._conn
            ).to_dict()

        except:
            return False

        return True

    def insert_topic(self, topic):
        """
        Insert topic to DB
        :param topic: Topic name
        :return: False or True
        """
        try:
            new_type_df = pd.DataFrame({
                'topic_name': [topic]
            })
            new_type_df.to_sql(name='topic', con=self._conn, if_exists='append', index_label='topic_id', index=False)

        except:
            return False

        return True

    def insert_type(self, type_name):
        """
        Insert type to DB
        :param type_name: Type name
        :return: False or True
        """
        try:
            new_type_df = pd.DataFrame({
                'type_name': [type_name]
            })
            new_type_df.to_sql(name='type', con=self._conn, if_exists='append', index_label='type_id', index=False)

        except:
            return False

        return True

    def get_types(self):
        """
        Get dictionary of types to self.types
        :return: False or True
        """
        try:
            self._types = pd.read_sql(
                f"SELECT * "
                f"FROM type;",
                self._conn
            ).to_dict()

        except:
            return False

        return True

    def is_multichoice(self):
        """
        Check type of task
        :return: True, if type is multichoice, False if type is coderunner
        """
        if self._types == {}:
            self.get_types()

        key = 0
        for k in self._types['type_id']:
            if self._types['type_id'][k] == self._type_id:
                key = k

        return True if self._types['type_name'][key] == 'multichoice' else False

    def insert_task(self, task):
        """
        Insert data to DB
        :param task: Dictionary with data of task
        :return: False or True
        """
        if not self._types:
            self.get_types()
        try:
            new_task_df = pd.DataFrame({
                'topic_id': task['topic_id'],
                'type_id': task['type_id'],
                'difficulty': task['difficulty'],
                'question_name': task['question_name'],
                'question_text': task['question_text']
            })
            new_task_df.to_sql(name='task', con=self._conn, if_exists='append', index_label='task_id', index=False)
            task_id = pd.read_sql(
                f"SELECT task_id "
                f"FROM task "
                f"WHERE topic_id = {task['topic_id'][0]} AND type_id = {task['type_id'][0]} AND "
                f"difficulty = {task['difficulty'][0]} AND question_name = '{task['question_name'][0]}';",
                self._conn
            )['task_id'].to_list()[-1]

            self._type_id = task['type_id'][0]

            if self.is_multichoice():
                new_multichoice_task_df = pd.DataFrame({
                    'task_id': task_id,
                    'penalty': task['penalty']
                })
                new_multichoice_task_df.to_sql(name='multichoice_task', con=self._conn, if_exists='append',
                                               index_label='task_id', index=False)
                for answer in task['answers']:
                    new_multichoice_answer_df = pd.DataFrame({
                        'task_id': task_id,
                        'answer_fraction': answer['answer_fraction'],
                        'answer': answer['answer']
                    })
                    new_multichoice_answer_df.to_sql(name='multichoice_answer', con=self._conn, if_exists='append',
                                                     index_label='multichoice_answer_id', index=False)

            else:
                new_coderunner_task_df = pd.DataFrame({
                    'task_id': task_id,
                    'template': task['template'],
                    'template_params': task['template_params'],
                    'answer_preload': task['answer_preload'],
                    'coderunner_type': task['coderunner_type']
                })
                new_coderunner_task_df.to_sql(name='coderunner_task', con=self._conn, if_exists='append',
                                              index_label='task_id', index=False)
                for test_case in task['test_case']:
                    new_test_case_df = pd.DataFrame({
                        'task_id': task_id,
                        'use_as_example': test_case['use_as_example'],
                        'test_code': test_case['test_code'],
                        'expected': test_case['expected']
                    })
                    new_test_case_df.to_sql(name='test_case', con=self._conn, if_exists='append',
                                            index_label='test_case_id', index=False)

        except Exception as error:
            print(error)
            return False

        return True

    def fill_template_of_task(self, task, name='task.xml'):
        """
        Fill in the template of a task
        :return: File Moodle XML with a task
        """
        if self._task_id >= 0:
            if self.is_multichoice():
                file_name = "multichoice_template.xml"
            else:
                file_name = "coderunner_template.xml"
            templater = tem.Templater(f"./templates/{file_name}")
            templater.set_data(task)

            if self.is_multichoice():
                templater.fill_multichoice_template_file(name)
            else:
                templater.fill_code_runner_template_file(name)

    def create_task(self, topic, type_task, difficulty):
        """
        Create task with topic, difficulty and type
        :return: dictionary with task or None
        """
        self.connecting_to_db()

        self._topic_id = topic
        self._type_id = type_task
        self._difficulty = difficulty

        self.get_types()

        if self.get_data():
            task_df_dict = self._task.iloc[0]
            task = {'question_name': task_df_dict['question_name'],
                    'question_text': task_df_dict['question_text']}

            if self.is_multichoice():
                task['penalty'] = self._multichoice_task['penalty']
                task['answers'] = {'answer_fraction': [],
                                   'answer': []}

                for i in range(len(self._multichoice_answers['answer_fraction'])):
                    task['answers']['answer_fraction'].append(self._multichoice_answers['answer_fraction'][i])
                    task['answers']['answer'].append(self._multichoice_answers['answer'][i])
            else:
                task['template'] = self._coderunner_task['template']
                task['template_params'] = self._coderunner_task['template_params']
                task['answer_preload'] = self._coderunner_task['answer_preload']
                task['coderunner_type'] = self._coderunner_task['coderunner_type']
                task['test_cases'] = {'use_as_example': [],
                                      'test_code': [],
                                      'expected': []}
                for i in range(len(self._test_cases['test_code'])):
                    task['test_cases']['use_as_example'].append(self._test_cases['use_as_example'][i])
                    task['test_cases']['test_code'].append(self._test_cases['test_code'][i])
                    task['test_cases']['expected'].append(self._test_cases['expected'][i])

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
        task = self.create_task(topic, type_task, difficulty)
        if task:
            self.fill_template_of_task(task)

    def create_variant(self, path):
        """
        Create variant of three tasks with topics and types
        :return:
        """
        try:
            with open(path, 'r') as file:
                var_params = json.loads(file.read())

            try:
                task_1 = self.create_task(var_params['task_1']['topic'], var_params['task_1']['type'], 1)
                task_2 = self.create_task(var_params['task_2']['topic'], var_params['task_2']['type'], 2)
                task_3 = self.create_task(var_params['task_3']['topic'], var_params['task_3']['type'], 3)

                if not task_1:
                    print('Task 1 cannot be created. Change topic or type of this task.')
                if not task_2:
                    print('Task 2 cannot be created. Change topic or type of this task.')
                if not task_3:
                    print('Task 3 cannot be created. Change topic or type of this task.')

                if task_1 and task_2 and task_3:
                    self._type_id = var_params['task_1']['type']
                    self.fill_template_of_task(task_1, 'task_1.xml')
                    self._type_id = var_params['task_2']['type']
                    self.fill_template_of_task(task_2, 'task_2.xml')
                    self._type_id = var_params['task_3']['type']
                    self.fill_template_of_task(task_3, 'task_3.xml')

            except Exception as e:
                print("Error creating tasks, not enough data for creating in the file.")
                print(e)

        except FileNotFoundError:
            print(f"File {path} for creating variant not found.")
