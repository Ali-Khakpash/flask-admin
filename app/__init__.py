from flask import (Flask,
                   g,
                   session,
                   request,
                   )
from config import config
from flask_menu import Menu
from controller.menu import menu
from controller.dashboard import dashboard
from Services.User_Load_From_Api import UserLoadApi


Menu_Instance = Menu()

def handle_bad_request(e):
    return 'not found!', 404


def create_app(config_name):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        Menu_Instance.init_app(app)
        app.register_blueprint(menu, url_prefix='/')
        app.register_blueprint(dashboard, url_prefix='/')

        @app.before_request
        def before_request_func():
            g.ass = 'ass'

        app.register_error_handler(404, handle_bad_request)



    return app
