from flask import Flask, render_template
from learn_project.model import db, Products


def create_app():
    app = Flask(__name__)  				 # создает экземпляр Flask в переменной app
    app.config.from_pyfile('config.py')  # задает файл конфигурационный файл
    db.init_app(app)					 # привязывает базу к приложению

    @app.route('/')  					 # путь, перейдя по котрому запустится app
    def index():  						 # возвращает стартовую страничку
        return render_template('index.html')

    @app.route('/ad_page/<prod_db_id>')
    def ad_page(prod_db_id):
        ad_items = Products.query.get(prod_db_id)
        return render_template('ad_page.html', ad_items=ad_items)
    return app  # возвращает экземпляр приложения Flask
