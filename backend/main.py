import click
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from waitress import serve

import dataProcessor as dp
import dynamicHelp as dh


@click.command(cls=dh.DynamicHelp)
@click.option('--topic', '-t', type=click.INT, help='The topic number of task: ')
@click.option('--type', '-T', type=click.IntRange(1, 2), help='The number of type of task: ')
@click.option('--difficulty', '-d', type=click.IntRange(1, 3),
              help='The difficulty of task between 1 and 3')
@click.option('--variant', type=str, help='Create a variant containing three tasks. Topics and types '
                                          'provided from a JSON file.')
def create_task_by_cli(topic, type, difficulty, variant):
    """
    Function for creating a task by CLI
    :param topic: Topic ID
    :param type: Type ID
    :param difficulty: Difficulty
    :return: None
    """
    data = dp.DataProcessor()

    if topic is not None and type is not None and difficulty is not None and variant is None:
        data.create_and_fill_task(topic, type, difficulty)

    if variant is not None and topic is None and type is None and difficulty is None:
        data.create_variant(variant)


app = Flask(__name__)
cors = CORS(app)


@app.route('/generate-task', methods=['GET'])
def generate_task():
    task_type = request.args.get('type')
    difficulty = request.args.get('difficulty')
    topic = request.args.get('topic')
    task = data_processor.create_task(topic, task_type, difficulty)
    if task:
        return task
    return {}


@app.route('/generate-variant', methods=['GET'])
def generate_variant():
    task_type_1 = request.args.get('type-1')
    topic_1 = request.args.get('topic-1')
    difficulty_1 = request.args.get('difficulty-1')
    task_type_2 = request.args.get('type-2')
    topic_2 = request.args.get('topic-2')
    difficulty_2 = request.args.get('difficulty-2')
    task_type_3 = request.args.get('type-3')
    topic_3 = request.args.get('topic-3')
    difficulty_3 = request.args.get('difficulty-3')

    task_1 = data_processor.create_task(topic_1, task_type_1, difficulty_1)
    task_2 = data_processor.create_task(topic_2, task_type_2, difficulty_2)
    task_3 = data_processor.create_task(topic_3, task_type_3, difficulty_3)
    return {1: task_1, 2: task_2, 3: task_3}


@app.route('/get-quantity-tasks', methods=['GET'])
def get_quantity_tasks():
    taskType = request.args.get('type')
    difficulty = request.args.get('difficulty')
    topic = request.args.get('topic')

    return str(data_processor.get_quantity_tasks(topic, taskType, difficulty))


@app.route('/get-uniq-percentages', methods=['GET'])
def get_uniq_percentages():
    print('get_uniq_percentages')


@app.route('/get-statistic', methods=['GET'])
def get_statistic():
    print('get_statistic')


@app.route('/get-topics', methods=['GET'])
def get_topics():
    return data_processor.get_topics()


@app.route('/import-task-from-file', methods=['GET'])
def import_task_from_file():
    print('import_task_from_file')


@app.route('/import-new-task', methods=['POST'])
def import_task():
    print('import_task')


@app.route('/import-new-topic', methods=['POST'])
def export_new_topic():
    topic = request.args.get('topic')
    #data_processor.insert_topic(topic)
    return "0"


@app.route('/check-topic-in-db', methods=['GET'])
def check_topic_in_db():
    topic = request.args.get('topic')
    return f'{data_processor.check_topic(topic)}'


@app.route('/export-task', methods=['GET'])
def export_task():
    task_id = request.args.get('id')
    data_processor.create_and_fill_task_by_id(task_id)
    return send_file('./task.xml', mimetype='text/xml', as_attachment=True, download_name='task.xml')


if __name__ == "__main__":
    # parser = parser.Parser()
    # parser.parse()
    # create_task_by_cli()
    data_processor = dp.DataProcessor()
    data_processor.connecting_to_db()
    context = ('local.crt', 'local.key')
    serve(app, host="192.168.0.6", port=8088)
