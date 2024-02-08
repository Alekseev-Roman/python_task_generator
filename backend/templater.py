import os


class Templater:
    def __init__(self, fileName):
        """
        Initialize Templater
        :param fileName:
        """
        self.fileName = fileName
        self.template = None

        self.data = None

    def openFile(self):
        """
        Open and read template file
        :return:
        """
        with open(self.fileName, 'r') as file:
            self.template = file.read()

    def setData(self, data):
        """
        Set data for filling templater later
        :param data:
        :return:
        """
        self.data = data

    def fillTemplateFile(self):
        self.openFile()

        self.template = self.template.replace('{{question_name}}', self.data['question_name'][0])
        self.template = self.template.replace('{{question_text}}', self.data['question_text'][0])
        # self.template = self.template.replace('{{coderunner_type}}', self.data[''][0])
        # self.template = self.template.replace('{{answer_preload}}', self.data[''][0])
        # self.template = self.template.replace('{{template}}', self.data[''][0])
        # self.template = self.template.replace('{{template_params}}', self.data[''][0])
        # self.template = self.template.replace('{{test_code}}', self.data[''][0])
        # self.template = self.template.replace('{{expected}}', self.data[''][0])

        with open('task.xml', 'w+') as file:
            file.write(self.template)


