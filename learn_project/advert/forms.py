from flask_wtf import FlaskForm
from learn_project.user.model import Users
from wtforms import FileField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class NewAdForm(FlaskForm):
    name = StringField('Название объявления',
                       validators=[DataRequired()],
                       render_kw={
                                  "class": "form-control",
                                  "placeholder": "Гараж"
                                  }
                       )
                       
    text = TextAreaField('Описание объявления',
                         render_kw={
                                  "class": "form-control",
                                  "placeholder": "Продам гараж",
                                  "rows": "3"
                                  }
                         )

    price = IntegerField('Цена',
                         render_kw={
                                    "class": "form-control",
                                    "placeholder": "101"
                                    }
                         )

    address = StringField('Место сделки',
                          render_kw={
                                     "class": "form-control",
                                     "placeholder": "г.Воронеж, ул.Ленина, д.42"
                                     }
                          )

    image = FileField('Фотографии')

    submit = SubmitField('Продолжить', render_kw={"class": "btn btn-primary"})

    #def validate_username(self, username):
    #    users_count = Users.query.filter_by(username=username.data).count()
    #    if users_count > 0:
    #        raise ValidationError('Пользователь с таким именем уже зарегистрирован')

    #def validate_email(self, email):
    #    users_count = Users.query.filter_by(email=email.data).count()
    #    if users_count > 0:
    #        raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')
