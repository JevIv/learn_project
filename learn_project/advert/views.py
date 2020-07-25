from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user
from learn_project import config, db
from learn_project.advert.model import Products, Images
from learn_project.advert.forms import NewAdForm
from learn_project.save_to_db import save_new_ad
from learn_project.save_to_db import save_edit
from learn_project.comments.forms import CommentForm


blueprint = Blueprint('advert', __name__, url_prefix='/adverts')


@blueprint.route('/products') # Страница со всеми объявлениями
def products():
    title           = 'Товары'
    page            = request.args.get('page', 1, type=int)
    active_ads      = Products.query.filter_by(status='active')
    products_list   = active_ads.order_by(Products.date.desc())
    products_list   = products_list.paginate(page, config.ITEMS_PER_PAGE, False)
    prev_url        = url_for('advert.products', page=products_list.prev_num) \
        if products_list.has_prev else None
    next_url        = url_for('advert.products', page=products_list.next_num) \
        if products_list.has_next else None

    return render_template('advert/products.html',
                           page_title=title,
                           products_list=products_list.items,
                           next_url=next_url,
                           prev_url=prev_url)


@blueprint.route('/ad_page/<prod_db_id>')  # Страница одного объявления
def ad_page(prod_db_id):
    ad_items    = Products.query.get(prod_db_id)
    date        = ad_items.pretty_date()
    image_urls  = Images.query.filter_by(product_id=prod_db_id).all()  # возвращает список объектов класса
    image_urls  = [image_url.img_url for image_url in image_urls]      # вытаскиваем из этих объектов ссылки и кладём в список
    image_urls  = enumerate(image_urls)                                # это чтобы в рендер передать индексы элементов списка
    comment_form = CommentForm(product_id=prod_db_id)                  
    if current_user.is_anonymous:                                      # без этой проверки ошибка базы если пользователь не залогинен
        owner   = False
    else:
        owner   = True if ad_items.created_by == current_user.id else False  # является ли юзер создателем объявления
    return render_template('advert/ad_page.html', ad_items=ad_items,
                            date=date, image_urls=image_urls, owner=owner,
                            comment_form=comment_form)


@blueprint.route('/new_ad')  # Добавить новое объявление
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
        save_new_ad(form, current_user.id)
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
    title   = 'Мои объявления'
    ad_list = Products.query.filter_by(created_by=current_user.id)
    ad_list = ad_list.order_by(Products.date.desc())
    return render_template('/advert/products.html',
                            page_title=title,
                            products_list=ad_list)


@blueprint.route('/hide/<ad_id>')
def hide(ad_id):
    ad_to_hide = Products.query.get(ad_id)
    if ad_to_hide.created_by == current_user.id:
        ad_to_hide.status = 'hiden'
        db.session.add(ad_to_hide)
        db.session.commit()
        return redirect(url_for('advert.own_ads'))
    else:
        flash('Это не ваше объясвление')
        return redirect(url_for('index'))


@blueprint.route('/sold/<ad_id>')
def sold(ad_id):
    ad_to_close = Products.query.get(ad_id)
    if ad_to_close.created_by == current_user.id:
        ad_to_close.status = 'sold'
        db.session.add(ad_to_close)
        db.session.commit()
        return redirect(url_for('advert.own_ads'))
    else:
        flash('Это не ваше объясвление')
        return redirect(url_for('index'))


@blueprint.route('/edit/<ad_id>')
def edit(ad_id):
    ad_to_edit = Products.query.get(ad_id)
    if ad_to_edit.created_by == current_user.id:
        form                = NewAdForm()
        form.ad_id.data     = ad_id
        form.name.data      = ad_to_edit.name
        form.text.data      = ad_to_edit.text
        form.price.data     = ad_to_edit.price
        form.address.data   = ad_to_edit.address
        image_urls          = Images.query.filter_by(product_id=ad_id).all()
        image_urls          = [image_url.img_url for image_url in image_urls]
        title               = 'Редактирование'
        return render_template('advert/edit.html', ad_items=ad_to_edit,
                                image_urls=image_urls, page_title=title, form=form)
    else:
        flash('Это не ваше объясвление')
        return redirect(url_for('index'))


@blueprint.route('/edit_ad-process', methods=['GET', 'POST'])
def edit_ad_process():
    form = NewAdForm()
    if form.validate_on_submit():
        save_edit(form)
        ad_id = form.ad_id.data
        flash('Ваше объявление принято!')
        return redirect(url_for('advert.ad_page', prod_db_id=ad_id))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        flash('Где-то ошибка')
        return redirect(url_for('index'))
