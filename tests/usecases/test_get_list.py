from consumatio.external.tmdb.tmdb import Tmdb
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
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", None, None)


def test_get_list_movie_watch_status():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", "Finished",
                          None)


def test_get_list_movie_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", None, True)


def test_get_list_movie_watch_status_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", "Finished",
                          True)


def test_get_list_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", None, None)


def test_get_list_tv_watch_status():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", "Finished",
                          None)


def test_get_list_tv_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", None, True)


def test_get_list_tv_watch_status_favorite():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", "Finished",
                          True)
