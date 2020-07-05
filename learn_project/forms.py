from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import SubmitField, StringField

class AddCommentForm(FlaskForm):
    body = StringField("Body", validators=[InputRequired()])
    submit = SubmitField("Post")