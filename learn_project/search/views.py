from flask import Blueprint, flash, redirect, render_template, request#, url_for
#from learn_project.search.forms import SearchForm
from learn_project.advert.model import Products


blueprint = Blueprint('search', __name__,url_prefix='/')


@blueprint.route('/search')
def search():  
    query = request.args.get('query')
#    results = []  
    if query:
        results = Products.query.filter(Products.name.contains(query) | Products.text.contains(query)).all()

    else:
        results = flash('По запросу ничего не найдено!')
    return render_template('search.html', page_title='Тут вам не авито!', results=results)


"""
	results = []
	form = SearchForm()
	search_item = form.search.data
	if request.method == 'POST' and form.validate_on_submit():
		if search_item == '':
			qry = db_session.query(Products)
			results = qry.all()
		if not results:
			flash('По запросу ничего не найдено!')
			return redirect('/')
		else:
			return render_template('navbar.html', 
	    							form=form,
	    							results=results)
"""