import os

from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI
from consumatio.external.db.models import *
from consumatio.usecases.get_watch_time import get_watch_time
from tests.tmdb.tmdb_mock import TmdbMock
from tests.utils.setup_app import setup_app


def test_get_watch_time_movie():
    tmdb = setup_app()[0]

    assert 0 == get_watch_time(tmdb, "991b7852b@991b7852b.com", "Movie", db)


def test_get_watch_time_tv():
    tmdb = setup_app()[0]

    assert 0 == get_watch_time(tmdb, "991b7852b@991b7852b.com", "TV", db)
