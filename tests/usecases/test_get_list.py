import os

from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI
from consumatio.external.db.models import *
from consumatio.usecases.get_list import get_list
from consumatio.usecases.set_watch_status import set_watch_status
from tests.tmdb.tmdb_mock import TmdbMock
from tests.utils.setup_app import setup_app


def test_get_list_movie():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", None, None)


def test_get_list_movie_watch_status():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", "Finished",
                          None)


def test_get_list_movie_favorite():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", None, True)


def test_get_list_movie_watch_status_favorite():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "Movie", "Finished",
                          True)


def test_get_list_tv():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", None, None)


def test_get_list_tv_watch_status():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", "Finished",
                          None)


def test_get_list_tv_favorite():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", None, True)


def test_get_list_tv_watch_status_favorite():
    tmdb = setup_app()[0]

    assert [] == get_list(tmdb, "c44298fc1@c44298fc1.com", "TV", "Finished",
                          True)
