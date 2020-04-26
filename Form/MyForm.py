from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Form, IntegerField
from wtforms.validators import DataRequired

class CustomForm(FlaskForm):
      username = IntegerField(label='username')
      password = PasswordField(label='password')
      email = StringField(label='email')

      # submit =

      # def __init__(self, username, password):
      #       self.username = username
      #       self.password = password

      @staticmethod
      def multiplyNums(x, y):
            return x + y