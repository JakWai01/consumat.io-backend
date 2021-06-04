from consumatio.external.db.db import Database
from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.set_favorite import set_favorite
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_set_favorite_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_favorite(tmdb, database, "83f4a921d36@83f4a921d36.com", "Movie", 12,
                 None, None, True)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Movie",
        User.external_id_content == "83f4a921d36@83f4a921d36.com",
        MediaData.media_id_content == 12).first()

    assert True == query.favorite_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "83f4a921d36@83f4a921d36.com").delete()

    db.session.commit()


def test_set_favorite_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_favorite(tmdb, database, "83f4a921d36@83f4a921d36.com", "TV", 1399,
                 None, None, True)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "TV",
        User.external_id_content == "83f4a921d36@83f4a921d36.com",
        MediaData.media_id_content == 1399).first()

    assert True == query.favorite_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "83f4a921d36@83f4a921d36.com").delete()

    db.session.commit()


def test_set_favorite_season():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_favorite(tmdb, database, "83f4a921d36@83f4a921d36.com", "Season", 1399,
                 1, None, True)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Season",
        User.external_id_content == "83f4a921d36@83f4a921d36.com",
        MediaData.tv_code == 1399).first()

    assert True == query.favorite_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "83f4a921d36@83f4a921d36.com").delete()

    db.session.commit()


def test_set_favorite_episode():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_favorite(tmdb, database, "83f4a921d36@83f4a921d36.com", "Episode",
                 1399, 1, 1, True)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Episode",
        User.external_id_content == "83f4a921d36@83f4a921d36.com",
        MediaData.tv_code == 1399).first()

    assert True == query.favorite_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "83f4a921d36@83f4a921d36.com").delete()

    db.session.commit()