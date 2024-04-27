import json
import pandas as pd

from dbConnector import DbConnector
from taskCreator import TaskCreator


class DbAPI:
    def __init__(self, params='./params.json'):
        self.__connector = DbConnector(params)
        self.__conn = DbConnector().connecting_to_db()

        self.multichoice_task = None
        self.multichoice_answers = None
        self.coderunner_task = None
        self.test_cases = None

        self.__type_id = None
        self.task = None
        
    def check_topic(self, topic_name):
        """
        Check there is topic in db or not
        :param topic_name: Name of topic
        :return: False if topic is not in db and True if topic is in db
        """
        count = pd.read_sql(
            f"SELECT COUNT(*) "
            f"FROM topic "
            f"WHERE topic_name = '{topic_name}';",
            self.__conn
        ).to_dict()['count'][0]

        return count

    def check_name(self, name):
        """
        Check there is name in db or not
        :param name: Name of task
        :return: False if name is not in db and True if name is in db
        """
        count = pd.read_sql(
            f"SELECT COUNT(*) "
            f"FROM task "
            f"WHERE question_name = '{name}';",
            self.__conn
        ).to_dict()['count'][0]

        return count
    
    def is_multichoice(self):
        """
        Check type of task
        :return: True, if type is multichoice, False if type is coderunner
        """
        types = self.get_types()

        key = 0
        for k in types['type_id']:
            if int(types['type_id'][k]) == int(self.__type_id):
                key = k
        return True if types['type_name'][key] == 'multichoice' else False

    def get_data(self, type_id, topic_id, difficulty):
        """
        Get data from DataBase
        :return : flag True or False depending on result of getting data
        """
        tasks = pd.read_sql(
            f"SELECT * "
            f"FROM task "
            f"WHERE type_id = {type_id} AND topic_id = {topic_id}"
            f" AND difficulty = {difficulty};",
            self.__conn
        )

        if tasks.shape[0] > 0:
            self.task = tasks.sample()
            task_id = self.task.iloc[0]['task_id']
            self.__type_id = self.task.iloc[0]['type_id']

            if self.is_multichoice():
                self.multichoice_task = pd.read_sql(
                    f"SELECT * "
                    f"FROM multichoice_task "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).to_dict()
                self.multichoice_answers = pd.read_sql(
                    f"SELECT * "
                    f"FROM multichoice_answer "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).to_dict()

            else:
                self.coderunner_task = pd.read_sql(
                    f"SELECT * "
                    f"FROM coderunner_task "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).iloc[0]
                self.test_cases = pd.read_sql(
                    f"SELECT * "
                    f"FROM test_case "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).to_dict()

            return True
        return None

    def get_data_by_id(self, task_id):
        """
        Get data from DataBase by task ID
        :return : flag True or False depending on result of getting data
        """
        self.task = pd.read_sql(
            f"SELECT * "
            f"FROM task "
            f"WHERE task_id = {task_id};",
            self.__conn
        )

        if self.task.shape[0] > 0:
            self.__type_id = self.task.iloc[0]['type_id']

            if self.is_multichoice():
                self.multichoice_task = pd.read_sql(
                    f"SELECT * "
                    f"FROM multichoice_task "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).to_dict()
                self.multichoice_answers = pd.read_sql(
                    f"SELECT * "
                    f"FROM multichoice_answer "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).to_dict()

            else:
                self.coderunner_task = pd.read_sql(
                    f"SELECT * "
                    f"FROM coderunner_task "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).iloc[0]
                self.test_cases = pd.read_sql(
                    f"SELECT * "
                    f"FROM test_case "
                    f"WHERE task_id = {task_id};",
                    self.__conn
                ).to_dict()

            return True
        return None

    def get_coderunners(self):
        """
        Get list of coderunner types
        :return: List of types or None
        """
        try:
            coderunners = pd.read_sql(
                f"SELECT * "
                f"FROM coderunner_types;",
                self.__conn
            ).to_dict()

            coderunners_dict = dict(zip(
                coderunners['coderunner_id'].values(),
                coderunners['coderunner_name'].values()
            ))

            return coderunners_dict
        except:
            return None

    def get_topics(self):
        """
        Get topics from DB and save to self.__topics
        :return: Topics or None
        """
        try:
            topics = pd.read_sql(
                f"SELECT * "
                f"FROM topic;",
                self.__conn
            ).to_dict()

            return dict(zip(topics['topic_id'].values(), topics['topic_name'].values()))
        except:
            return None

    def get_types(self):
        """
        Get dictionary of types to self._types
        :return: Type or None
        """
        try:
            types = pd.read_sql(
                f"SELECT * "
                f"FROM type;",
                self.__conn
            ).to_dict()

            return types
        except:
            return None

    def get_quantity_tasks(self, topic, type_task, difficulty):
        """
        Get quantity of tasks with params
        :param topic:
        :param type_task:
        :param difficulty:
        :return: Int
        """
        quantity = pd.read_sql(
            f"SELECT COUNT(*) "
            f"FROM task "
            f"WHERE topic_id = {topic} AND type_id = {type_task} AND difficulty = {difficulty};",
            self.__conn
        ).to_dict()['count'][0]

        return quantity

    def get_quantity_tasks_by_topic_diff(self, topic, difficulty):
        """
        Get quantity of tasks with params without type of task
        :param topic:
        :param difficulty:
        :return: Int
        """
        quantity = pd.read_sql(
            f"SELECT COUNT(*) "
            f"FROM task "
            f"WHERE topic_id = {topic} AND difficulty = {difficulty};",
            self.__conn
        ).to_dict()['count'][0]

        return quantity

    def get_topic_name_by_id(self, topic_id):
        """
        Get topic name by topic id
        :param topic_id:
        :return: topic name
        """
        name = pd.read_sql(
            f"SELECT topic_name "
            f"FROM topic "
            f"WHERE topic_id = {topic_id};",
            self.__conn
        ).to_dict()['topic_name'][0]

        return name

    def get_topics_and_quantity_tasks(self):
        """
        Get topics and quantity tasks with these topics
        :return: List with couples topic - quantity
        """
        rare_statistic = pd.read_sql(
            f"SELECT topic.topic_id, topic_name, type.type_id, type.type_name, COUNT(task_id) as quantity "
            f"FROM task "
            f"RIGHT JOIN topic ON task.topic_id = topic.topic_id "
            f"LEFT JOIN type ON task.type_id = type.type_id "
            f"GROUP BY topic.topic_id, topic_name, type.type_id, type_name;",
            self.__conn
        ).to_dict()

        statistic = []

        for i in rare_statistic['topic_id']:
            statistic.append({
                'topic_id': rare_statistic['topic_id'][i],
                'topic_name': rare_statistic['topic_name'][i],
                'type_id': rare_statistic['type_id'][i] if rare_statistic['type_name'][i] else '-',
                'type_name': rare_statistic['type_name'][i] if rare_statistic['type_name'][i] else '-',
                'quantity': rare_statistic['quantity'][i]
            })

        return statistic

    def get_tasks_by_topic(self, topic_id):
        """
        Get tasks with topic by topic_id
        :param topic_id: topic id
        :return: tasks
        """
        tasks = pd.read_sql(
            f"SELECT * "
            f"FROM task "
            f"WHERE topic_id = {topic_id};",
            self.__conn
        )

        types = self.get_types()
        types_dict = {}
        for key, value in types['type_id'].items():
            types_dict[str(value)] = types['type_name'][key]
        tasks_list = []

        if tasks.shape[0] > 0:
            for task_id in tasks['task_id']:
                # task = TaskCreator.create_task_by_id(task_id)
                if self.get_data_by_id(task_id):
                    task_df_dict = self.task.iloc[0]
                    task = {'question_name': task_df_dict['question_name'],
                            'question_text': task_df_dict['question_text'],
                            'task_id': str(task_df_dict['task_id']),
                            'type_id': str(task_df_dict['type_id']),
                            'difficulty': str(task_df_dict['difficulty'])}

                    if self.is_multichoice():
                        task['penalty'] = self.multichoice_task['penalty']
                        task['answers'] = {'answer_fraction': [],
                                           'answer': []}

                        for i in range(len(self.multichoice_answers['answer_fraction'])):
                            task['answers']['answer_fraction'].append(self.multichoice_answers['answer_fraction'][i])
                            task['answers']['answer'].append(self.multichoice_answers['answer'][i])
                    else:
                        coderunners = self.get_coderunners()
                        task['template'] = self.coderunner_task['template'].replace("''", "'")
                        task['template_params'] = self.coderunner_task['template_params']
                        task['answer_preload'] = self.coderunner_task['answer_preload']
                        task['coderunner_type'] = coderunners[self.coderunner_task['coderunner_id']]
                        task['test_cases'] = {'use_as_example': [],
                                              'test_code': [],
                                              'stdin': [],
                                              'expected': []}
                        for i in range(len(self.test_cases['test_code'])):
                            task['test_cases']['use_as_example'].append(self.test_cases['use_as_example'][i])
                            task['test_cases']['test_code'].append(self.test_cases['test_code'][i])
                            task['test_cases']['stdin'].append(self.test_cases['stdin'][i])
                            task['test_cases']['expected'].append(self.test_cases['expected'][i])
                task['type_name'] = types_dict[task['type_id']]
                tasks_list.append(task)
            return tasks_list

        return []

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
            new_type_df.to_sql(name='topic', con=self.__conn, if_exists='append', index_label='topic_id', index=False)

            return True
        except:
            return False

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
            new_type_df.to_sql(name='type', con=self.__conn, if_exists='append', index_label='type_id', index=False)

            return True
        except:
            return False

    def insert_coderunner(self, coderunner_name):
        """
        Insert coderunner name to DB
        :param coderunner_name: Name of coderunner
        :return: True or False
        """
        try:
            new_coderunner_df = pd.DataFrame({
                'coderunner_name': [coderunner_name]
            })
            new_coderunner_df.to_sql(
                name='coderunner_types', con=self.__conn, if_exists='append',
                index_label='coderunner_id', index=False
            )

            return True
        except:
            return False

    def insert_task(self, task):
        """
        Insert data to DB
        :param task: Dictionary with data of task
        :return: False or True
        """
        try:
            new_task_df = pd.DataFrame({
                'topic_id': task['topic_id'],
                'type_id': task['type_id'],
                'difficulty': task['difficulty'],
                'question_name': task['question_name'],
                'question_text': task['question_text']
            })
            new_task_df.to_sql(name='task', con=self.__conn, if_exists='append', index_label='task_id', index=False)
            task_id = pd.read_sql(
                f"SELECT task_id "
                f"FROM task "
                f"WHERE topic_id = {task['topic_id'][0]} AND type_id = {task['type_id'][0]} AND "
                f"difficulty = {task['difficulty'][0]} AND question_name = '{task['question_name'][0]}';",
                self.__conn
            )['task_id'].to_list()[-1]

            self.__type_id = task['type_id'][0]

            if self.is_multichoice():
                new_multichoice_task_df = pd.DataFrame({
                    'task_id': task_id,
                    'penalty': task['penalty']
                })
                new_multichoice_task_df.to_sql(name='multichoice_task', con=self.__conn, if_exists='append',
                                               index_label='task_id', index=False)
                for answer in task['answers']:
                    new_multichoice_answer_df = pd.DataFrame({
                        'task_id': task_id,
                        'answer_fraction': answer['answer_fraction'],
                        'answer': answer['answer']
                    })
                    new_multichoice_answer_df.to_sql(name='multichoice_answer', con=self.__conn, if_exists='append',
                                                     index_label='multichoice_answer_id', index=False)

            else:
                new_coderunner_task_df = pd.DataFrame({
                    'task_id': task_id,
                    'template': task['template'],
                    'template_params': task['template_params'],
                    'answer_preload': task['answer_preload'],
                    'coderunner_id': task['coderunner_id']
                })
                new_coderunner_task_df.to_sql(name='coderunner_task', con=self.__conn, if_exists='append',
                                              index_label='task_id', index=False)
                for test_case in task['test_case']:
                    new_test_case_df = pd.DataFrame({
                        'task_id': task_id,
                        'use_as_example': test_case['use_as_example'],
                        'test_code': test_case['test_code'],
                        'stdin': test_case['stdin'],
                        'expected': test_case['expected']
                    })
                    new_test_case_df.to_sql(name='test_case', con=self.__conn, if_exists='append',
                                            index_label='test_case_id', index=False)

        except Exception as error:
            print(error)
            return False
        return True

    def delete_topic_by_id(self, topic_id):
        """
        Delete topic in DB by topic_id
        :return:
        """
        pd.read_sql(
            f"DELETE "
            f"FROM topic "
            f"WHERE topic_id = {int(topic_id)}; "
            f"RETURNING *;",
            self.__conn
        )

        df = pd.read_sql_query(
            f"SELECT * " 
            f"FROM topic;",
            self.__conn
        )
        df = df[df['topic_id'] != int(topic_id)]
        df.to_sql('topic', self.__conn, if_exists='replace')

    def delete_task_by_id(self, task_id):
        """
        Delete task by task_id
        :param task_id:
        :return:
        """
        pass
