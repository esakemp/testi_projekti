from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///artists.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

#files from albums folder
from application.artists import models
from application.artists import views

#files from auth folder
from application.auth import models
from application.auth import views

db.create_all()
