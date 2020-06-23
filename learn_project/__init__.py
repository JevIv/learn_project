from flask import Flask, render_template
from learn_project.model import db, Products


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
        products_list = Products.query.order_by(Products.date.desc()).limit(20).all()	        #запрашиваем 20 товаров сортируем по дате
        return render_template('products.html', page_title=title, products_list=products_list)	#limit(20)-до 20 товаров


    return app  # возвращает экземпляр приложения Flask
