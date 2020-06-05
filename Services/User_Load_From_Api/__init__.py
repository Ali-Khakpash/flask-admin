from flask import (session,
                   abort,
                   redirect,
                   url_for,
                   )


class UserLoadApi():
    @staticmethod
    def get_token():
        access_token = session.get("access_token")
        if access_token:
            return access_token
        else:
            # abort(401, description="Not Authorized")
            redirect(url_for('menu.login'))
            return False
