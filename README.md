# Генератор задач на программирование на Python

## Описание
Генератор задач на программирование на Python - приложение с web-интерфейсом для генерации задач на защиты лабораторных работ по информатике на кафедре МО ЭВМ СПбГЭТУ "ЛЭТИ".<br>
Данное приложение позволяет пользователю сгенерировать задачу по трем критериям: тип, тема и сложность, ткже приложение поддерживает генерацию варианта из трех задач. Сгенерированные задачи пользователь може скачать в виде XML-файлов для дальнейше загрузки в СДО Moodle.<br><br>

При необходимости пользователь может загрузить новые задачи в базу данных тремя способами: 
- Moodle XML файл.
- URL задачи в СДО Moodle
- Форма

## Начало использование
Перед начало использования скопируйте данные репозитория в локальную дирректорию. <br>
Для загрузки задач из СДО Moodle по URL заполните *username* и *password* в файле backend/payload.json, указав данные аккаунта с доступом к заданиям. <br>
Процесс запуска:
1. Если у вас не установлен PostgreSQL-14, запустите bash-скрипт *postgres_install.sh* <br>
```bash ./DB/postgres_install.sh```
2. Для создания БД запустите скрипт *db_create.sh* <br>
```bash ./DB/db_create.sh```
3. Для заполнения БД задачи, использованными с осени 2020 года по осень 2023 года запустите Python-скрипт *parse.py* <br>
```python3 ./backend/parse.py```
4. Для запуска backend части приложения запустите Python-скрипт *main.py* <br>
```python3 ./backend/main.py```
5. Для запуска frontend части в отдельном окне терминала введите следующие команды:<br>
```cd ./frontend```<br>
```npm run install```<br>
```npm run serve```

<br><br>
После запуска web-интерфейс будет доступен по адресу `localhost:1024`

