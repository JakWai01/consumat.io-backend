from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.get_season import get_season
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_tv():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    dict = {
        'air_date':
        '2011-04-17',
        'code':
        3624,
        'favorite':
        None,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        None,
        'overview':
        'Trouble is brewing in the Seven Kingdoms of Westeros. For the '
        "driven inhabitants of this visionary world, control of Westeros' "
        'Iron Throne holds the lure of great power. But in a land where '
        'the seasons can last a lifetime, winter is coming...and beyond '
        'the Great Wall that protects them, an ancient evil has returned. '
        'In Season One, the story centers on three primary areas: the '
        'Stark and the Lannister families, whose designs on controlling '
        'the throne threaten a tenuous peace; the dragon princess '
        'Daenerys, heir to the former dynasty, who waits just over the '
        'Narrow Sea with her malevolent brother Viserys; and the Great '
        'Wall--a massive barrier of ice where a forgotten danger is '
        'stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }

    assert dict == get_season("42600ede0@42600ede0.com", tmdb, 1399, 1)
