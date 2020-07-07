from flask import Blueprint, render_template, flash, redirect, url_for
from learn_project.model import db, Products
from learn_project.user.model import Users
from learn_project.comments.forms import AddCommentForm

blueprint = Blueprint('comments', __name__, url_prefix='/ad_page/')


@blueprint.route("/comments/<prod_db_id>", methods=["GET", "POST"])
@login_required
def comment_post(product_id):
    product = Products.query.get_or_404(product_id)
    form = AddCommentForm()
    author = Users.query.get(username)

    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comments(body=form.body.data, 
                               product=product,
                               author=current_user._get_current_object())
            db.session.add(comment)
            db.session.commit()
            flash("Ваш коментарий был добавлен!")
            return redirect(url_for("ad_page.html", id=product.id))

    return render_template('ad_page.html', form=form, comments=comments,
                            product=product, author=author)
