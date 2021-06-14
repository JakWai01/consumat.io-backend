from consumatio.external.db.models import *
from consumatio.usecases.get_watch_count import get_watch_count
from tests.utils.setup_app import setup_app


def test_get_watch_count_movie():
    tmdb = setup_app()[0]

    assert 0 == get_watch_count(tmdb, "2ae41e464@2ae41e464.com", "Movie", db)


def test_get_watch_count_tv():
    tmdb = setup_app()[0]

    assert 0 == get_watch_count(tmdb, "2ae41e464@2ae41e464.com", "TV", db)


def test_get_watch_count_animation():
    tmdb = setup_app()[0]

    assert 0 == get_watch_count(tmdb, "2ae41e464@2ae41e464.com", "Animation",
                                db)
