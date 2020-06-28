from getpass import getpass
from learn_project import create_app
from learn_project.model import db, Users
import sys

app = create_app()
with app.app_context():
    username = input('Введите имя:')

    if Users.query.filter(Users.username == username).count():
        print('такой пользователь уже существует')
        sys.exit(0)

    password_1 = getpass('Введите пароль')
    password_2 = getpass('Подтверждение пароля')
    if not password_1 == password_2:
        print('пароли не совпадают')
        sys.exit(0)

    new_user = Users(username=username, role = 'admin')
    new_user.set_password(password_1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Пользователь создан. ID = {new_user.id}')
