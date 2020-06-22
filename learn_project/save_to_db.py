from learn_project.model import db, Products
from learn_project.__init__ import create_app


<<<<<<< HEAD
def save_products(details_list):  #передаём данные в базу
    app = create_app()
    with app.app_context():
        for details in details_list:
            products_exists = Products.query.filter(Products.ad_number == details['ad_number']).count()  # проверка на дубликаты по номеру обьявления
            print(products_exists)
            if not products_exists:
                all_products = Products(name=details['name'],
                                        price=details['price'],
                                        date=details['date'],
                                        text=details['text'],
                                        address=details['address'],
                                        ad_number=details['ad_number'],
                                        images_urls=details['images_urls'])
                db.session.add(all_products)  # кладем в сессию базы
                db.session.commit()  # сохранение новости в базу
=======
def save_products(d_dict):   #передаём данные в базу
    #products_exists = Products.query.filter(Products.ad_number == d_dict['ad_number']) 		#проверка на дубликаты по номеру обьявления
    #if not products_exists:
    all_products = Products(name=d_dict['name'], text=d_dict['text'], price=d_dict['price'], address=d_dict['address'], published=d_dict['date'], ad_number=d_dict['ad_number'], images_urls=d_dict['images_urls'])
    db.session.add(all_products)           										#кладем в сессию базы
    db.session.commit()                											#сохранение новости в базу
>>>>>>> c6eec89d4438f9f33831bc06a7b5c10eb8adf786
