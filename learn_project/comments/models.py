from learn_project.model import db
from sqlalchemy.orm import relationship

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, 
                          nullable=False,
                          default=datetime.now())
    author_id = db.Column(db.Integer, 
                          db.ForeignKey('user.id', onedelete='CASCADE'),
                          index=True)
    product_id = db.Column(db.Integer,
                          db.ForeignKey('product.id', onedelete='CASCADE'),
                          index=True)
    product = relationship('Products',backref='comments')
    author = relationship('Users',backref='comments')

    def comments_count(self):
        return Comment.query.filter(Comment.product_id == self.id).count()

    def __repr__(self):
        return '<Comments {}>'.format(self.body)