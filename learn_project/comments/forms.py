from flask_wtf import FlaskForm
from learn_project.advert.model import Products
from wtforms.validators import DataRequired, ValidationError
from wtforms import SubmitField, StringField, HiddenField

class CommentForm(FlaskForm):
    product_id = HiddenField('ID Товара', validators=[DataRequired()])
    comment_text = StringField('Добавить коментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_product_id(self,product_id):
        if not Products.query.get(product_id.data):
            raise ValidationError('Вы пытаетесь прокомментировать товар с несуществующим id')
