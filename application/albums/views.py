from application import app
from flask import render_template, request

@app.route("/albums/new")
def albums_form():
    return render_template(albums/new.html)

@app.route("/albums/", methods=["POST"])
def albums_create():
    print(request.form.get("name"))

    return "hello world!"