from flask import redirect, render_template, request, url_for

from application import app, db
from application.albums.models import Album
from application.albums.forms import AlbumForm

#list all albums
@app.route("/albums", methods=["GET"])
def albums_index():
    return render_template("albums/list.html", albums = Album.query.all())

#shows form for adding albums
@app.route("/albums/new")
def albums_form():
    return render_template("albums/new.html", form = AlbumForm())

#mark album as owned or not owned
@app.route("/albums/<album_id>/", methods=["POST"])
def albums_set_owned(album_id):
    
    a = Album.query.get(album_id)

    if a.owned == True:
        a.owned = False
    else:
        a.owned = True    

    #a.owned = True
    db.session().commit()   

    return redirect(url_for("albums_index")) 

#mark album as not owned
@app.route("/albums/<album_id>/", methods=["POST"])
def albums_set_not_owned(album_id):

    a = Album.query.get(album_id)
    a.owned = False
    db.Session().commit()

    return redirect(url_for("albums_index"))


#creates new album
@app.route("/albums/", methods=["POST"])
def albums_create():
    form = AlbumForm(request.form)

    if not form.validate():
        return render_template("albums/new.html", form = form)

    a = Album(form.name.data)
    a.owned = form.owned.data

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("albums_index"))