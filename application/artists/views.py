from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.artists.models import Artist
from application.artists.forms import ArtistForm

#list all albums
@app.route("/artists", methods=["GET"])
def artists_index():
    return render_template("artists/list.html", artists = Artist.query.all())

#shows form for adding albums
@app.route("/artists/new")
@login_required
def artists_form():
    return render_template("artists/new.html", form = ArtistForm())

#mark album as owned or not owned
@app.route("/artists/<artist_id>/", methods=["POST"])
@login_required
def artist_set_owned(artist_id):
    
    a = Artist.query.get(artist_id)

    if a.owned == True:
        a.owned = False
    else:
        a.owned = True    

    
    db.session().commit()   

    return redirect(url_for("artists_index")) 

#testing
#creates new album
@app.route("/artists/", methods=["POST"])
@login_required
def artists_create():
    form = ArtistForm(request.form)

    if not form.validate():
        return render_template("artists/new.html", form = form)

    a = Artist(form.name.data)
    a.owned = form.owned.data
    
    db.session().add(a)
    db.session().commit()

    return redirect(url_for("artists_index"))