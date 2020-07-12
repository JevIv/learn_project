#запуск сервера
#set FLASK_APP=webapp && set FLASK_ENV=development && 
#set FLASK_DEBUG=1 && flask run
from flask import Flask, render_template
from flask_login import LoginManager
from learn_project.model import db
from learn_project.user.model import Users
from learn_project.user.views import blueprint as user_blueprint
from learn_project.advert.views import blueprint as advert_blueprint
from learn_project.comments.views import blueprint as comments_blueprint
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(advert_blueprint)
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')  					 # путь, перейдя по котрому запустится app
    def index():  						 # возвращает стартовую страничку
        return render_template('advert/index.html', page_title='Тут вам не авито!')

    return app  # возвращает экземпляр приложения Flask
