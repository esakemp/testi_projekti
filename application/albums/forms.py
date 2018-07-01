from flask_wtf import FlaskForm
from wtforms import StringField

class AlbumForm(FlaskForm):
    name = StringField("Album name")

    class Meta:
        csrf = False
