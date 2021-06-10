from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.set_watch_status import set_watch_status
from consumatio.usecases.get_list import get_list
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_list_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", None, None,
                          db)


def test_get_list_movie_watch_status():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", "Finished",
                          None, db)


def test_get_list_movie_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", None, True,
                          db)


def test_get_list_movie_watch_status_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", "Finished",
                          True, db)


def test_get_list_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", None, None,
                          db)


def test_get_list_tv_watch_status():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", "Finished",
                          None, db)


def test_get_list_tv_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", None, True,
                          db)


def test_get_list_tv_watch_status_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", "Finished",
                          True, db)
