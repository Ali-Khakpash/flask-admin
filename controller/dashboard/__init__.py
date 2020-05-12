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
from Form.EditForm import EditForm

dashboard = Blueprint("dashboard", __name__)



@dashboard.route('home', methods=['GET'])
def home():
    q = request.args.get('q')
    edit_form = EditForm()
    return render_template('dashboard/home.html', q=q, edit_form=edit_form)


@dashboard.route('test', methods=['GET'])
@login_required
def test():
    user = UserLoadApi()
    return make_response(user.email)
