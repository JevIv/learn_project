"""Опишем наш товар"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False)
    address = db.Column(db.String, nullable=False)
    ad_number = db.Column(db.String, unique=True, nullable=False)
    comments = db.relationship('Comments', backref='product', lazy='dynamic')

    def get_comments(self):
        return Comments.query.filter_by(product_id=products.id).order_by(Comments.date.desc())

    def __repr__(self):
        return '<Products {} {}>'.format(self.id, self.name)


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return '<Images {} {}>'.format(self.id, self.product_id)