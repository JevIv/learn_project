"""Модуль сохраняет в базу продукты из словаря"""
from learn_project.model import db, Products

def save_products(name, text, price, address, published, ad_number, images_urls):   #передаём данные в базу
    products_exists = Products.query.filter(Products.ad_number == ad_number) 		#проверка на дубликаты по номеру обьявления
    if not products_exists:
        all_products = Products(name=name, text=text, price=price, address=address, published=published, ad_number=ad_number, images_urls=images_urls)
        db.session.add(all_products)           										#кладем в сессию базы
        db.session.commit()                											#сохранение новости в базу