from consumatio.external.db.models import *
from consumatio.usecases.get_search import get_search
from tests.utils.setup_app import setup_app


def test_get_search():
    tmdb = setup_app()[0]

    dict = {
        'total_pages':
        66,
        'results': [{
            'code': 1769,
            'title': 'Johnny Test',
            'genres': None,
            'overview':
            "Young Johnny is gung-ho and full of courage. Johnny's brainiac twin sisters, Susan and Mary, use Johnny as their guinea pig for their outrageous scientific experiments. If they can dream it up, Johnny will do it; as long as his genetically engineered super dog, Dukey, can come along.",
            'popularity': 15.925,
            'rating_average': 5.6,
            'rating_count': 80,
            'first_air_date': '2005-09-17',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/ecxpOnYv7iTUVNUmZRoxRksaC1f.jpg',
            'poster_path': '/rn5YbXP4UunS0BLhmjqndHJYhp.jpg',
            'providers': None,
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1769',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
        }, {
            'code': 226979,
            'title': 'Test',
            'genres': None,
            'overview':
            'San Francisco, 1985. Two opposites attract at a modern dance company. Together, their courage and resilience are tested as they navigate a world full of risks and promise, against the backdrop of a disease no one seems to know anything about.',
            'popularity': 5.496,
            'rating_average': 6.6,
            'rating_count': 105,
            'release_date': '2013-06-29',
            'runtime': None,
            'status': None,
            'backdrop_path': '/xySCWwZVuU03xOsJfs1Qk8yG2DF.jpg',
            'poster_path': '/tTWRomgIMOoIB3CJLPlVbqSawEm.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/226979',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 401123,
            'title': 'Beta Test',
            'genres': None,
            'overview':
            "While testing the latest first person shooter from global game developer, Sentinel, video game champion Max Troy discovers the events happening within the game are being reflected in the real world. He soon determines that the game's protagonist is real-life Orson Creed, an ex-Sentinel employee who is being remotely controlled by the corporation for reasons unknown. As virtual and real worlds collide, Max and Creed must join forces to unravel the conspiracy before the game's sinister events escalate and overwhelm the city.",
            'popularity': 5.633,
            'rating_average': 5.3,
            'rating_count': 137,
            'release_date': '2016-07-22',
            'runtime': None,
            'status': None,
            'backdrop_path': '/rG2jdLdj4U55MgI3g9f85w2th1y.jpg',
            'poster_path': '/zKisJfMxpp0KfX4P3VyDrH0edg6.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/401123',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 71761,
            'title': 'Bäst i test',
            'genres': None,
            'overview': 'Swedish version of Taskmaster.',
            'popularity': 8.346,
            'rating_average': 5.8,
            'rating_count': 4,
            'first_air_date': '2017-03-10',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/gNzlviwUtStMOxNiLYmU0GDswV5.jpg',
            'poster_path': '/nnT18R49fIKFmmfaQqMXcBEaplK.jpg',
            'providers': None,
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/71761',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
        }, {
            'code': 43155,
            'title': 'Test Pilot',
            'genres': None,
            'overview':
            'Jim is a test pilot. His wife Ann and best friend Gunner try their best to keep him sober. But the life of a test pilot is anything but safe.',
            'popularity': 5.171,
            'rating_average': 6.5,
            'rating_count': 43,
            'release_date': '1938-04-16',
            'runtime': None,
            'status': None,
            'backdrop_path': '/qyM5OA9UfIlNWocQrI3BH7CZhxo.jpg',
            'poster_path': '/j3Xn5Zl9IGOHyEqNYU31eyiLTQE.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/43155',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 4591,
            'title': "America's Test Kitchen",
            'genres': None,
            'overview':
            "America's Test Kitchen is a half-hour cooking show distributed to public television stations in the United States, also airing in Canada. The show's host is Cook's Illustrated editor-in-chief Christopher Kimball; the show and the magazine are affiliated, and the magazine's test kitchen facility in Brookline, Massachusetts, is used as a set for the show.\n\nCook's Illustrated's parent company, Boston Common Press, renamed itself America's Test Kitchen in 2004.",
            'popularity': 7.658,
            'rating_average': 8,
            'rating_count': 6,
            'first_air_date': '2001-08-04',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/2UwBG0nStY7JhLQnP5LKVSGPNx4.jpg',
            'poster_path': '/eZjnMVcVgdSwJJB6aLfcqefxq0z.jpg',
            'providers': None,
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/4591',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
        }, {
            'code': 679548,
            'title': 'The Alpha Test',
            'genres': None,
            'overview':
            'A suburban family drives their new gadget, The Alpha Home Assistant, to a killing rampage after mistreating and abusing it, leading to a full A.I. uprising…',
            'popularity': 5.356,
            'rating_average': 7,
            'rating_count': 2,
            'release_date': '2021-02-04',
            'runtime': None,
            'status': None,
            'backdrop_path': '/6Hw9TxmY0PV93VB2CCQFFqqRFI4.jpg',
            'poster_path': '/ozbvCucRf3ZXUH5oQSdAayjLVdg.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/679548',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 67102,
            'title': "Pilot Pirx's Inquest",
            'genres': None,
            'overview':
            'This movie is about a rocket pilot named Pirx who is hired to go on a mission to evaluate some nonlinears (robots) for use as crewmembers on future space flights. Pirx and his crew, made up of nonlinears and humans, are sent out to launch two satellites into the rings of Saturn. Upon returning to Earth there is an inquest to determine if Pirx was responsible for the "accident." In the end, it is found that one of the robots caused the malfunction in an attempt to kill the human crewmembers and Pirx is cleared of all charges. In this tale Lem puts forth the idea that what is perceived a human weakness is in fact an advantage over a perfect machine. Pirx defeats the robot, because a human can hesitate, make wrong decisions, have doubts, but a robot cannot. A similar idea is present in Isaac Asimov\'s Robot Series, where putting a robot in a position where it cannot chose between the Three laws of robotics fries its positronic brain.',
            'popularity': 3.977,
            'rating_average': 5.8,
            'rating_count': 17,
            'release_date': '1979-05-27',
            'runtime': None,
            'status': None,
            'backdrop_path': '/xE3Y5ntcbqDz9FzwLWSVVR5qF7H.jpg',
            'poster_path': '/pqjWWjZlCGIW1dsdeLqS9mR0DbB.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/67102',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 456768,
            'title': 'Crash Test Aglaé',
            'genres': None,
            'overview':
            "Aglaé, a young factory worker, has only one focus in life: her job at a car crash test site. When she learns that the factory is going to be relocated abroad, she accepts, to everyone's surprise, to go to India in order to hold on to her job. Accompanied by two colleagues, she sets out on a perilous road trip to the other side of the world.",
            'popularity': 3.53,
            'rating_average': 6.1,
            'rating_count': 61,
            'release_date': '2017-08-02',
            'runtime': None,
            'status': None,
            'backdrop_path': '/qCfcrZdYCMB7GOr7971T6jLR5kl.jpg',
            'poster_path': '/8dTtG54rJbg3HWxFptUageWcfBD.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/456768',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 617120,
            'title': 'Test',
            'genres': None,
            'overview':
            'Kurt Longson tries to avenge his daughters death. To succeed he has to battle with his conscience and morality to realize true love.',
            'popularity': 2.16,
            'rating_average': 4.7,
            'rating_count': 23,
            'release_date': '2018-05-22',
            'runtime': None,
            'status': None,
            'backdrop_path': None,
            'poster_path': '/5F6eKWJNHfYgHf2PDsb73fmAdK8.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/617120',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 637254,
            'title': 'Test Pattern',
            'genres': None,
            'overview':
            'A relationship is put to the test after the girlfriend is sexually assaulted and the boyfriend drives her from hospital to hospital in search of a rape kit.',
            'popularity': 2.772,
            'rating_average': 7.3,
            'rating_count': 4,
            'release_date': '2021-02-19',
            'runtime': None,
            'status': None,
            'backdrop_path': '/x5t4isLoBmetWszgZRD1LI1VgQX.jpg',
            'poster_path': '/26TUusJoyE5G1KVpu2IijUi9hbi.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/637254',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 67506,
            'title': 'Test Pilot Donald',
            'genres': None,
            'overview':
            "Donald flies his model airplane into Chip 'n Dale's tree. Dale climbs in and proceeds to cause trouble.",
            'popularity': 3.63,
            'rating_average': 5.8,
            'rating_count': 11,
            'release_date': '1951-06-08',
            'runtime': None,
            'status': None,
            'backdrop_path': '/cHgjAltr4EuNlSKeUhAb1N4OYGo.jpg',
            'poster_path': '/5hQ4AozcvTmr74xDHotE8UG4yDN.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/67506',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 160647,
            'title': '3 Day Test',
            'genres': None,
            'overview':
            "Martin Taylor has totally lost touch with his family. He has no clue who his teenage daughter's friends are, why his son only communicates with an electronic sign outside his bedroom door, or why his youngest child only watches faith TV. Convinced the family needs to reconnect, Martin surprises the wife and kids with a little experiment-he locks them in their own home with no power, no heat, no running water, and absolutely no contact with the world outside! The sudden holiday staycation isn't what the Taylors had in mind for the weekend, but they'll have to team up to prove they can survive Dad's wacky mission. With a heartfelt message and some persistence, one little member of the family helps put their priorities back in the pews, because they'll need all the faith they have to get through this!",
            'popularity': 3.487,
            'rating_average': 5.3,
            'rating_count': 17,
            'release_date': '2012-11-05',
            'runtime': None,
            'status': None,
            'backdrop_path': '/e8RKGOcU1QpNoDpBzwCxfTDSQep.jpg',
            'poster_path': '/tU92SyvB0YKjgkZx3qW6iu89BQq.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/160647',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 749645,
            'title': 'The Beta Test',
            'genres': None,
            'overview':
            'A married Hollywood agent receives a mysterious letter for an anonymous sexual encounter and becomes ensnared in a sinister world of lying, infidelity, and digital data.',
            'popularity': 2.744,
            'rating_average': 0,
            'rating_count': 0,
            'release_date': '2021-06-18',
            'runtime': None,
            'status': None,
            'backdrop_path': '/dS933c3Yv9Qxi4DU9yaW1WfFhCC.jpg',
            'poster_path': '/rqX3bH4h46U9hQTReEjWWHBTbnv.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/749645',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }, {
            'code': 355161,
            'title': 'Crash Test',
            'genres': None,
            'overview':
            'Adapted from their beloved comedy show at Upright Citizens Brigade, Crash Test showcases Rob Huebel and Paul Scheer on a state-of-the-art party bus adventure, picking up famous comedians and celebrities as they go on a sightseeing tour of Los Angeles. Ben Stiller, Stuart Cornfeld and Mike Rosenstein of Red Hour executive produced the special.',
            'popularity': 1.738,
            'rating_average': 5.8,
            'rating_count': 8,
            'release_date': '2015-08-18',
            'runtime': None,
            'status': None,
            'backdrop_path': None,
            'poster_path': '/aYyVunZFovilRWCiQMhgWu99ZIa.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/355161',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            '__typename': 'Movie'
        }]
    }

    assert dict == get_search("da39a3ee5e@da39a3ee5e.com", tmdb, "test", 1, db)

