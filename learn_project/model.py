"""Опишем наш товар"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    address = db.Column(db.String, nullable=False)
<<<<<<< HEAD
=======
    published = db.Column(db.String, nullable=False)
>>>>>>> c6eec89d4438f9f33831bc06a7b5c10eb8adf786
    ad_number = db.Column(db.String, unique=True, nullable=False)
    images_urls = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Products {} {}>'.format(self.id, self.name)
