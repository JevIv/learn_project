from flask import Blueprint, flash, redirect, render_template, url_for
from learn_project.search.forms import SearchForm


blueprint = Blueprint('search', __name__)



@blueprint.route('/search', methods=['GET', 'POST'])
def search():
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
	    	return render_template('base.html', 
	    							form=form,
	    							results=results)