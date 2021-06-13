from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import *
from sqlalchemy.sql import func
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


class User(db.Model):
    __tablename__ = 'user_data'
    user_id_content = db.Column(db.Integer, primary_key=True)
    external_id_content = db.Column(db.String(255), nullable=False)
    media_data = db.relationship('MediaData',
                                 backref=db.backref('user_data', lazy=True))
    language = db.Column(db.String(30), nullable=False, default="en-US")
    country = db.Column(db.String(30), nullable=False, default="US")

    def __init__(self, external_id: str):
        self.external_id_content = external_id


class MediaData(db.Model):
    __tablename__ = 'media_data'
    user_data_id_content = db.Column(db.Integer, primary_key=True)
    watch_status_content = db.Column(db.String(255), nullable=True)
    rating_content = db.Column(db.Integer, nullable=True)
    media_id_content = db.Column(db.Integer, nullable=False)
    media_type_content = db.Column(db.String(30), nullable=False)
    user_id_content_media_data = db.Column(
        db.Integer, db.ForeignKey('user_data.user_id_content'), nullable=False)
    number_of_watched_episodes = db.Column(db.Integer, nullable=True)
    favorite_content = db.Column(db.Boolean, unique=False, default=False)
    tv_code = db.Column(db.Integer, nullable=True)
    created_on = db.Column(db.DateTime(timezone=False), default=func.now())

    def __init__(self, watch_status: str, rating: float, media_id: int,
                 media_type: str, user_id: int,
                 number_of_watched_episodes: int, tv_code: int):
        self.watch_status_content = watch_status
        self.rating_content = rating
        self.media_id_content = media_id
        self.media_type_content = media_type
        self.user_id_content_media_data = user_id
        self.number_of_watched_episodes = number_of_watched_episodes
        self.tv_code = tv_code