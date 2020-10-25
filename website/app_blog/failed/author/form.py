from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, ValidationError
from wtforms.fields.html5 import EmailField
from app_blog.author.model import UserRegister

class FormRegister(Form):
    """build Form by Model
    
    password2: confirm input
    """
    username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(6, 30)
    ])
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')