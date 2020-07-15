"""from flask import Blueprint, flash, redirect, render_template, url_for
from learn_project.search.forms import SearchForm


blueprint = Blueprint('search', __name__)


@blueprint.route('/search', methods=['GET', 'POST'])
def search():
	query = request.args.get('query')  
	        query = request.args.get('query')  
	        if query:
	            results = Products.query.filter(Products.name.contains(query) | Products.text.contains(query)).all()
	        else:
	            results = flash('По запросу ничего не найдено!')						 # возвращает стартовую страничку
	            return redirect('/')


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
	    							results=results)"""