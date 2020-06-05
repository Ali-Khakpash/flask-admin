from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    first_name = StringField(label='First Name', render_kw={'class': 'form-control', 'placeholder': 'Eg: John'})
    last_name = StringField(label='Lirst Name', render_kw={'class': 'form-control', 'placeholder': 'Eg: Doe'})
    age = StringField(label='Age', render_kw={'class': 'form-control', 'id':'age-form', 'placeholder': 'Enter your Age', 'type': 'number'})
    city = StringField(label='City', render_kw={'class': 'form-control', 'placeholder': 'Enter your location'})
    phone_number = StringField(label='Phone Number', render_kw={'class': 'form-control', 'id':'phone-number-form', 'placeholder': 'Enter your phone number', 'type': 'tel'})
    facebook = StringField(label='Facebook', render_kw={'class': 'form-control', 'id':'facebook-form', 'placeholder': 'facebook account'})
    instagram = StringField(label='Instagram', render_kw={'class': 'form-control', 'id':'instagram-form', 'placeholder': 'instagram account'})
    skype = StringField(label='Skype', render_kw={'class': 'form-control', 'id':'skype-form', 'placeholder': 'skype account'})
    whatsapp = StringField(label='WhatsApp', render_kw={'class': 'form-control', 'id':'whatsapp-form', 'placeholder': 'whatsapp account'})

