from learn_project import config
from learn_project.model import db
from learn_project.advert.model import Products, Images


def save_products(name, price, date, text, address, ad_number, images_url_list, user_id=1, status='active'):  #передаём данные в базу
    products_exists = Products.query.filter(Products.ad_number == ad_number).count()  # проверка на дубликаты по номеру обьявления
    if not products_exists:
        all_products = Products(name=name,
                                price=price,
                                date=date,
                                text=text,
                                address=address,
                                ad_number=ad_number,
                                created_by=user_id,
                                status=status)
        db.session.add(all_products)  # кладем в сессию базы
        db.session.flush()            # добавляет данные в экземпляр таблицы, который без коммита пока лежит в приложении
                                      # благодаря этому мы можем на лету вытащить all_products.id (см. ниже)
        for url in images_url_list:
            add_url = Images(img_url=url, product_id=all_products.id)
            db.session.add(add_url)
        db.session.commit()  # сохранение всё в базу


def save_changes(name, price, text, address, file_urls, ad_id):
    changes = Products.query.get(ad_id)
    changes.name = name
    changes.price = price
    changes.text = text
    changes.address = address
    db.session.add(changes)
    if file_urls:
        add_url = Images(img_url=file_urls, product_id=ad_id)
        db.session.add(add_url)
    db.session.commit()


def save_new_ad(form, user_id):
    name        = form.name.data
    price       = str(form.price.data)
    date        = Products.default_date()
    text        = form.text.data
    address     = form.address.data
    ad_number   = Products.generate_ad_number()
    filename    = form.image.data.filename
    filename    = Products.generate_filename(filename)
    file_path   = config.IMAGES_DIR + filename
    file_urls   = [config.IMAGE_URL + filename]  # Это костыль т.к. функция сохранения принимает на вход список
    form.image.data.save(file_path)              # Да, пока умеем сохранять только один файл
    save_products(name, price, date, text, address, ad_number, file_urls, user_id)


def save_edit(form):
    ad_id       = form.ad_id.data
    name        = form.name.data
    price       = str(form.price.data)
    text        = form.text.data
    address     = form.address.data
    filename    = form.image.data.filename
    if filename:
        filename    = Products.generate_filename(filename)
        file_path   = config.IMAGES_DIR + filename
        file_urls   = config.IMAGE_URL + filename
        form.image.data.save(file_path)
    else:
        file_urls = ''
    save_changes(name=name, price=price, text=text, address=address,
                 file_urls=file_urls, ad_id=ad_id)
