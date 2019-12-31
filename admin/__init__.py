from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from Model.User import User, db
from admin.my_admin import MicroBlogModelView

myadmin = Admin(name='microblog', template_mode='bootstrap3')

myadmin.add_view(MicroBlogModelView(User, db.session))



































