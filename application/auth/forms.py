from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username", [validators.Length(min=6)])
    password = PasswordField("Password", [validators.Length(min=8)])

    class Meta:
        csrf = False        