import click
from flask import Flask, request, send_file
from flask_cors import CORS
from waitress import serve
import xmltodict

import dataProcessor as dp
import dynamicHelp as dh
import parser


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
    task_type = request.args.get('type')
    difficulty = request.args.get('difficulty')
    topic = request.args.get('topic')
    return str(data_processor.get_quantity_tasks(topic, difficulty, task_type))


@app.route('/get-quantity-tasks-topic-diff', methods=['GET'])
def get_quantity_tasks_topic_diff():
    difficulty = request.args.get('difficulty')
    topic = request.args.get('topic')
    return str(data_processor.get_quantity_tasks(topic, difficulty))


@app.route('/get-uniq-percentages', methods=['GET'])
def get_uniq_percentages():
    print('get_uniq_percentages')


@app.route('/get-statistic', methods=['GET'])
def get_statistic():
    return data_processor.get_topics_and_quantity_tasks()


@app.route('/get-topics', methods=['GET'])
def get_topics():
    return data_processor.get_topics()


@app.route('/get-topic-name-by-id', methods=['GET'])
def get_topic_name_by_id():
    topic_id = request.args.get('topic-id')
    return data_processor.get_topic_name_by_id(topic_id)


@app.route('/get-tasks-by-topic', methods=['GET'])
def get_tasks_by_topic():
    topic_id = request.args.get('topic-id')
    return data_processor.get_tasks_by_topic(topic_id)


@app.route('/delete-topic-by-id', methods=['POST'])
def delete_topic_by_id():
    topic_id = request.args.get('topic-id')
    data_processor.delete_topic_by_id(topic_id)
    return '1'


@app.route('/get-task-name-by-id', methods=['POST'])
def delete_task_by_id():
    task_id = request.args.get('task-id')
    data_processor.delete_task_by_id(task_id)
    return '1'


@app.route('/get-coderunners', methods=['GET'])
def get_coderunners():
    return data_processor.get_coderunners()


@app.route('/import-task-from-file', methods=['GET', 'POST'])
def import_task_from_file():
    topic_id = request.args.get('topic')
    difficulty = request.args.get('difficulty')
    xml_data = request.files['data']
    content_dict = xmltodict.parse(xml_data)
    pars = parser.Parser()
    pars.parse_xml_dict(content_dict, topic_id, difficulty)

    return '1'


@app.route('/import-new-task', methods=['POST'])
def import_task():
    task = request.json
    task = data_processor.format_task(task)
    res = data_processor.insert_task(task)
    if res:
        return '1'
    else:
        return '0'


@app.route('/import-new-topic', methods=['POST'])
def export_new_topic():
    topic = request.args.get('topic')
    data_processor.insert_topic(topic)
    return '1'


@app.route('/check-topic-in-db', methods=['GET'])
def check_topic_in_db():
    topic = request.args.get('topic')
    return f'{data_processor.check_topic(topic)}'


@app.route('/check-name-in-db', methods=['GET'])
def check_name_in_db():
    name = request.args.get('name')
    return f'{data_processor.check_name(name)}'


@app.route('/export-task', methods=['GET'])
def export_task():
    task_id = request.args.get('id')
    data_processor.create_and_fill_task_by_id(task_id)
    return send_file('./task.xml', mimetype='text/xml', as_attachment=True, download_name='task.xml')


@app.route('/export-variant', methods=['GET'])
def export_variant():
    task_1_id = request.args.get('id-1')
    task_2_id = request.args.get('id-2')
    task_3_id = request.args.get('id-3')
    data_processor.create_variant_by_id(task_1_id, task_2_id, task_3_id)
    return send_file('./variant.zip', mimetype='text/xml', as_attachment=True, download_name='variant.zip')


if __name__ == "__main__":
    # create_task_by_cli()
    data_processor = dp.DataProcessor()
    context = ('local.crt', 'local.key')
    serve(app, host="192.168.0.6", port=8088)
