""""""
from learn_project import create_app
from learn_project.parser import parse

app = create_app()
with app.app_context():
	parse()