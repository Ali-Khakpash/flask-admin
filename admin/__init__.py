from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from Model.User import User, db
from Model.product import Product
from admin.my_admin import MicroBlogModelView, ProductView

myadmin = Admin(name='microblog' , template_mode='bootstrap3', static_url_path='templates/admin' )

# myadmin.add_view(MicroBlogModelView(User, db.session))
myadmin.add_view(ProductView(Product, db.session))




















