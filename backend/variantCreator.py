import json
import zipfile

from taskCreator import TaskCreator


class VariantCreator:
    def __init__(self, db_api):
        self.__db_API = db_api
        self.__task_creator = TaskCreator(db_api)

    def create_variant(self, path):
        """
        Create variant of three tasks with topics and types
        :return:
        """
        try:
            with open(path, 'r') as file:
                var_params = json.loads(file.read())

            try:
                task_1 = self.__task_creator.create_task(var_params['task_1']['topic'], var_params['task_1']['type'], 1)
                task_2 = self.__task_creator.create_task(var_params['task_2']['topic'], var_params['task_2']['type'], 2)
                task_3 = self.__task_creator.create_task(var_params['task_3']['topic'], var_params['task_3']['type'], 3)

                if not task_1:
                    print('Task 1 cannot be created. Change topic or type of this task.')
                if not task_2:
                    print('Task 2 cannot be created. Change topic or type of this task.')
                if not task_3:
                    print('Task 3 cannot be created. Change topic or type of this task.')

                if task_1 and task_2 and task_3:
                    self.__task_creator.set_type_id(var_params['task_2']['type'])
                    self.__task_creator.set_task_for_template(task_2)
                    self.__task_creator.fill_template_of_task('task_1.xml')

                    self.__task_creator.set_type_id(var_params['task_2']['type'])
                    self.__task_creator.set_task_for_template(task_2)
                    self.__task_creator.fill_template_of_task('task_2.xml')

                    self.__task_creator.set_type_id(var_params['task_3']['type'])
                    self.__task_creator.set_task_for_template(task_3)
                    self.__task_creator.fill_template_of_task('task_3.xml')

            except Exception as e:
                print("Error creating tasks, not enough data for creating in the file.")
                print(e)

        except FileNotFoundError:
            print(f"File {path} for creating variant not found.")

    def create_variant_by_id(self, task_1_id, task_2_id, task_3_id, name='variant.zip'):
        """
        Create variant with 3 task. Variant is saved to XML file
        :param task_1_id: ID of task
        :param task_2_id: ID of task
        :param task_3_id: ID of task
        :return: None
        """
        task_1 = self.__task_creator.create_task_by_id(task_1_id)
        task_2 = self.__task_creator.create_task_by_id(task_2_id)
        task_3 = self.__task_creator.create_task_by_id(task_3_id)

        if not task_1:
            print('Task 1 cannot be created. Change topic or type of this task.')
        if not task_2:
            print('Task 2 cannot be created. Change topic or type of this task.')
        if not task_3:
            print('Task 3 cannot be created. Change topic or type of this task.')

        if task_1 and task_2 and task_3:
            self.__task_creator.set_type_id(task_1['type_id'])
            self.__task_creator.set_task_for_template(task_1)
            self.__task_creator.fill_template_of_task('task_1.xml')

            self.__task_creator.set_type_id(task_2['type_id'])
            self.__task_creator.set_task_for_template(task_2)
            self.__task_creator.fill_template_of_task('task_2.xml')

            self.__task_creator.set_type_id(task_3['type_id'])
            self.__task_creator.set_task_for_template(task_3)
            self.__task_creator.fill_template_of_task('task_3.xml')

            with zipfile.ZipFile(name, mode="w") as archive:
                archive.write('task_1.xml')
                archive.write('task_2.xml')
                archive.write('task_3.xml')
