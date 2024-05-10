class Templater:
    def __init__(self, file_name=''):
        """
        Initialize Templater
        :param file_name:
        """
        self.file_name = file_name
        self.template = None

        self.data = None

    def open_file(self):
        """
        Open and read template file
        :return:
        """
        try:
            with open(self.file_name, 'r') as file:
                self.template = file.read()
        except FileNotFoundError:
            print(f"Template file - {self.file_name} wasn't found.")

    def set_data(self, data):
        """
        Set data for filling templater later
        :param data: tuple of tasks
        :return:
        """
        self.data = data

    def fill_code_runner_template_file(self, name):
        self.open_file()

        try:
            self.template = self.template.replace('{{question_name}}', self.data['question_name'])
            self.template = self.template.replace('{{question_text}}', self.data['question_text'])
            self.template = self.template.replace('{{coderunner_type}}', self.data['coderunner_type'])
            self.template = self.template.replace('{{template}}', self.data['template'])
            self.template = self.template.replace('{{answer_preload}}', self.data['answer_preload'])
            self.template = self.template.replace('{{template_params}}', self.data['template_params'])
            for i in range(len(self.data['test_cases']['test_code'])):
                self.template = self.template.replace(
                    '{{testcase}}',
                    f'<testcase testtype="0" useasexample="{str(self.data["test_cases"]["use_as_example"])}" '
                    f'hiderestiffail="1" mark="1.0000000" >\n'
                    f'    <testcode>\n'
                    f'        <text>{str(self.data["test_cases"]["test_code"])}</text>\n'
                    f'    </testcode>\n'
                    f'    <stdin>\n'
                    f'        <text></text>\n'
                    f'    </stdin>\n'
                    f'    <expected>\n'
                    f'        <text>{str(self.data["test_cases"]["expected"])}</text>\n'
                    f'    </expected>\n'
                    f'    <extra>\n'
                    f'        <text></text>\n'
                    f'    </extra>\n'
                    f'    <display>\n'
                    f'        <text>SHOW</text>\n'
                    f'    </display>\n'
                    f'{{{{testcase}}}}'
                )
            self.template = self.template.replace('{{testcase}}', '')

        except ValueError:
            print("Coderunner template file can't be filled. There aren't enough data for template.")

        with open(name, 'w+') as file:
            file.write(self.template)

    def fill_multichoice_template_file(self, name):
        self.open_file()

        try:
            self.template = self.template.replace('{{question_name}}', self.data['question_name'])
            self.template = self.template.replace('{{question_text}}', self.data['question_text'])
            self.template = self.template.replace('{{penalty}}', str(self.data['penalty']))
            for i in range(len(self.data['answers']['answer'])):
                self.template = self.template.replace(
                    '{{answer}}',
                    f'<answer fraction="{str(self.data["answers"]["answer_fraction"][i])}" format="html">\n'
                    f'    <text><![CDATA[{str(self.data["answers"]["answer"][i])}]]></text>\n'
                    f'    <feedback format="html">\n'
                    f'        <text></text>\n'
                    f'    </feedback>\n'
                    f'</answer>\n'
                    f'{{{{answer}}}}'
                )
            self.template = self.template.replace('{{answer}}', '')
        except ValueError:
            print("Multichoice template file can't be filled. There aren't enough data for template.")

        with open(name, 'w+') as file:
            file.write(self.template)

