from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.get_watch_time import get_watch_time
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_watch_time_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert 0 == get_watch_time(tmdb, "991b7852b@991b7852b.com", "Movie")


def test_get_watch_time_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    assert 0 == get_watch_time(tmdb, "991b7852b@991b7852b.com", "TV")
