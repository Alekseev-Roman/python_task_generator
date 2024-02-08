# Create DB

sudo -i -u postgres bash -c "
createdb cs_labworks;
psql -c \"\connect cs_labworks\" -c \"
ALTER USER postgres PASSWORD 'postgres';
CREATE TABLE theme (theme_id serial PRIMARY KEY, theme_name varchar(64));
CREATE TABLE type (type_id serial PRIMARY KEY, type_name varchar(64));
CREATE TABLE task (task_id serial PRIMARY KEY, theme_id serial REFERENCES theme (theme_id), type_id serial REFERENCES type (type_id), difficulty smallserial, question_name varchar(32), question_text text);
CREATE TABLE coderunner_task (task_id serial REFERENCES task (task_id), template text, template_params varchar(64), answer_preload varchar(128));
CREATE TABLE test_case (task_id serial REFERENCES task (task_id), use_as_example boolean, test_code varchar(64), expected varchar(64));
CREATE TABLE multichoice_task (task_id serial REFERENCES task (task_id), penalty decimal);
CREATE TABLE multichoice_answer (task_id serial REFERENCES task (task_id), answer_fraction smallint, answer varchar(192));
\""

