from flask import Flask
from config import config
from Model.User import db
from admin import myadmin
from routes.signup import signUp_routes

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        myadmin.init_app(app)
    app.register_blueprint(signUp_routes, url_prefix='/signup')

    return app
