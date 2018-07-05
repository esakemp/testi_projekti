from flask import Flask
app = Flask(__name__)

#database init
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///artists.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

#files from application folder
from application import views

#files from artists folder
from application.artists import models
from application.artists import views

#files from auth folder
from application.auth import models
from application.auth import views

#files from albums folder
from application.albums import models
from application.albums import views

#login functionality
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#create database if needed
db.create_all()
