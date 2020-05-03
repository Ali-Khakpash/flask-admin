from flask import redirect, url_for, flash, Blueprint, request, make_response, render_template
from flask_menu import register_menu
# from controller.dashboard import dashboard
from ..dashboard import dashboard
from Form.MyForm import CustomForm
from Services.REST_API_Client.rest import REST

menu = Blueprint("menu", __name__)


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
        if (res.get('status_code') == 200):
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
            return render_template('auth/signup.html', res=res, form=form_fields, submit='create account', action='register')

    return render_template('auth/signup.html', form=form_fields, submit='Create account', action='register')
