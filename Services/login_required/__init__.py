from flask import (session,
                   make_response,
                   request,
                   redirect,
                   url_for,
                   )

from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('access_token') is None:
            return redirect(url_for('menu.login'), 302, )
        else:
            return f(*args, **kwargs)

    return decorated_function
