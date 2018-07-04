from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField

class AlbumForm(FlaskForm):
    name = StringField("Album name", [validators.InputRequired()])
    owned = BooleanField("Album owned")
    rpm = IntegerField("Album RPM", [validators.Length(2), validators.NumberRange(min(33), max(78))])

    class Meta:
        crsf = False