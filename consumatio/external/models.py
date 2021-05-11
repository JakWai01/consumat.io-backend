from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Cache(db.Model):
    query_content = db.Column(db.Text(), primary_key=True)
    body_content = db.Column(db.Text())
    last_changed = db.Column(db.DateTime())

    def __init__(self, query: str, body: str):
        self.query_content = query
        self.body_content = body
        self.last_changed = datetime.date.today()