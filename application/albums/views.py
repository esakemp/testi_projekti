from flask import render_template, request, url_for,redirect
from flask_login import login_required

from application import db, app
from application.albums.models import Album
from application.albums.forms import AlbumForm

@app.route("/albums/new")
def albums_form():
    return(render_template("albums/new.html", form = AlbumForm()))
