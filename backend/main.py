import click

import dataProcessor as dp

@click.command()
@click.option('--topic', '-t', type=click.INT, help='The topic number of task: '
                                                    '0 - Dictionaries and lists, '
                                                    '1 - The Turing machine,'
                                                    '2 - Number systems, '
                                                    '3 - Representation of a real number in memory, '
                                                    '4 - Image processing, '
                                                    '5 - Decorators, '
                                                    '6 - Linked list, '
                                                    '7 - Functional programming, '
                                                    '8 - Classes')
@click.option('--type', '-T', type=click.IntRange(0, 2), help='The number of type of task: '
                                                              '0 - Task with code, '
                                                              '1 - Multichoice task with one correct answer, '
                                                              '2 - Multichoice task with several correct answers')
@click.option('--difficulty', '-d', type=click.IntRange(0, 2),
              help='The difficulty of task between 0 and 2')
def createTaskByCLI(topic, type, difficulty):
    """
    Function for creating a task by CLI
    :param topic:
    :param type:
    :param difficulty:
    :return:
    """
    data = dp.DataProcessor()
    data.createTask(topic, type, difficulty)
    data.fillTemplateOfTask()


if __name__ == "__main__":
    createTaskByCLI()
