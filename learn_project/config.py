import os

basedir = os.path.abspath(os.path.dirname(__file__))  # абсолютный путь к файлу конфига
<<<<<<< HEAD

PROXY = {'http': 'http://127.0.0.1:5566',
         'https': 'https://127.0.0.1:5566'}

=======
>>>>>>> dc7f625ed7cfc88455eaccf4cdb448cf76081c34
TARGET_URL = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/zvukovye_karty-ASgBAgICAkTGB~pm7gm6Zw?cd=1'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'learn_project.db')