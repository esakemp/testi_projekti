from flask import render_template, request, url_for,redirect
from flask_login import login_required

from application import db, app
from application.albums.models import Album
from application.albums.forms import AlbumForm

@app.route("/albums", methods=["GET"])
def albums_index():
    return brender_template("albums/list.html", albums = Album.query.all())

@app.route("/albums/new")
def albums_form():
    return render_template("albums/new.html", form = AlbumForm())

@app.route("/albums/<album_id>/", methods=["POST"])
def albums_set_owned(album_id):

    album = Album.query.get(album_id)

    if album.owned == False:
        album.owned = True
    else:
        album.owned = False

    db.session().commit()

    return redirect(url_for("albums_index"))

@app.route("/albums/", methods=["POST"])
def albums_create():

    form = AlbumForm(request.form)

    if not form.validate():
        return render_template("albums/new.html", form = form)

    album = Album(form.name.data)
    album.owned = form.owned.data

    db.session().add(album)
    db.session().commit()

    return redirect(url_for("albums_index"))
