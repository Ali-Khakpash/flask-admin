from flask_wtf import FlaskForm
from wtforms import StringField, Form
from wtforms.validators import DataRequired

class CustomForm(FlaskForm):
      username = StringField('username')
      password = StringField('password')

      # def __init__(self, username, password):
      #       self.username = username
      #       self.password = password

      @staticmethod
      def multiplyNums(x, y):
            return x + y