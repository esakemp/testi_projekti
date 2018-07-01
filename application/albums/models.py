from application import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Datetime, default=db.func.current_timestamp())
    date_modified = db.column(db.Datetime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    owned = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.owned = False
        