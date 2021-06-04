from consumatio.external.tmdb.tmdb import Tmdb
from consumatio.usecases.get_tv_seasons import get_tv_seasons
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_tv_seasons():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = Tmdb(tmdb_key, db)

    dict = [{
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
        'driven inhabitants of this visionary world, control of '
        "Westeros' Iron Throne holds the lure of great power. But in a "
        'land where the seasons can last a lifetime, winter is '
        'coming...and beyond the Great Wall that protects them, an '
        'ancient evil has returned. In Season One, the story centers on '
        'three primary areas: the Stark and the Lannister families, '
        'whose designs on controlling the throne threaten a tenuous '
        'peace; the dragon princess Daenerys, heir to the former '
        'dynasty, who waits just over the Narrow Sea with her malevolent '
        'brother Viserys; and the Great Wall--a massive barrier of ice '
        'where a forgotten danger is stirring.',
        'poster_path':
        '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg',
        'season_number':
        1,
        'title':
        'Season 1',
        'tv_code':
        1399
    }, {
        'air_date':
        '2012-04-01',
        'code':
        3625,
        'favorite':
        None,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        None,
        'overview':
        'The cold winds of winter are rising in Westeros...war is '
        'coming...and five kings continue their savage quest for control '
        'of the all-powerful Iron Throne. With winter fast approaching, '
        'the coveted Iron Throne is occupied by the cruel Joffrey, '
        'counseled by his conniving mother Cersei and uncle Tyrion. But '
        'the Lannister hold on the Throne is under assault on many '
        'fronts. Meanwhile, a new leader is rising among the wildings '
        'outside the Great Wall, adding new perils for Jon Snow and the '
        "order of the Night's Watch.",
        'poster_path':
        '/5tuhCkqPOT20XPwwi9NhFnC1g9R.jpg',
        'season_number':
        2,
        'title':
        'Season 2',
        'tv_code':
        1399
    }, {
        'air_date':
        '2013-03-31',
        'code':
        3626,
        'favorite':
        None,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        None,
        'overview':
        'Duplicity and treachery...nobility and honor...conquest and '
        'triumph...and, of course, dragons. In Season 3, family and '
        'loyalty are the overarching themes as many critical storylines '
        'from the first two seasons come to a brutal head. Meanwhile, '
        "the Lannisters maintain their hold on King's Landing, though "
        'stirrings in the North threaten to alter the balance of power; '
        'Robb Stark, King of the North, faces a major calamity as he '
        'tries to build on his victories; a massive army of wildlings '
        'led by Mance Rayder march for the Wall; and Daenerys '
        'Targaryen--reunited with her dragons--attempts to raise an army '
        'in her quest for the Iron Throne.',
        'poster_path':
        '/7d3vRgbmnrRQ39Qmzd66bQyY7Is.jpg',
        'season_number':
        3,
        'title':
        'Season 3',
        'tv_code':
        1399
    }, {
        'air_date':
        '2014-04-06',
        'code':
        3628,
        'favorite':
        None,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        None,
        'overview':
        'The War of the Five Kings is drawing to a close, but new '
        'intrigues and plots are in motion, and the surviving factions '
        'must contend with enemies not only outside their ranks, but '
        'within.',
        'poster_path':
        '/dniQ7zw3mbLJkd1U0gdFEh4b24O.jpg',
        'season_number':
        4,
        'title':
        'Season 4',
        'tv_code':
        1399
    }, {
        'air_date':
        '2015-04-12',
        'code':
        62090,
        'favorite':
        None,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        None,
        'overview':
        'The War of the Five Kings, once thought to be drawing to a '
        'close, is instead entering a new and more chaotic phase. '
        'Westeros is on the brink of collapse, and many are seizing what '
        'they can while the realm implodes, like a corpse making a feast '
        'for crows.',
        'poster_path':
        '/527sR9hNDcgVDKNUE3QYra95vP5.jpg',
        'season_number':
        5,
        'title':
        'Season 5',
        'tv_code':
        1399
    }, {
        'air_date':
        '2016-04-24',
        'code':
        71881,
        'favorite':
        None,
        'number_of_episodes':
        10,
        'number_of_watched_episodes':
        None,
        'overview':
        'Following the shocking developments at the conclusion of season '
        'five, survivors from all parts of Westeros and Essos regroup to '
        'press forward, inexorably, towards their uncertain individual '
        'fates. Familiar faces will forge new alliances to bolster their '
        'strategic chances at survival, while new characters will emerge '
        'to challenge the balance of power in the east, west, north and '
        'south.',
        'poster_path':
        '/zvYrzLMfPIenxoq2jFY4eExbRv8.jpg',
        'season_number':
        6,
        'title':
        'Season 6',
        'tv_code':
        1399
    }, {
        'air_date':
        '2017-07-16',
        'code':
        81266,
        'favorite':
        None,
        'number_of_episodes':
        7,
        'number_of_watched_episodes':
        None,
        'overview':
        'The long winter is here. And with it comes a convergence of '
        'armies and attitudes that have been brewing for years.',
        'poster_path':
        '/3dqzU3F3dZpAripEx9kRnijXbOj.jpg',
        'season_number':
        7,
        'title':
        'Season 7',
        'tv_code':
        1399
    }, {
        'air_date':
        '2019-04-14',
        'code':
        107971,
        'favorite':
        None,
        'number_of_episodes':
        6,
        'number_of_watched_episodes':
        None,
        'overview':
        'The Great War has come, the Wall has fallen and the Night '
        "King's army of the dead marches towards Westeros. The end is "
        'here, but who will take the Iron Throne?',
        'poster_path':
        '/39FHkTLnNMjMVXdIDwZN8SxYqD6.jpg',
        'season_number':
        8,
        'title':
        'Season 8',
        'tv_code':
        1399
    }]

    assert dict == get_tv_seasons("d41d8cd98@d41d8cd98.com", tmdb, 1399)
