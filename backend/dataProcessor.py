import pandas as pd
import psycopg2 as ps
import json
import sys

import templater as tem

class DataProcessor:
    def __init__(self):
        """
        Initialize the Data class for storing and processing data from DB
        """
        self.conn = None
        self.params_dic = None

        # Data
        self.themes = None
        self.types = None
        self.tasks = None
        self.coderunner_tasks = None
        self.test_cases = None
        self.multichoice_tasks = None
        self.multichoice_answers = None

        # IDs
        self.theme_id = None
        self.type_id = None
        self.task_id = None

        self.difficulty = None
        self.task = None

        # Flags
        self.its_multichoice_task = False

    def readConnectData(self):
        """
        Read data for connecting to DB from file params.json
        :return: None
        """
        with open('params.json', 'r') as file:
            self.params_dic = json.loads(file.read())

    def connectingToDB(self):
        """
        Connect to the DataBase and return the connection
        :param params_dic:
        :return conn:
        """

        self.conn = None
        try:
            self.conn = ps.connect(**self.params_dic)
        except (Exception, ps.DatabaseError) as error:
            print(error)
            sys.exit(1)
        return self.conn

    def getData(self):
        """
        Get data from DataBase
        :return : data
        """

        self.tasks = pd.read_sql(f"SELECT * "
                                 f"FROM task "
                                 f"WHERE type_id = {self.type_id} AND theme_id = {self.theme_id}"
                                 f" AND difficulty = {self.difficulty}",
                                 self.conn)

        if self.tasks.shape[0] > 0:
            self.task = self.tasks.sample()
            self.task_id = self.task['task_id'][0]

        if self.its_multichoice_task:
            self.multichoice_tasks = pd.read_sql(f"SELECT * "
                                                 f"FROM multichoice_task "
                                                 f"WHERE task_id = {self.task_id}",
                                                 self.conn)
            self.multichoice_answers = pd.read_sql(f"SELECT * "
                                                   f"FROM multichoice_answer "
                                                   f"WHERE task_id = {self.task_id}",
                                                   self.conn)
        else:
            self.coderunner_tasks = pd.read_sql(f"SELECT * "
                                                f"FROM coderunner_task "
                                                f"WHERE task_id = {self.task_id}",
                                                self.conn)
            self.test_cases = pd.read_sql(f"SELECT * "
                                          f"FROM test_case "
                                          f"WHERE task_id = {self.task_id}",
                                          self.conn)

    def inputData(self):
        """
        Input data and insert data to DB
        :return: None
        """
        pass

    def fillTemplateOfTask(self):
        """
        Fill in the template of a task
        :return: File Moodle XML with a task
        """
        if self.type_id == 0:
            fileName = "coderunner_template.xml"
        else:
            fileName = "multichoice_template.xml"

        templater = tem.Templater(f"./templates/{fileName}")
        templater.setData(self.task.to_dict())
        templater.fillTemplateFile()

    def createTask(self, theme, type, difficulty):
        """
        Create task with topic, difficulty and type
        :return: dictionary with task
        """
        self.readConnectData()
        self.connectingToDB()

        self.theme_id = theme
        self.type_id = type
        self.difficulty = difficulty

        self.getData()

    def createVariant(self):
        """
        Create variant of three tasks with topics and types
        :return: dictionary with tasks
        """
        pass
