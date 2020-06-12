from flask import Flask, render_template
import config as cfg


def create_app():
    app = Flask(__name__)  # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    @app.route('/')  # путь, перейдя по котрому запустится app
    def index():  # возвращает стартовую страничку
        return render_template('index.html')
    return app  # возвращает экземпляр приложения Flask