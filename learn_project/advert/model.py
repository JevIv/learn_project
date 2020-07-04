from learn_project.model import db
from datetime import datetime as dt
import uuid


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False)
    address = db.Column(db.String, nullable=False)
    ad_number = db.Column(db.String, unique=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Products {} {}>'.format(self.id, self.name)

    def default_date():
        return dt.now()

    def generate_ad_number():
        return uuid.uuid4().time_low


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return '<Images {} {}>'.format(self.id, self.product_id)
