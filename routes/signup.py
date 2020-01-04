from flask import Blueprint, render_template, request, make_response, json
import requests
from Model.User import User, db

signUp_routes = Blueprint("signUp_routes", __name__, template_folder='../')


@signUp_routes.route('', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        # payload = {'username': request.values.get('username'), 'password': request.values.get('password')}
        payload = {
       "username" : request.values.get('username'),
       "password" : request.values.get('password')
        }
        r = requests.post('http://127.0.0.1:5000/api/users', json=payload)
        dics = json.loads(r.text)
        #return make_response(dics['user']['username'])
        #return make_response({'stat_code': r.status_code})
        dics["stat_code"] = r.status_code

        if(dics["stat_code"]==200):
            new_user = User(dics['user']['username'], dics['user']['password'])
            db.session.add(new_user)
            db.session.commit()
        #return make_response(dics)
    return render_template('templates/signing/signup.html')
