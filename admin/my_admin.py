from flask_admin import Admin
from flask import current_app
from flask import Blueprint


myadmin = Admin(name='microblog', template_mode='bootstrap3')

