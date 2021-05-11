from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Cache(db.Model):
    query = db.Column(db.Text(), primary_key=True)
    body = db.Column(db.Text())
    last_changed = db.Column(db.DateTime())

    def __init__(self, query: str, body: str):
        self.query = query
        self.body = body
        self.last_changed = datetime.date.today()