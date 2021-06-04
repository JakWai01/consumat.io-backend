from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.get_watch_count import get_watch_count
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_watch_count_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert 0 == get_watch_count(tmdb, "2ae41e464@2ae41e464.com", "Movie")


def test_get_watch_count_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert 0 == get_watch_count(tmdb, "2ae41e464@2ae41e464.com", "TV")


def test_get_watch_count_animation():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert 0 == get_watch_count(tmdb, "2ae41e464@2ae41e464.com", "Animation")