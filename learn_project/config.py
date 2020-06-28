import os

basedir = os.path.abspath(os.path.dirname(__file__))  # абсолютный путь к файлу конфига

PROXY = {'http': 'http://127.0.0.1:5566',
         'https': 'https://127.0.0.1:5566'}

TARGET_URL = 'https://www.avito.ru/novosibirsk/drugie_zhivotnye/horki-ASgBAgICAUSyA65L?cd=1'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'learn_project.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
<<<<<<< HEAD
ITEMS_PER_PAGE = 5
=======
SECRET_KEY = 'f6a205862b971721d3b1aaf0499be1262c2db7ab'
>>>>>>> a9ea3abc864face1ff46aba0c3c8ee0a258858f7
