from db import db
from flask_login import UserMixin
from flask_authorize import RestrictionsMixin, AllowancesMixin
from flask_authorize import PermissionsMixin
from Model.role import Role
from Model.Group import Group
# from login_handle import login_manager
# from app import login_manager
from login_handle import login_manager


UserGroup = db.Table(
    'user_group', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
)

UserRole = db.Table(
    'user_role', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True,nullable = False)
    password = db.Column(db.String(120), nullable = False)
    # `roles` and `groups` are reserved words that *must* be defined
    # on the `User` model to use group- or role-based authorization.
    roles = db.relationship(
        'Role', secondary=UserRole, backref=db.backref('user_roles', lazy='dynamic')
    )

    groups = db.relationship('Group', secondary=UserGroup)

    def __init__(self, username, password):
        self.username = username
        self.password = password



# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)