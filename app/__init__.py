from flask import Flask
from config import config
from Model.User import db
from admin.my_admin import myadmin

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        myadmin.init_app(app)

    return app
