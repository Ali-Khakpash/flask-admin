from flask import Blueprint, render_template, request, make_response, json, g, session
import requests
from flask_login import login_user, current_user, login_required

from Model.User import User, db

from flask_authorize.plugin import CURRENT_USER

auth_routes = Blueprint("Auth_routes", __name__, template_folder='../')


@auth_routes.route('signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        # payload = {'username': request.values.get('username'), 'password': request.values.get('password')}
        payload = {
            "username": request.values.get('username'),
            "password": request.values.get('password')
        }
        r = requests.post('http://127.0.0.1:5000/api/users', json=payload)
        dics = json.loads(r.text)
        # return make_response(dics['user']['username'])
        # return make_response({'stat_code': r.status_code})
        dics["stat_code"] = r.status_code

        if (dics["stat_code"] == 200):
            new_user = User(dics['user']['username'], dics['user']['password'])
            db.session.add(new_user)
            db.session.commit()
        # return make_response(dics)
    return render_template('templates/auth/signup.html')


@auth_routes.route('signin', methods=['POST', 'GET'])
def sign_in():
    # if request.method == 'POST':
    #    payload = {
    #      "username": request.values.get('username'),
    #      "password": request.values.get('password')
    #     }
    #    the_user = get_current_user(payload)
    #    session['user'] = the_user.username
    #    return make_response({'the_user':session.get('user')})
    if request.method == 'POST':
        user = User.query.filter_by(username='ali').first()
        if user is not None:
           login_user(user)
           return make_response({'user':user.username})
    return render_template('templates/auth/signin.html')


@auth_routes.route('test', methods=['GET'])
@login_required
def test_in():
    return make_response({'current_user': current_user.password})


def get_current_user(payload):
    r = requests.post('http://127.0.0.1:5000/api/users/login', json=payload)
    dics = json.loads(r.text)
    dics["stat_code"] = r.status_code

    if (dics["stat_code"] == 200):
        current_user = User(username=request.values.get('username'), password=request.values.get('password'))
        return current_user
    return 'ops User not Found'
