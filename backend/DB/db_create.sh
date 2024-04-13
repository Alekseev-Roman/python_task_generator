# Create DB

sudo -i -u postgres bash -c "
createdb cs_labworks;
psql -c \"\connect cs_labworks\" -c \"
ALTER USER postgres PASSWORD 'postgres';
CREATE TABLE topic (topic_id serial PRIMARY KEY, topic_name varchar(64));
CREATE TABLE type (type_id serial PRIMARY KEY, type_name varchar(64));
CREATE TABLE coderunner_types (coderunner_id serial PRIMARY KEY, coderunner_name varchar(64));
CREATE TABLE task (task_id serial PRIMARY KEY, topic_id serial REFERENCES topic (topic_id), type_id serial REFERENCES type (type_id), difficulty smallserial, question_name varchar(128), question_text text);
CREATE TABLE coderunner_task (task_id serial REFERENCES task (task_id) PRIMARY KEY, coderunner_id serial REFERENCES coderunner_types (coderunner_id), template text, template_params varchar(64), answer_preload varchar(128));
CREATE TABLE test_case (test_case_id serial PRIMARY KEY, task_id serial REFERENCES task (task_id), use_as_example boolean, test_code text, expected text);
CREATE TABLE multichoice_task (task_id serial REFERENCES task (task_id) PRIMARY KEY, penalty decimal);
CREATE TABLE multichoice_answer (multichoice_answer_id serial PRIMARY KEY, task_id serial REFERENCES task (task_id), answer_fraction decimal, answer varchar(192));
\""

