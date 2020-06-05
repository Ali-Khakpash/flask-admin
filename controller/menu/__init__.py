from flask import (redirect,
                   url_for,
                   flash,
                   Blueprint,
                   request,
                   make_response,
                   render_template,
                   session,
                   )
from flask_menu import register_menu
from .. import dashboard
from Form.MyForm import CustomForm
from Services.REST_API_Client.rest import REST
from flask_login import login_user
from Services.User_Load_From_Api import UserLoadApi
from .. import menu


@menu.route('', methods=['GET'])
@register_menu(menu, '.account', 'Your account')
def index():
    return render_template('menu/index.html')


@menu.route('login', methods=['GET', 'POST'])
@register_menu(menu, '.login', 'Sign in')
def login():
    rest_client = REST()
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

        res = rest_client.register('signin', payload)
        if res.get('status_code') == 200:
            session['access_token'] = res.get('access_token')
            session['email'] = res.get('currentUser')
            return redirect(url_for('dashboard.home'), 302, )
        else:
            return render_template('auth/signin.html', res=res, form=form_fields, submit='Login', action='login')

    return render_template('auth/signin.html', form=form_fields, submit='Login', action='login')


@menu.route('register', methods=['GET', 'POST'])
@register_menu(menu, '.register', 'Sign up')
def register():
    rest_client = REST()
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

        res = rest_client.register('signup', payload)
        if (res.get('status_code') == 200):
            flash(res.get('message'))
            return redirect(url_for('menu.login'), 302, )
        else:
            return render_template('auth/signup.html', res=res, form=form_fields, submit='create account',
                                   action='register')

    return render_template('auth/signup.html', form=form_fields, submit='Create account', action='register')
