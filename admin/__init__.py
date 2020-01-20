from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from Model.User import User, db
from Model.product import Product
from admin.my_admin import MicroBlogModelView, ProductView, SignUp, MyView

myadmin = Admin(name='microblog' , template_mode='bootstrap3', index_view=
            AdminIndexView(
                    name='Home',
                    template='templates/admin/index.html',
                    url='/'
                )
            )

# myadmin.add_view(MicroBlogModelView(User, db.session))
myadmin.add_view(ProductView(Product, db.session))
myadmin.add_view(SignUp(User, db.session, name='SignUp', url='/signup'))
myadmin.add_view(MyView(name='My View', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))





















