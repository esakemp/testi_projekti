from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class AlbumForm(FlaskForm):
    name = StringField("Album name", [validators.Length(min=1)])
    owned = BooleanField("Owned")

    class Meta:
        csrf = False
