from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, HiddenField, StringField
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

"""
    Этот класс:
    1. передаёт в шаблон всякие параметры и названия полей
    2. запоминает ввод пользователя и передаёт его в processing
"""


class NewAdForm(FlaskForm):
    name = StringField('Название объявления',
                       validators=[DataRequired()],
                       render_kw={"class": "form-control",
                                  "placeholder": "Гараж"})

    text = TextAreaField('Описание объявления',
                         render_kw={"class": "form-control",
                                    "placeholder": "Продам гараж",
                                    "rows": "3"})

    price = IntegerField('Цена',
                         render_kw={"class": "form-control",
                                    "placeholder": "101"})

    address = StringField('Место сделки',
                          render_kw={"class": "form-control",
                                     "placeholder": "г.Воронеж, ул.Ленина, д.42"})

    image = FileField('Фотографии')
    submit = SubmitField('Продолжить', render_kw={"class": "btn btn-primary"})
    ad_id = HiddenField('id объявления')
