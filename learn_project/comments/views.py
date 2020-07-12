from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from learn_project.model import db, Products
from learn_project.user.model import Users
from learn_project.comments.forms import CommentForm

blueprint = Blueprint('comments', __name__, url_prefix='/ad_page/')


@blueprint.route("<prod_db_id>/comments", methods=["POST"])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        if Products.query.filter(Products.id == form.product_id.data).first():
            comment = Comment(text=form.comment_text.data, product_id=form.product_id.data, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            flash('Комментарий успешно добавлен')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash('Ошибка в заполнении поля "{}": - {}'.format(
                        getattr(form, field).label.text,
                        error
                    ))
        return redirect(get_redirect_target())