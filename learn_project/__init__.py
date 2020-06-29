from flask import Flask, render_template
from flask_login import LoginManager, current_user, login_required
from learn_project.model import db
from learn_project.user.model import Users
from learn_project.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')  					 # путь, перейдя по котрому запустится app
    def index():  						 # возвращает стартовую страничку
        return render_template('index.html')

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Поздравляю! Вы админ.'
        else:
            return 'Вы не админ.'

    return app  # возвращает экземпляр приложения Flask
