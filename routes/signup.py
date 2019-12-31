from flask import Blueprint, render_template

signUp_routes = Blueprint("signUp_routes", __name__)

@signUp_routes.route('', methods=['POST','GET'], template_folder='../')
def sign_up():
    return render_template('templates/signin.html')