# lybrary

Хранилище данных. Можно передать ссылку на страницу или внести информацию в реадктор (WYSIWYG).
Пользователи и группы.
Иерархия каталогов.

Основан на следующих компонентах:

* Python 3
* CherryPy
* python-lxml
* psycopg2
* руки из плеч

Данные хранятся только в базе PostgreSQL. Никакой кучи файлов.

Запускаем, как самостоятельный сервер:

`./lyb`

или подключаем в WEB-сервер fcgi-скрипт lybrary.fcgi
