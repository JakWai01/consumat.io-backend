import os

from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI
from consumatio.external.db.db import Database
from consumatio.external.db.models import *
from consumatio.usecases.set_number_of_watched_episodes import \
    set_number_of_watched_episodes
from tests.tmdb.tmdb_mock import TmdbMock
from tests.utils.setup_app import setup_app


def test_set_number_of_watched_episodes():
    tmdb, database, db = setup_app()

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
