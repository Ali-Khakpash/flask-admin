from flask import Blueprint, request, make_response, render_template
from flask_menu import register_menu
from Form.MyForm import CustomForm
from Services.REST_API_Client.rest import REST


menu = Blueprint("menu", __name__)


@menu.route('', methods=['GET'])
@register_menu(menu, '.account', 'Your account')
def index():
        return render_template('menu/index.html')


@menu.route('login', methods=['GET'])
@register_menu(menu, '.login', 'Sign in')
def login():
        return render_template('auth/signin.html')




@menu.route('register', methods=['GET'])
@register_menu(menu, '.register', 'Sign up')
def register():
        restClient = REST()
        form = CustomForm()
        form_fields = {
                'email': form.email,
                'password': form.password
        }
        if request.method == 'POST':
                payload = {
                        "email": request.values.get('email'),
                        "password": request.values.get('password')
                }

                res = restClient.register('signup', payload)
                if (res.get('status_code') == 200):
                        # return self.render('templates/auth/signin.html', res=res, form=form_fields, submit='signin', action='/signin/')
                        flash(res.get('message'))
                        return redirect(url_for('signin.indecx'), 302, )
                else:
                        return self.render('templates/auth/signup.html', res=res, form=form_fields,
                                           submit='create account', action='/signup/')

        return render_template('auth/signup.html', form=form_fields, submit='Create account', action='/signup/')





