import os

basedir = os.path.abspath(os.path.dirname(__file__))  # абсолютный путь к файлу конфига

IMAGES_DIR = os.path.join('learn_project', 'static', 'pictures', '')
IMAGE_URL = os.path.sep.join(['', 'static', 'pictures', ''])
ITEMS_PER_PAGE = 5
PROXY = {'http': 'http://127.0.0.1:5566',
         'https': 'https://127.0.0.1:5566'}
SECRET_KEY = 'f6a205862b971721d3b1aaf0499be1262c2db7ab'
SENDGRID_API_KEY = 'API_KEY_HERE'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'learn_project.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SRC_MAIL = 'learn_project@mail.ru'
TARGET_URL = 'https://www.avito.ru/novosibirsk/drugie_zhivotnye/horki-ASgBAgICAUSyA65L?cd=1'
