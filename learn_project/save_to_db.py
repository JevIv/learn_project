from learn_project.model import db
from learn_project.advert.model import Products, Images


def save_products(name, price, date, text, address, ad_number, images_url_list):  #передаём данные в базу
    products_exists = Products.query.filter(Products.ad_number == ad_number).count()  # проверка на дубликаты по номеру обьявления
    if not products_exists:
        all_products = Products(name=name,
                                price=price,
                                date=date,
                                text=text,
                                address=address,
                                ad_number=ad_number)
        db.session.add(all_products)  # кладем в сессию базы
        db.session.flush()            # добавляет данные в экземпляр таблицы, который без коммита пока лежит в приложении
                                      # благодаря этому мы можем на лету вытащить all_products.id (см. ниже)
        for url in images_url_list:
            add_url = Images(img_url=url, product_id=all_products.id)
            db.session.add(add_url)
        db.session.commit()  # сохранение всё в базу
