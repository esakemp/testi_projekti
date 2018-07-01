from application import app, db
from flask import redirect, render_template, request, url_for
from application.albums.models import Album

#list all albums
@app.route("/albums", methods=["GET"])
def album_index():
    return render_template("albums/list.html", albums = Album.query.all())

#shows form for adding albums
@app.route("/albums/new")
def albums_form():
    return render_template("albums/new.html")

#creates new album
@app.route("/albums/", methods=["POST"])
def albums_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("albums_index"))