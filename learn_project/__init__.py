#запуск сервера
#set FLASK_APP=webapp && set FLASK_ENV=development && 
#set FLASK_DEBUG=1 && flask run
from flask import Flask, render_template, request, url_for
from flask_login import LoginManager, current_user, login_required
from learn_project.model import db, Products, Images, Comments
from learn_project.user.model import Users
from learn_project.user.views import blueprint as user_blueprint
from flask_migrate import Migrate
from learn_project.forms import AddCommentForm


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    migrate = Migrate(app, db)

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


    @app.route("/comment", methods=["GET", "POST"])
    #@app.route("/ad_page/<prod_db_id>/comment", methods=["GET", "POST"])
    @login_required
    def comment_post(product_id):
        product = Products.query.get_or_404(product_id)
        form = AddCommentForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                comments = Comments(body=form.body.data, article=products.id)
                db.session.add(comments)
                db.session.commit()
                flash("Ваш коментарий был добавлен!")
                return redirect(url_for("post", product_id=products.id))
        return render_template("comment_post.html", title="Добавить коментарий", form=form, product_id=product_id)

    return app  # возвращает экземпляр приложения Flask
