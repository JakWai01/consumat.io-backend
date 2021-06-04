from consumatio.external.db.db import Database
from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.set_watch_status import set_watch_status
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_set_watch_status_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_watch_status(database, "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
                     12, "Movie", "Finished")

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Movie", User.external_id_content ==
        "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
        MediaData.media_id_content == 12).first()

    assert "Finished" == query.watch_status_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(User.external_id_content ==
                      "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com").delete()

    db.session.commit()


def test_set_watch_status_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_watch_status(database, "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
                     1399, "TV", "Finished")

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "TV", User.external_id_content ==
        "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
        MediaData.media_id_content == 1399).first()

    assert "Finished" == query.watch_status_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(User.external_id_content ==
                      "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com").delete()

    db.session.commit()