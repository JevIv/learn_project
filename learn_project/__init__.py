#запуск сервера
#set FLASK_APP=webapp && set FLASK_ENV=development && 
#set FLASK_DEBUG=1 && flask run
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from learn_project.model import db, Users, Products, Images
from learn_project.forms import LoginForm, RegistrationForm, Email, EqualTo
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')  					 # путь, перейдя по котрому запустится app
    def index():  						 # возвращает стартовую страничку
        return render_template('index.html')

    @app.route('/products')
    def products():
        
        title = 'Товары'
        page = request.args.get('page', 1, type=int)
        products_list = Products.query.order_by(Products.date.desc()).paginate(page,
                                                                               app.config['ITEMS_PER_PAGE'],
                                                                               False)
        prev_url = url_for('products', page=products_list.prev_num) \
        if products_list.has_prev else None

        next_url = url_for('products', page=products_list.next_num) \
        if products_list.has_next else None

        return render_template('products.html',
                                page_title=title,
                                products_list=products_list.items,
                                next_url=next_url, 
                                prev_url=prev_url)

    @app.route('/ad_page/<prod_db_id>')
    def ad_page(prod_db_id):
        ad_items = Products.query.get(prod_db_id)
        image_urls = Images.query.filter_by(product_id=prod_db_id).all()  # возвращает список объектов класса
        image_urls = [image_url.img_url for image_url in image_urls]      # вытаскиваем из этих объектов ссылки и кладём в список
        return render_template('ad_page.html', ad_items=ad_items, image_urls=image_urls)

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


    @app.route('/register')
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('news.index'))
        form = RegistrationForm()
        title = "Регистрация"
        return render_template('user/registration.html', page_title=title, form=form)


    @app.route('/process-reg', methods=['POST'])
    def process_reg():
        form = RegistrationForm()
        if form.validate_on_submit():
            new_user = User(username=form.username.data, email=form.email.data, role='user')
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегистрировались!')
            return redirect(url_for('user.login'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash('Ошибка в поле "{}": - {}'.format(
                        getattr(form, field).label.text,
                        error
                    ))
            return redirect(url_for('user.register'))
            flash('Пожалуйста, исправьте ошибки в форме')

    return app  # возвращает экземпляр приложения Flask
