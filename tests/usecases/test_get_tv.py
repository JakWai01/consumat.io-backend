from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.get_tv import get_tv
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
    tmdb = TmdbMock(tmdb_key, db)

    dict = {
        'backdrop_path':
        '/suopoADq0k8YZr4dQXcU6pToj6s.jpg',
        'cast': [{
            'image_path': '/86jeYFV40KctQMDQIWhJ5oviNGj.jpg',
            'job': 'Acting',
            'name': 'Emilia Clarke',
            'role': 'Daenerys Targaryen'
        }, {
            'image_path': '/xR2IBnBlUdyBe5hecaVdtRuQqUE.jpg',
            'job': 'Acting',
            'name': 'Lena Headey',
            'role': 'Cersei Lannister'
        }, {
            'image_path': '/1hUAKYvSi4vZSYvTnD2TlqF6VVx.jpg',
            'job': 'Acting',
            'name': 'Sophie Turner',
            'role': 'Sansa Stark'
        }, {
            'image_path': '/wWTG27LBVTuHhIZ96aJcrkHuy8Z.jpg',
            'job': 'Acting',
            'name': 'Kit Harington',
            'role': 'Jon Snow'
        }, {
            'image_path': '/lRsRgnksAhBRXwAB68MFjmTtLrk.jpg',
            'job': 'Acting',
            'name': 'Peter Dinklage',
            'role': 'Tyrion Lannister'
        }, {
            'image_path': '/dv1zRmSvSg8lDrxeM0SswYze6Z0.jpg',
            'job': 'Acting',
            'name': 'Nikolaj Coster-Waldau',
            'role': 'Jaime Lannister'
        }, {
            'image_path': '/zLTq39cdRjS43dEzb78c1p1QcbT.jpg',
            'job': 'Acting',
            'name': 'Maisie Williams',
            'role': 'Arya Stark'
        }, {
            'image_path': '/ljmFT9zYqh4k2bmEcNU6rxoE7fW.jpg',
            'job': 'Acting',
            'name': 'Liam Cunningham',
            'role': 'Davos Seaworth'
        }, {
            'image_path': '/eLcisM9qqCLWnf0iImHuSn08FOi.jpg',
            'job': 'Acting',
            'name': 'John Bradley',
            'role': 'Samwell Tarly'
        }, {
            'image_path': '/eeTnNiustUbShHU09EQ6LoOpzcg.jpg',
            'job': 'Acting',
            'name': 'Conleth Hill',
            'role': 'Varys'
        }, {
            'image_path': '/kmlv5i02n3zKryBr2W3kSeWVKTD.jpg',
            'job': 'Acting',
            'name': 'Gwendoline Christie',
            'role': 'Brienne of Tarth'
        }, {
            'image_path': '/atkSptvQU7XdRVGrL5hiymbXwhd.jpg',
            'job': 'Acting',
            'name': 'Jacob Anderson',
            'role': 'Grey Worm'
        }, {
            'image_path': '/yI5xxWITp2YjMgiwac72Nen60jq.jpg',
            'job': 'Acting',
            'name': 'Jerome Flynn',
            'role': 'Bronn'
        }, {
            'image_path': '/meEHyiCRXTTCiYQMzP4VEdvEuD0.jpg',
            'job': 'Acting',
            'name': 'Rory McCann',
            'role': 'Sandor Clegane'
        }, {
            'image_path': '/lnR0AMIwxQR6zUCOhp99GnMaRet.jpg',
            'job': 'Acting',
            'name': 'Joe Dempsie',
            'role': 'Gendry'
        }, {
            'image_path': '/b6hQvID3oXPXnyrrXs22MBv2lyN.jpg',
            'job': 'Acting',
            'name': 'Isaac Hempstead-Wright',
            'role': 'Bran Stark'
        }],
        'code':
        1399,
        'creators': [{
            'image_path': '/xvNN5huL0X8yJ7h3IZfGG4O2zBD.jpg',
            'name': 'David Benioff'
        }, {
            'image_path': '/2RMejaT793U9KRk2IEbFfteQntE.jpg',
            'name': 'D. B. Weiss'
        }],
        'favorite':
        None,
        'first_air_date':
        '2011-04-17',
        'genres': [{
            'name': 'Sci-Fi & Fantasy'
        }, {
            'name': 'Drama'
        }, {
            'name': 'Action & Adventure'
        }],
        'last_air_date':
        '2019-05-19',
        'number_of_episodes':
        73,
        'number_of_seasons':
        8,
        'overview':
        'Seven noble families fight for control of the mythical land of '
        'Westeros. Friction between the houses leads to full-scale war. '
        'All while a very ancient evil awakens in the farthest north. '
        'Amidst the war, a neglected military order of misfits, the '
        "Night's Watch, is all that stands between the realms of men and "
        'icy horrors beyond.',
        'popularity':
        485.212,
        'poster_path':
        '/u3bZgnGQ9T01sWNhyveQz0wH0Hl.jpg',
        'providers': [{
            'name': 'Sky Go'
        }, {
            'name': 'Sky Ticket'
        }],
        'rating_average':
        8.4,
        'rating_count':
        None,
        'rating_user':
        None,
        'runtime':
        60,
        'status':
        'Ended',
        'title':
        'Game of Thrones',
        'tmdb_url':
        'https://www.themoviedb.org/tv/1399',
        'watch_status':
        None
    }

    assert dict == get_tv("03344f636@03344f636.com", tmdb, 1399)