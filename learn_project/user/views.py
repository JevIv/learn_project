from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from learn_project.model import db
from learn_project.user.forms import AdminForm, LoginForm, RegistrationForm
from learn_project.user.model import Users
from learn_project.utils import get_redirect_target, run_parser

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/admin')
@login_required
def admin_index():
    title = 'Админка'
    admin_form = AdminForm()
    if current_user.is_admin:
        return render_template('user/admin_page.html', page_title=title, form=admin_form)
    else:
        flash('вы не админ')
        return redirect(url_for('index'))


@blueprint.route('/parse')
@login_required
def parse():
    if current_user.is_admin:
        run_parser()
        flash('Парсер запущен')
        return redirect(get_redirect_target())


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/login-process', methods=['POST'])
def login_process():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter(Users.username == form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('logged in')
            return redirect(url_for('index'))

        flash('wrong login or password')
        return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('bb gl hf')
    return redirect(url_for('user.login'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('user/registration.html', page_title=title, form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = Users(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))
        flash('Пожалуйста, исправьте ошибки в форме')
