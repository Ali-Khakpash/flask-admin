from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    first_name = StringField(label='First Name', render_kw={'class': 'form-control', 'placeholder': 'Eg: John'})
    last_name = StringField(label='Lirst Name', render_kw={'class': 'form-control', 'placeholder': 'Eg: Doe'})
    city = StringField(label='City', render_kw={'class': 'form-control', 'placeholder': 'Enter your location'})
    phone_number = StringField(label='Phone Number', render_kw={'class': 'form-control', 'placeholder': 'Enter your phone number', 'type': 'tel'})
    facebook = StringField(label='Facebook', render_kw={'class': 'form-control', 'placeholder': 'facebook account'})
    instagram = StringField(label='Instagram', render_kw={'class': 'form-control', 'placeholder': 'instagram account'})
    skype = StringField(label='Skype', render_kw={'class': 'form-control', 'placeholder': 'skype account'})
    whatsapp = StringField(label='WhatsApp', render_kw={'class': 'form-control', 'placeholder': 'whatsapp account'})

