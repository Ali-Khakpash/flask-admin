from flask_admin import expose
from flask_admin.contrib import sqla

class MicroBlogModelView(sqla.ModelView):
    can_delete = False  # disable model deletion
    page_size = 50  # the number of entries to display on the list view
    column_exclude_list = ['password', ]

    @expose('/gh')
    def index(self):
        self._template_args['name'] = 'foobar'
        self._template_args['code'] = '12345'
        #return self._template_args['name']  $used for passing variables to
        return 'fggf'


    def is_accessible(self):
        return True


    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return 'f'


    def is_visible(self):
        return True
