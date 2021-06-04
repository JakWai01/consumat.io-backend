from consumatio.external.db.db import Database
from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.set_rating import set_rating
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_set_rating_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    database = Database(db)
    app.app.app_context().push()

    set_rating(database, "d8007d620@d8007d620.com", "Movie", 12, 10)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Movie",
        User.external_id_content == "d8007d620@d8007d620.com",
        MediaData.media_id_content == 12).first()

    assert 10 == query.rating_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "d8007d620@d8007d620.com").delete()

    db.session.commit()


def test_set_rating_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    database = Database(db)
    app.app.app_context().push()

    set_rating(database, "d8007d620@d8007d620.com", "TV", 1399, 10)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "TV",
        User.external_id_content == "d8007d620@d8007d620.com",
        MediaData.media_id_content == 1399).first()

    assert 10 == query.rating_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "d8007d620@d8007d620.com").delete()

    db.session.commit()