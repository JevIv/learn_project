from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from learn_project.model import db
from learn_project.user.forms import LoginForm, RegistrationForm, Email, EqualTo
from learn_project.user.model import Users

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@blueprint.route('/login-process', methods=['POST'])
def login_process():
    form = LoginForm()

    if form.validate_on_submit:
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
    return redirect(url_for('index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('registration.html', page_title=title, form=form)


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
