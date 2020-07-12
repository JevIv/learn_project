from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user
from learn_project import config, db
from learn_project.advert.model import Products, Images
from learn_project.advert.forms import NewAdForm
from learn_project.save_to_db import save_products as save_new_ad

blueprint = Blueprint('advert', __name__, url_prefix='/adverts')


@blueprint.route('/products')
def products():

    title = 'Товары'
    page = request.args.get('page', 1, type=int)
    products_list = Products.query.order_by(Products.date.desc()).paginate(page,
                                                                           config.ITEMS_PER_PAGE,
                                                                           False)
    prev_url = url_for('advert.products', page=products_list.prev_num) \
        if products_list.has_prev else None

    next_url = url_for('advert.products', page=products_list.next_num) \
        if products_list.has_next else None

    return render_template('advert/products.html',
                           page_title=title,
                           products_list=products_list.items,
                           next_url=next_url,
                           prev_url=prev_url)


@blueprint.route('/ad_page/<prod_db_id>')
def ad_page(prod_db_id):
    ad_items = Products.query.get(prod_db_id)
    date = ad_items.date.strftime('%d.%m.%Y %H:%M')
    image_urls = Images.query.filter_by(product_id=prod_db_id).all()  # возвращает список объектов класса
    image_urls = [image_url.img_url for image_url in image_urls]      # вытаскиваем из этих объектов ссылки и кладём в список
    return render_template('advert/ad_page.html', ad_items=ad_items,
                            date=date, image_urls=image_urls)


@blueprint.route('/new_ad')
def new_ad():
    if current_user.is_authenticated:
        form = NewAdForm()
        title = 'Новое объявление'
        return render_template('advert/new_ad.html', page_title=title, form=form)
    else:
        flash('авторизуйтесь')
        return redirect(url_for('user.login'))


@blueprint.route('/new_ad-process', methods=['GET', 'POST'])
def new_ad_process():
    form = NewAdForm()
    if form.validate_on_submit():

        name        = form.name.data
        price       = str(form.price.data)
        date        = Products.default_date()
        text        = form.text.data
        address     = form.address.data
        ad_number   = Products.generate_ad_number()
        user_id     = current_user.id
        filename    = form.image.data.filename
        filename    = Products.generate_filename(filename)
        file_path   = config.IMAGES_DIR + filename
        file_urls   = [config.IMAGE_URL + filename]  # Это костыль т.к. функция сохранения принимает на вход список

        form.image.data.save(file_path)  # Да, пока умеем сохранять только один файл
        save_new_ad(name, price, date, text, address, ad_number, file_urls, user_id)
        flash('Ваше объявление принято!')
        return redirect(url_for('index'))

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        flash('Где-то ошибка')
        return redirect(url_for('index'))


@blueprint.route('/own_ads')
def own_ads():
    title = 'Мои объявления'
    ad_list = Products.query.filter_by(created_by=current_user.id)
    ad_list = ad_list.order_by(Products.date.desc())
    return render_template('/advert/products.html',
                            page_title=title,
                            products_list=ad_list)
