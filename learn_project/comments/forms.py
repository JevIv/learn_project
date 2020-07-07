from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField

class AddCommentForm(FlaskForm):
    body = StringField("", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Добавить коментарий!', render_kw={"class": "btn btn-primary"})