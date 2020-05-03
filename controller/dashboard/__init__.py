from flask import redirect, url_for, flash, Blueprint, request, make_response, render_template


dashboard = Blueprint("dashboard", __name__)


@dashboard.route('home', methods=['GET'])
def home():
    return render_template('dashboard/home.html')