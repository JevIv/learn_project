from learn_project.model import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime,
                          nullable=False,
                          default=datetime.now())
    product = relationship('Products',
                          backref='comments')
    users = relationship('Users',
                          backref='comments')
    user_id = db.Column(db.Integer,
                          db.ForeignKey('users.id', ondelete='CASCADE'),
                          index=True)
    product_id = db.Column(db.Integer,
                          db.ForeignKey('products.id', ondelete='CASCADE'),
                          index=True)

    def __repr__(self):
        return '<Comments {}>'.format(self.body)
