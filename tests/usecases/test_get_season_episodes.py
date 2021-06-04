from consumatio.external.tmdb.tmdb import Tmdb
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
    tmdb = Tmdb(tmdb_key, db)

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
        'favorite': None
    }, {
        'code': 63057,
        'title': 'The Kingsroad',
        'episode_number': 2,
        'season_number': 1,
        'overview':
        'While Bran recovers from his fall, Ned takes only his daughters to Kings Landing. Jon Snow goes with his uncle Benjen to The Wall. Tyrion joins them.',
        'air_date': '2011-04-24',
        'rating_average': 7.58,
        'still_path': '/icjOgl5F9DhysOEo6Six2Qfwcu2.jpg',
        'favorite': None
    }, {
        'code': 63058,
        'title': 'Lord Snow',
        'episode_number': 3,
        'season_number': 1,
        'overview':
        "Lord Stark and his daughters arrive at King's Landing to discover the intrigues of the king's realm.",
        'air_date': '2011-05-01',
        'rating_average': 7.925,
        'still_path': '/4vCYVtIhiYSUry1lviA7CKPUB5Z.jpg',
        'favorite': None
    }, {
        'code': 63059,
        'title': 'Cripples, Bastards, and Broken Things',
        'episode_number': 4,
        'season_number': 1,
        'overview':
        "Eddard investigates Jon Arryn's murder. Jon befriends Samwell Tarly, a coward who has come to join the Night's Watch.",
        'air_date': '2011-05-08',
        'rating_average': 8.045,
        'still_path': '/Ai2UPMWv38xGjOgNBuA1o8w8dUI.jpg',
        'favorite': None
    }, {
        'code': 63060,
        'title': 'The Wolf and the Lion',
        'episode_number': 5,
        'season_number': 1,
        'overview':
        'Catelyn has captured Tyrion and plans to bring him to her sister, Lysa Arryn, at The Vale, to be tried for his, supposed, crimes against Bran. Robert plans to have Daenerys killed, but Eddard refuses to be a part of it and quits.',
        'air_date': '2011-05-15',
        'rating_average': 8.5,
        'still_path': '/fGFhmR6ocxhsgU3J6pXpygxaitc.jpg',
        'favorite': None
    }, {
        'code': 63061,
        'title': 'A Golden Crown',
        'episode_number': 6,
        'season_number': 1,
        'overview':
        'While recovering from his battle with Jamie, Eddard is forced to run the kingdom while Robert goes hunting. Tyrion demands a trial by combat for his freedom. Viserys is losing his patience with Drogo.',
        'air_date': '2011-05-22',
        'rating_average': 8.272,
        'still_path': '/6FcfWGFlDyWZ2JvQi8uvkxbDx1z.jpg',
        'favorite': None
    }, {
        'code': 63062,
        'title': 'You Win or You Die',
        'episode_number': 7,
        'season_number': 1,
        'overview':
        "Robert has been injured while hunting and is dying. Jon and the others finally take their vows to the Night's Watch. A man, sent by Robert, is captured for trying to poison Daenerys. Furious, Drogo vows to attack the Seven Kingdoms.",
        'air_date': '2011-05-29',
        'rating_average': 8.478,
        'still_path': '/5ZNrAvoNAG9scYHgxLVyozypOmV.jpg',
        'favorite': None
    }, {
        'code': 63063,
        'title': 'The Pointy End',
        'episode_number': 8,
        'season_number': 1,
        'overview':
        'Eddard and his men are betrayed and captured by the Lannisters. When word reaches Robb, he plans to go to war to rescue them. The White Walkers attack The Wall. Tyrion returns to his father with some new friends.',
        'air_date': '2011-06-05',
        'rating_average': 8.1,
        'still_path': '/imjEc0gD9djHOlsJX00l08TaaGp.jpg',
        'favorite': None
    }, {
        'code': 63064,
        'title': 'Baelor',
        'episode_number': 9,
        'season_number': 1,
        'overview':
        "Robb goes to war against the Lannisters. Jon finds himself struggling on deciding if his place is with Robb or the Night's Watch. Drogo has fallen ill from a fresh battle wound. Daenerys is desperate to save him.",
        'air_date': '2011-06-12',
        'rating_average': 8.813,
        'still_path': '/3pcFXQOKHnZhRkGCQ7Y8HRB1v8V.jpg',
        'favorite': None
    }, {
        'code': 63065,
        'title': 'Fire and Blood',
        'episode_number': 10,
        'season_number': 1,
        'overview':
        "With Ned dead, Robb vows to get revenge on the Lannisters. Jon must officially decide if his place is with Robb or the Night's Watch. Daenerys says her final goodbye to Drogo.",
        'air_date': '2011-06-19',
        'rating_average': 8.626,
        'still_path': '/7GhSiFhXOg81AevNQWrX6DOEL1U.jpg',
        'favorite': None
    }]

    assert list == get_season_episodes("8996fb924@8996fb924.com", tmdb, 1399,
                                       1)
