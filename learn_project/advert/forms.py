from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, StringField
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


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
