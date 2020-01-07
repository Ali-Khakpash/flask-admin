from flask import Flask, g, session, request
from config import config
from Model.User import db, User
from admin import myadmin
from routes.Authentication import auth_routes, sign_in
from flask_authorize import Authorize
from login_handle import login_manager
from flask_login import current_user

authorize = Authorize(current_user = current_user)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
        login_manager.init_app(app)
        authorize.init_app(app)
        myadmin.init_app(app)
        app.register_blueprint(auth_routes, url_prefix='/auth')
        db.create_all()
        @app.before_request
        def before_request_func():
            g.ass = 'ass'

        @login_manager.user_loader
        def load_user(id):
            return User.query.filter_by(id=id).first()

    return app
