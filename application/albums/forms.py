from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators

class AlbumForm(FlaskForm):
    name = StringField("Album name")
    owned = BooleanField("Album owned")
    rpm = IntegerField("Album RPM")

    class Meta:
        csrf = False