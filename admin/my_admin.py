import requests
from flask import request, make_response, json, jsonify
from flask_admin import expose, BaseView
from flask_admin.contrib import sqla
from Form.MyForm import CustomForm
from Model.User import User, db


class MicroBlogModelView(sqla.ModelView):
    can_delete = False  # disable model deletion
    page_size = 50  # the number of entries to display on the list view
    column_exclude_list = ['password']
    form_excluded_columns = ['owner', 'group']  #To remove fields from the create and edit forms

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


class ProductView(sqla.ModelView):
    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
    # """
    #     Custom create view.
    # """
       form = CustomForm()
       return self.render('templates/crud/create.html' , form=form)


# class SignUp(BaseView):
#     @expose('/createUser', methods=('GET', 'POST'))
#     def index(self):
#        form = CustomForm()
#        form_fields = {
#            'username':form.username,
#            'password':form.password
#        }
#
#        if request.method == 'POST':
#           payload = {
#                "username": request.values.get('username'),
#                "password": request.values.get('password')
#           }
#
#           resp = call_post_api(payload,'users')
#           if (resp["stat_code"] == 200):
#               new_user = User(resp['user']['username'], resp['user']['password'])
#               db.session.add(new_user)
#               db.session.commit()
#           return make_response({'type':'resp'})
#        return self.render('templates/crud/create.html' , form=form_fields, submit='create account',
#                           action='/signup/createUser'
#                           )


class SignUp(BaseView ):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        form = CustomForm()
        form_fields = {
        'username':form.username,
        'password':form.password
        }
        if request.method == 'POST':
            payload = {
                "username": request.values.get('username'),
                "password": request.values.get('password')
            }
            resp = call_post_api(payload,'users')
            if (resp["stat_code"] == 200):
                new_user = User(resp['user']['username'], resp['user']['password'])
                db.session.add(new_user)
                db.session.commit()
        return self.render('templates/crud/create.html', form=form_fields, submit='create account',
                           action='/signup/'
                           )


class SignIn(BaseView):
     @expose('/', methods=('GET', 'POST'))
     def indecx(self):
         form = CustomForm()
         form_fields = {
             'username': form.username,
             'password': form.password
         }
         if request.method == 'POST':
             payload = {
                 "username": request.values.get('username'),
                 "password": request.values.get('password')
             }
             resp = call_post_api(payload, 'users/login')
             return make_response({'user':resp})
         return self.render('templates/crud/create.html', form=form_fields, submit='signin',
                            action='/signin/'
                            )




class MyView(BaseView):
    @expose('/')
    def index(self):
        return 'Hello World!'


def call_post_api(payload ,endpoint):
    api_url = 'http://127.0.0.1:5000/api/'
    r = requests.post(api_url+endpoint, json=payload)
    dics = json.loads(r.text)
    dics["stat_code"] = r.status_code
    return dics


