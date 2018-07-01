from application import app, db
from flask import redirect, render_template, request, url_for

@app.route("/albums/new")
def albums_form():
    return render_template(albums/new.html)

@app.route("/albums/", methods=["POST"])
def albums_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("albums_index"))