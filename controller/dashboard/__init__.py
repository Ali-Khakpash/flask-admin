import os
from flask import (redirect,
                   url_for,
                   flash,
                   Blueprint,
                   request,
                   make_response,
                   render_template,
                   session,
                   jsonify,
                   current_app,
                   )

from functools import wraps
from Services.login_required import login_required
from Services.REST_API_Client.rest import REST
from Services.User_Load_From_Api import UserLoadApi
from Form.EditForm import EditForm
from .. import menu
from .. import dashboard


@dashboard.route('home', methods=['GET'])
def home():
    q = request.args.get('q')
    edit_form = EditForm()
    return render_template('dashboard/home.html', q=q, edit_form=edit_form)


@dashboard.route('edit_profile', methods=['PUT'])
def edit_profile():
    token = UserLoadApi.get_token()
    if token is not False:
        payload = {
            "email": session.get("email"),
            "first_name": request.values.get('first_name'),
            "last_name": request.values.get('last_name'),
            "age": request.values.get('age'),
            "city": request.values.get('city'),
            "country": request.values.get('country'),
            "phone_number": request.values.get('phone_number'),
            "social_media_accounts": {
                "Skype": request.values.get('skype'),
                "Facebook": request.values.get('facebook'),
                "WhatsApp": request.values.get('whatsapp'),
                "Instagram": request.values.get('instagram')
            }
        }
        rest_client = REST()
        headers = {"Authorization": "Bearer " + token}
        res = rest_client.edit('edit_profile', payload, headers)
        if res.get('status_code') == 200:
            return jsonify(status_code=200)
    else:
        return jsonify(redirect_url=url_for('menu.login'), status_code=401)


@dashboard.route('upload_avatar', methods=['POST'])
def upload_avatar():
    file = request.files.get('file')
    sendfile = {"file": (file.filename, file, file.content_type)}
    rest_client = REST()
    token = UserLoadApi.get_token()
    if token is not False:
        headers = {"Authorization": "Bearer " + token}
        res = rest_client.upload_file('upload_avatar', sendfile, headers)
        return jsonify(res)
    else:
        return jsonify(redirect_url=url_for('menu.login'), status_code=401)


@dashboard.route('home_data', methods=['GET'])
def home_data():
    token = UserLoadApi.get_token()
    if token is not False:
        rest_client = REST()
        headers = {"Authorization": "Bearer " + token}
        res = rest_client.get('home', headers)
        if res.get('status_code') == 200:
            return jsonify(res)
        else:
            return jsonify(status_code=500)
    else:
        return jsonify(redirect_url=url_for('menu.login'), status_code=401)



@dashboard.route('test', methods=['GET'])
@login_required
def test():
    user = UserLoadApi()
    return make_response(user.email)
