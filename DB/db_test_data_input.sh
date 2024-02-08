# Pull DB by test data

sudo -i -u postgres bash -c "
psql -c \"\connect cs_labworks\" -c \"
INSERT INTO theme (theme_id, theme_name) VALUES
	(0, 'Словари и списки'),
	(1, 'Машина Тьюринга'),
	(2, 'Представление вещетвенного числа в памяти');
INSERT INTO type (type_id, type_name) VALUES
	(0, 'Выбор одного правильного ответа'),
	(1, 'Выбор нескольких правильных ответов'),
	(2, 'Написание кода');
INSERT INTO task (task_id, theme_id, type_id, difficulty, question_name, question_text) VALUES
	(0, 0, 2, 1, 'first_question', 'first_question text'),
	(1, 1, 0, 2, 'second_question', 'second_question text'),
	(2, 2, 1, 3, 'thrid_question', 'thrid_question text');
INSERT INTO coderunner_task (task_id, template, template_params, answer_preload) VALUES
	(2, 'template thrid_question', 'params', 'preload');
INSERT INTO test_case (task_id, use_as_example, test_code, expected) VALUES
	(2, TRUE, 'test_code', 'expected');
INSERT INTO multichoice_task (task_id, penalty) VALUES
	(0, 100.0),
	(1, 50.0);
INSERT INTO multichoice_answer (task_id, answer_fraction, answer) VALUES
	(0, 100, 'da'),
	(1, 50, 'net'),
	(1, 50, 'ne znay');
\""

