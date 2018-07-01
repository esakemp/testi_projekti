from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

#files from albums folder
from application.albums import models
from application.albums import views

#files from auth folder
from application.auth import models

db.create_all()
