from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cache(db.Model):
    query = db.Column(db.String(255), primary_key=True)
    body = db.Column(db.String(255))
    last_changed = db.Column(db.DateTime())
