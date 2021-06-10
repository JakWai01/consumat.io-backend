from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.get_season_episodes import get_season_episodes
import os
from consumatio.external.db.models import *
from consumatio.app import App


def test_get_season_episodes():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()

    app.app.app_context().push()
    tmdb = TmdbMock(tmdb_key, db)

    list = [{
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }, {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.661,
        'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg',
        'favorite': False
    }]

    assert list == get_season_episodes("8996fb924@8996fb924.com", tmdb, 1399,
                                       1, db)
