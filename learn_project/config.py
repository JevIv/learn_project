import os

<<<<<<< HEAD
basedir = os.path.abspath(os.path.dirname(__file__)) # абсолютный путь к файлу конфига

TARGET_URL = 'http://avito.ru'
=======
basedir = os.path.abspath(os.path.dirname(__file__))  # абсолютный путь к файлу конфига

PROXY = {'http': 'http://127.0.0.1:5566',
         'https': 'https://127.0.0.1:5566'}

TARGET_URL = 'https://www.avito.ru/novosibirsk/drugie_zhivotnye/horki-ASgBAgICAUSyA65L?cd=1'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'learn_project.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'f6a205862b971721d3b1aaf0499be1262c2db7ab'
ITEMS_PER_PAGE = 5
SECRET_KEY = 'f6a205862b971721d3b1aaf0499be1262c2db7ab'
IMAGES_DIR = os.path.join('learn_project', 'static', 'pictures', '')
IMAGE_URL = os.path.sep.join(['', 'static', 'pictures', ''])
>>>>>>> e99760d2e5b23a0ba8ac435756c59baef3262361
