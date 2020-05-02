from flask import Blueprint, request, make_response, render_template
from flask_menu import register_menu


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
        return render_template('auth/signup.html')




