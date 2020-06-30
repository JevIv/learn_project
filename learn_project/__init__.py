from flask import Flask, render_template, request, url_for
from learn_project.model import db, Products, Images


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению

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

    return app  # возвращает экземпляр приложения Flask
