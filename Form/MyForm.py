from flask_wtf import FlaskForm
from wtforms import StringField, Form
from wtforms.validators import DataRequired

class CustomForm(FlaskForm):
      ozil = StringField('ozil')
