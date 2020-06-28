from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from learn_project.model import db, Users
from learn_project.forms import LoginForm


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')  					 # путь, перейдя по котрому запустится app
    def index():  						 # возвращает стартовую страничку
        return render_template('index.html')

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/login-process', methods=['POST'])
    def login_process():
        form = LoginForm()

        if form.validate_on_submit:
            user = Users.query.filter(Users.username == form.username.data).first()

            if user and user.check_password(form.password.data):
                login_user(user)
                flash('logged in')
                return redirect(url_for('index'))

            flash('wrong login or password')
            return redirect(url_for('login'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Поздравляю! Вы админ.'
        else:
            return 'Вы не админ.'


    @app.route('/logout')
    def logout():
        logout_user()
        flash('bb gl hf')
        return redirect(url_for('index'))

    return app  # возвращает экземпляр приложения Flask