from db import db
from flask_authorize import RestrictionsMixin, AllowancesMixin
from flask_authorize import PermissionsMixin
from flask_sqlalchemy import SQLAlchemy

class Product(db.Model, PermissionsMixin):
    __tablename__ = 'products'
    __permissions__ = dict(
        owner=['read', 'update', 'delete', 'revoke'],
        group=['read', 'update'],
        other=['read']
    )

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(200))
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # def __init__(self, name, desc, user_id=None):
    #     self.name = name
    #     self.desc = desc
    #     self.user_id = user_id