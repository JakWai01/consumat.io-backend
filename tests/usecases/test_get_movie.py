from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.get_movie import get_movie
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
        'backdrop_path':
        '/dFYguAfeVt19qAbzJ5mArn7DEJw.jpg',
        'cast': [{
            'image_path': '/8iDSGu5l93N7benjf6b3AysBore.jpg',
            'job': 'Acting',
            'name': 'Albert Brooks',
            'role': 'Marlin (voice)'
        }, {
            'image_path': '/z8IEEid4z63CBlJtxrTKEfsW7NA.jpg',
            'job': 'Acting',
            'name': 'Ellen DeGeneres',
            'role': 'Dory (voice)'
        }, {
            'image_path': '/fe4mUSp0XotA6Ku4Bs69Q9o2lqU.jpg',
            'job': 'Acting',
            'name': 'Alexander Gould',
            'role': 'Nemo (voice)'
        }, {
            'image_path': '/nbv4rIpJnw0OvowBZgwEWVriH9V.jpg',
            'job': 'Acting',
            'name': 'Willem Dafoe',
            'role': 'Gill (voice)'
        }, {
            'image_path': '/813ffbpoaoaJRdoe1yrbivboWKp.jpg',
            'job': 'Acting',
            'name': 'Brad Garrett',
            'role': 'Bloat (voice)'
        }, {
            'image_path': '/cDcB8mKP1GiIeoM3Qe7GIucs0iv.jpg',
            'job': 'Acting',
            'name': 'Allison Janney',
            'role': 'Peach (voice)'
        }, {
            'image_path': '/nrXfqtXDDYzSFNLPQnfLkus4I7s.jpg',
            'job': 'Acting',
            'name': 'Austin Pendleton',
            'role': 'Gurgle (voice)'
        }, {
            'image_path': '/ihcP1Bbnj9QkC9tEoDA4IkmV2tX.jpg',
            'job': 'Acting',
            'name': 'Stephen Root',
            'role': 'Bubbles (voice)'
        }, {
            'image_path': '/x0LqiqXF53vLYX4O4Chpd1EWw8u.jpg',
            'job': 'Acting',
            'name': 'Vicki Lewis',
            'role': 'Deb / Flo (voice)'
        }, {
            'image_path': '/f1BoWC2JbCcfP1e5hKfGsxkHzVU.jpg',
            'job': 'Writing',
            'name': 'Joe Ranft',
            'role': 'Jacques (voice)'
        }, {
            'image_path': '/npXFjaFQzBNroCEPllGPTZ5IisA.jpg',
            'job': 'Acting',
            'name': 'Geoffrey Rush',
            'role': 'Nigel (voice)'
        }, {
            'image_path': '/gasNitCwepbqNcYBmDHpsCgZH0I.jpg',
            'job': 'Writing',
            'name': 'Andrew Stanton',
            'role': 'Crush (voice)'
        }, {
            'image_path': '/vTWYllD9V76rgv9XAbtkkjjeunG.jpg',
            'job': 'Acting',
            'name': 'Elizabeth Perkins',
            'role': 'Coral (voice)'
        }, {
            'image_path': '/grsKC7Yp8Sfx8fwJnEM59GG4ogX.jpg',
            'job': 'Acting',
            'name': 'Nicholas Bird',
            'role': 'Squirt (voice)'
        }, {
            'image_path': '/dJe3nTCIToebjj1WHFHP7LmZKyk.jpg',
            'job': 'Acting',
            'name': 'Bob Peterson',
            'role': 'Mr. Ray (voice)'
        }, {
            'image_path': '/7WClJFIZ7QDkTMgFi8Rl1XQp6wV.jpg',
            'job': 'Acting',
            'name': 'Barry Humphries',
            'role': 'Bruce (voice)'
        }, {
            'image_path': '/j8tbvkg0kyCZihbwrUNRxwhqXXe.jpg',
            'job': 'Acting',
            'name': 'Eric Bana',
            'role': 'Anchor (voice)'
        }, {
            'image_path': '/kuaIudFTIBahGAdCamThG13jPp7.jpg',
            'job': 'Acting',
            'name': 'Bruce Spence',
            'role': 'Chum (voice)'
        }, {
            'image_path': '/gvrRsTfx47KupgRwTKp0gqryHPe.jpg',
            'job': 'Acting',
            'name': 'Bill Hunter',
            'role': 'Dentist (voice)'
        }, {
            'image_path': None,
            'job': 'Acting',
            'name': 'LuLu Ebeling',
            'role': 'Darla (voice)'
        }, {
            'image_path': None,
            'job': 'Acting',
            'name': 'Jordan Ranft',
            'role': 'Tad (voice)'
        }, {
            'image_path': '/k4R1E1aXQ2hwjFUCu9Wnz0PU1H8.jpg',
            'job': 'Acting',
            'name': 'Erica Beck',
            'role': 'Pearl (voice)'
        }, {
            'image_path': '/87eGn2O4NCz6Q1MFCQUCWxF0N6x.jpg',
            'job': 'Acting',
            'name': 'Erik Per Sullivan',
            'role': 'Sheldon (voice)'
        }, {
            'image_path': '/oRtDEOuIO1yDhTz5dORBdxXuLMO.jpg',
            'job': 'Acting',
            'name': 'John Ratzenberger',
            'role': 'Fish School (voice)'
        }, {
            'image_path': '/jPOuOHzYV7VYC4Ozy3u4nvnDZxO.jpg',
            'job': 'Acting',
            'name': 'Jack Angel',
            'role': 'Additional Voices (voice)'
        }, {
            'image_path': '/4K1HF10EvDjdaIoDAnWqFZjnmvk.jpg',
            'job': 'Acting',
            'name': 'Mickie McGowan',
            'role': 'Additional Voices (voice)'
        }],
        'code':
        12,
        'directors': [{
            'image_path': '/gasNitCwepbqNcYBmDHpsCgZH0I.jpg',
            'name': 'Andrew Stanton'
        }],
        'favorite':
        None,
        'genres': [{
            'name': 'Animation'
        }, {
            'name': 'Family'
        }],
        'overview':
        'Nemo, an adventurous young clownfish, is unexpectedly taken from '
        "his Great Barrier Reef home to a dentist's office aquarium. It's "
        'up to his worrisome father Marlin and a friendly but forgetful '
        'fish Dory to bring Nemo home -- meeting vegetarian sharks, '
        'surfer dude turtles, hypnotic jellyfish, hungry seagulls, and '
        'more along the way.',
        'popularity':
        66.144,
        'poster_path':
        '/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg',
        'providers': [{
            'name': 'Disney Plus'
        }],
        'rating_average':
        7.8,
        'rating_count':
        15073,
        'rating_user':
        None,
        'release_date':
        '2003-05-30',
        'runtime':
        100,
        'status':
        'Released',
        'title':
        'Finding Nemo',
        'tmdb_url':
        'https://www.themoviedb.org/movie/12',
        'watch_status':
        None
    }

    assert dict == get_movie("07e2fd2df@07e2fd2df.com", tmdb, 12)
