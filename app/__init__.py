from flask import Flask
from flask_session import Session
from config import config
from Model.User import db
from admin import myadmin
from routes.Authentication import auth_routes, sign_in
from flask_authorize import Authorize

sess = Session()
authorize = Authorize()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
        sess.init_app(app)
        #authorize.init_app(app)
        myadmin.init_app(app)
        app.register_blueprint(auth_routes, url_prefix='/auth')
        db.create_all()

    return app
