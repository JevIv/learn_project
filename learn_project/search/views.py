from flask import Blueprint, flash, render_template, request
from learn_project.advert.model import Products


blueprint = Blueprint('search', __name__, url_prefix='/')


@blueprint.route('/search')
def search():
    query = request.args.get('query')
    if query:
        results = Products.query.filter(Products.name.contains(query) | Products.text.contains(query)).all()
        for result in results:
            results_id    = result.query.get(result.id)
        if not results:
            results = flash('По запросу ничего не найдено!')
    else:
        results = flash('По запросу ничего не найдено!')
    return render_template('search.html', page_title='Тут вам не авито!', results=results, results_id=results_id)
