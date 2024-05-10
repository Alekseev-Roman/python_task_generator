from dbAPI import DbAPI
from taskCreator import TaskCreator
from variantCreator import VariantCreator


class DataProcessor:
    def __init__(self):
        """
        Initialize the Data class for storing and processing data from DB
        """
        self.__db_api = DbAPI()
        self.__task_creator = TaskCreator(self.__db_api)
        self.__variant_creator = VariantCreator(self.__db_api)

    def create_and_fill_task(self, topic, task_type, difficulty):
        self.__task_creator.create_and_fill_task(topic, task_type, difficulty)

    def create_variant(self, variant):
        self.__variant_creator.create_variant(variant)

    def create_task(self, topic, task_type, difficulty):
        return self.__task_creator.create_task(topic, task_type, difficulty)

    def get_quantity_tasks(self, topic, difficulty, task_type=None):
        if task_type is None:
            return self.__db_api.get_quantity_tasks_by_topic_diff(topic, difficulty)
        else:
            return self.__db_api.get_quantity_tasks(topic, task_type, difficulty)

    def get_topics_and_quantity_tasks(self):
        return self.__db_api.get_topics_and_quantity_tasks()

    def get_topics(self):
        return self.__db_api.get_topics()

    def get_topic_name_by_id(self, topic_id):
        return self.__db_api.get_topic_name_by_id(topic_id)

    def get_tasks_by_topic(self, topic_id):
        return self.__db_api.get_tasks_by_topic(topic_id)

    def delete_topic_by_id(self, topic_id):
        self.__db_api.delete_topic_by_id(topic_id)

    def delete_task_by_id(self, task_id):
        self.__db_api.delete_task_by_id(task_id)

    def get_coderunners(self):
        return self.__db_api.get_coderunners()

    def insert_task(self, task):
        return self.__db_api.insert_task(task)

    def insert_type(self, type_name):
        return self.__db_api.insert_type(type_name)

    def insert_topic(self, topic):
        return self.__db_api.insert_topic(topic)

    def insert_coderunner(self, coderunner):
        return self.__db_api.insert_coderunner(coderunner)

    def check_topic(self, topic):
        return self.__db_api.check_topic(topic)

    def check_name(self, name):
        return self.__db_api.check_name(name)

    def create_and_fill_task_by_id(self, task_id):
        self.__task_creator.create_and_fill_task_by_id(task_id)

    def create_variant_by_id(self, task_1_id, task_2_id, task_3_id):
        self.__variant_creator.create_variant_by_id(task_1_id, task_2_id, task_3_id)

    @staticmethod
    def format_task(task):
        """
        Format task from dict of lists to list of dicts in test_case
        :param task: task
        :return: task
        """
        test_cases = []
        for test_case in task['test_case']:
            test_cases.append({
                'use_as_example': [test_case['use_as_example']],
                'test_code': [test_case['test_code']],
                'stdin': [test_case['stdin']],
                'expected': [test_case['expected']]
            })
        task['test_case'] = test_cases
        return task
