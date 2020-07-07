from learn_project.model import db

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index=True, default=datime.utcnow)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
    	allowed_tags = ['a', 'abbr', 'acronym', 'b',
    					'code', 'em', 'i', 'strong']
    	target.body_html = bleach.linkify(bleach.clean(
    					markdown(value, output_format='html'),
    					tags=allowed_tags, strip=True))
    db.event.listen(Comments.body, 'set', Comments.on_changed_body)


    def __repr__(self):
        return '<Comments {}>'.format(self.body)