from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.get_episode import get_episode
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_movie():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    dict = {
        'air_date':
        '2011-04-17',
        'code':
        63056,
        'episode_number':
        1,
        'favorite':
        None,
        'overview':
        'Jon Arryn, the Hand of the King, is dead. King Robert Baratheon '
        "plans to ask his oldest friend, Eddard Stark, to take Jon's "
        'place. Across the sea, Viserys Targaryen plans to wed his sister '
        'to a nomadic warlord in exchange for an army.',
        'rating_average':
        7.661,
        'season_number':
        1,
        'still_path':
        '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'title':
        'Winter Is Coming'
    }

    assert dict == get_episode("63af3075f@63af3075f.com", tmdb, 1399, 1, 1)
