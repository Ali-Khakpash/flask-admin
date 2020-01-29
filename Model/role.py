from db import db
from flask_authorize import RestrictionsMixin, AllowancesMixin
from flask_authorize import PermissionsMixin


class Role(AllowancesMixin, db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

