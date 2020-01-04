from flask import Blueprint, render_template, request

signUp_routes = Blueprint("signUp_routes", __name__, template_folder='../')


@signUp_routes.route('', methods=['POST', 'GET'])
def sign_up():

    if request.method == 'POST':
       print()
    return render_template('templates/signing/signup.html')
