from learn_project.model import db, Products
from learn_project import create_app


def save_products(name, price, date, text, address, ad_number, images_urls):  #передаём данные в базу
    products_exists = Products.query.filter(Products.ad_number == ad_number).count()  # проверка на дубликаты по номеру обьявления
    if not products_exists:
        all_products = Products(name=name,
                                price=price,
                                date=date,
                                text=text,
                                address=address,
                                ad_number=ad_number,
                                images_urls=images_urls)
        db.session.add(all_products)  # кладем в сессию базы
        db.session.commit()  # сохранение новости в базу
