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
    images_urls = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Products {} {}>'.format(self.id, self.name)
