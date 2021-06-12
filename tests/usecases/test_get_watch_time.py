import os

from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI
from consumatio.external.db.models import *
from consumatio.usecases.get_watch_time import get_watch_time
from tests.tmdb.tmdb_mock import TmdbMock


def test_get_watch_time_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(tmdb_key, "mysecret", DEFAULT_DATABASE_URI, None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert 0 == get_watch_time(tmdb, "991b7852b@991b7852b.com", "Movie")


def test_get_watch_time_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(tmdb_key, "mysecret", DEFAULT_DATABASE_URI, None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert 0 == get_watch_time(tmdb, "991b7852b@991b7852b.com", "TV")
