import login
import requests
from flask import request, make_response, json, jsonify
from flask_admin import expose, BaseView
from flask_admin.contrib import sqla
from Form.MyForm import CustomForm
from Model.User import User, db
from flask_login import login_user, current_user, login_required
from Services.REST_API_Client.rest import REST


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


class ProductView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    def create_view(self):
        return self.render('templates/crud/createtemplate.html')

    @expose('/new', methods=('GET', 'POST'))
    def new_view(self):
        return self.render('templates/crud/new.html')

    #create_template = 'crud/createtemplate.html'

    # def is_visible(self):
    #       return True
    # def is_accessible(self):
    #       return login.current_user.is_authenticated

    pass



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

    # def is_accessible(self):
    #     if(login.current_user.is_authenticated):
    #        return False

    @expose('/', methods=('GET', 'POST'))
    def index(self):
        restClient = REST()
        form = CustomForm()
        form_fields = {
        'username':form.username,
        'password':form.password,
        'email':form.email
        }
        if request.method == 'POST':
            payload = {
                "username": request.values.get('username'),
                "password": request.values.get('password'),
                "email":    request.values.get('email')
            }
            #resp = call_post_api(payload,'signup')
            #print(resp)
            res = restClient.register('signup', payload)
            return self.render('templates/crud/create.html', res=res, form=form_fields, submit='create account', action='/signup/')
            #return make_response(res)
            # if (resp["stat_code"] == 200):
            #     new_user = User(resp['user']['username'], resp['user']['password'])
            #     db.session.add(new_user)
            #     db.session.commit()
        return self.render('templates/crud/create.html', form=form_fields, submit='create account',action='/signup/')


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

             if(resp['stat_code']):
                 user = User.query.filter_by(username=payload['username']).first()
                 if user is not None:
                     login_user(user)
                     return make_response({'user': current_user.username})

             return make_response({'status':resp['stat_code']})
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
    #dics = json.loads(r.text)
    #dics["stat_code"] = r.status_code
    return r.status_code


