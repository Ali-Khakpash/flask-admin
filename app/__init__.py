from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
# from Models.authors import db,ma
from Model.User import db

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()  # creats all table from model class

    return app
    # attach routes and custom error pages here