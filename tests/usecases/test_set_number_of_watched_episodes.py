from consumatio.external.db.db import Database
from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.set_number_of_watched_episodes import set_number_of_watched_episodes
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_set_number_of_watched_episodes():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    tmdb = Tmdb(tmdb_key, db)
    database = Database(db)
    app.app.app_context().push()

    set_number_of_watched_episodes(tmdb, database, "7af927da3e@7af927da3e.com",
                                   1399, 1, 4)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Season",
        User.external_id_content == "7af927da3e@7af927da3e.com",
        MediaData.tv_code == 1399).first()

    assert 4 == query.number_of_watched_episodes

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "83f4a921d36@83f4a921d36.com").delete()

    db.session.commit()