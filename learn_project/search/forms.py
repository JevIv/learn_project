from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
  search = StringField('Поиск', [DataRequired()], render_kw={"class": "form-control mr-sm-2"})
  submit = SubmitField('Поиск', render_kw={'class': 'btn btn-outline-success my-2 my-sm-0'})