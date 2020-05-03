from flask import Flask, g, session, request
from config import config
from Model.User import db, User
from flask_authorize import Authorize
from login_handle import login_manager
from flask_login import current_user
from flask_menu import Menu
from controller.menu import menu
from controller.dashboard import dashboard
# from authorize import authorize

authorize = Authorize()
Menu_Instance = Menu()

def imp():
    fgfg = 'dff'
    return fgfg

def create_app(config_name):
    app = Flask(__name__, template_folder="../templates", static_folder="../static",)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
        Menu_Instance.init_app(app)
        login_manager.init_app(app)
        authorize.init_app(app)
        db.create_all()
        app.register_blueprint(menu, url_prefix='/')
        app.register_blueprint(dashboard, url_prefix='/')
        @app.before_request
        def before_request_func():
            g.ass = 'ass'

        @login_manager.user_loader
        def load_user(id):
            return User.query.filter_by(id=id).first()

        # @authorize.has_role('reader')
        # def test_role():
        #     user = User.query.filter_by(username='c').first()
        #     # return render_template('templates/auth/test_role.html', user=user)
        #     return user

    return app
