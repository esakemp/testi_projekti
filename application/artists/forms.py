from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ArtistForm(FlaskForm):
    name = StringField("Artist name", [validators.Length(min=1)])
    owned = BooleanField("Owned")

    class Meta:
        csrf = False
