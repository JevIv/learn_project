from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from learn_project.user.forms import LoginForm
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
