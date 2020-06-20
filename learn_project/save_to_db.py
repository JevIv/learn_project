"""Модуль сохраняет в базу продукты из словаря"""
from learn_project.model import db, Products


def save_products(d_dict):   #передаём данные в базу
    #products_exists = Products.query.filter(Products.ad_number == d_dict['ad_number']) 		#проверка на дубликаты по номеру обьявления
    #if not products_exists:
    all_products = Products(name=d_dict['name'], text=d_dict['text'], price=d_dict['price'], address=d_dict['address'], published=d_dict['date'], ad_number=d_dict['ad_number'], images_urls=d_dict['images_urls'])
    db.session.add(all_products)           										#кладем в сессию базы
    db.session.commit()                											#сохранение новости в базу
