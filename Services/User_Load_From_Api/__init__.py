from flask import session


class UserLoadApi():
    def __init__(self):
        self.email = session.get("email")
        self.access_token = session.get("access_token")
