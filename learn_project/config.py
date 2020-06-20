import os

basedir = os.path.abspath(os.path.dirname(__file__))  # абсолютный путь к файлу конфига

PROXY = {'http': 'http://127.0.0.1:5566',
         'https': 'https://127.0.0.1:5566'}

TARGET_URL = 'https://www.avito.ru/novosibirsk/drugie_zhivotnye/horki-ASgBAgICAUSyA65L?cd=1'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'learn_project.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
