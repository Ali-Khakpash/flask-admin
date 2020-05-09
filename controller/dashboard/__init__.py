from flask import (redirect,
                   url_for,
                   flash,
                   Blueprint,
                   request,
                   make_response,
                   render_template,
                   session,
                   jsonify,
                   )

from functools import wraps
from Services.login_required import login_required
from Services.User_Load_From_Api import UserLoadApi


dashboard = Blueprint("dashboard", __name__)



@dashboard.route('home', methods=['GET'])
def home():
    return render_template('dashboard/home.html')


@dashboard.route('test', methods=['GET'])
@login_required
def test():
    user = UserLoadApi()
    return make_response(user.email)
