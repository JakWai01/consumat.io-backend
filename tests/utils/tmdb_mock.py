class TmdbMock:
    def __init__(self: object, tmdb_key: str, db: object):
        pass

    def get_movie_details(self: object, external_id: str, movie_id: int) -> dict:
        return {
            "code": 12,
            'title': 'Finding Nemo',
            'genres': [{
                'name': 'Animation'
            }, {
                'name': 'Family'
            }],
            'overview':
            "Nemo, an adventurous young clownfish, is unexpectedly taken from his Great Barrier Reef home to a dentist's office aquarium. It's up to his worrisome father Marlin and a friendly but forgetful fish Dory to bring Nemo home -- meeting vegetarian sharks, surfer dude turtles, hypnotic jellyfish, hungry seagulls, and more along the way.",
            'popularity': 66.144,
            'rating_average': 7.8,
            'rating_count': 15073,
            'release_date': '2003-05-30',
            'runtime': 100,
            'status': 'Released',
            'backdrop_path': '/dFYguAfeVt19qAbzJ5mArn7DEJw.jpg',
            'poster_path': '/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg'
        }

    def get_movie_providers(self: object, external_id: str, movie_id: int) -> dict:
        return {'providers': [{'name': 'Disney Plus'}]}

    def get_movie_credits(self: object, movie_id: int) -> dict:
        return {
            'cast': [{
                'name': 'Albert Brooks',
                'role': 'Marlin (voice)',
                'image_path': '/8iDSGu5l93N7benjf6b3AysBore.jpg',
                'job': 'Acting'
            }, {
                'name': 'Ellen DeGeneres',
                'role': 'Dory (voice)',
                'image_path': '/z8IEEid4z63CBlJtxrTKEfsW7NA.jpg',
                'job': 'Acting'
            }, {
                'name': 'Alexander Gould',
                'role': 'Nemo (voice)',
                'image_path': '/fe4mUSp0XotA6Ku4Bs69Q9o2lqU.jpg',
                'job': 'Acting'
            }, {
                'name': 'Willem Dafoe',
                'role': 'Gill (voice)',
                'image_path': '/nbv4rIpJnw0OvowBZgwEWVriH9V.jpg',
                'job': 'Acting'
            }, {
                'name': 'Brad Garrett',
                'role': 'Bloat (voice)',
                'image_path': '/813ffbpoaoaJRdoe1yrbivboWKp.jpg',
                'job': 'Acting'
            }, {
                'name': 'Allison Janney',
                'role': 'Peach (voice)',
                'image_path': '/cDcB8mKP1GiIeoM3Qe7GIucs0iv.jpg',
                'job': 'Acting'
            }, {
                'name': 'Austin Pendleton',
                'role': 'Gurgle (voice)',
                'image_path': '/nrXfqtXDDYzSFNLPQnfLkus4I7s.jpg',
                'job': 'Acting'
            }, {
                'name': 'Stephen Root',
                'role': 'Bubbles (voice)',
                'image_path': '/ihcP1Bbnj9QkC9tEoDA4IkmV2tX.jpg',
                'job': 'Acting'
            }, {
                'name': 'Vicki Lewis',
                'role': 'Deb / Flo (voice)',
                'image_path': '/x0LqiqXF53vLYX4O4Chpd1EWw8u.jpg',
                'job': 'Acting'
            }, {
                'name': 'Joe Ranft',
                'role': 'Jacques (voice)',
                'image_path': '/f1BoWC2JbCcfP1e5hKfGsxkHzVU.jpg',
                'job': 'Writing'
            }, {
                'name': 'Geoffrey Rush',
                'role': 'Nigel (voice)',
                'image_path': '/npXFjaFQzBNroCEPllGPTZ5IisA.jpg',
                'job': 'Acting'
            }, {
                'name': 'Andrew Stanton',
                'role': 'Crush (voice)',
                'image_path': '/gasNitCwepbqNcYBmDHpsCgZH0I.jpg',
                'job': 'Writing'
            }, {
                'name': 'Elizabeth Perkins',
                'role': 'Coral (voice)',
                'image_path': '/vTWYllD9V76rgv9XAbtkkjjeunG.jpg',
                'job': 'Acting'
            }, {
                'name': 'Nicholas Bird',
                'role': 'Squirt (voice)',
                'image_path': '/grsKC7Yp8Sfx8fwJnEM59GG4ogX.jpg',
                'job': 'Acting'
            }, {
                'name': 'Bob Peterson',
                'role': 'Mr. Ray (voice)',
                'image_path': '/dJe3nTCIToebjj1WHFHP7LmZKyk.jpg',
                'job': 'Acting'
            }, {
                'name': 'Barry Humphries',
                'role': 'Bruce (voice)',
                'image_path': '/7WClJFIZ7QDkTMgFi8Rl1XQp6wV.jpg',
                'job': 'Acting'
            }, {
                'name': 'Eric Bana',
                'role': 'Anchor (voice)',
                'image_path': '/j8tbvkg0kyCZihbwrUNRxwhqXXe.jpg',
                'job': 'Acting'
            }, {
                'name': 'Bruce Spence',
                'role': 'Chum (voice)',
                'image_path': '/kuaIudFTIBahGAdCamThG13jPp7.jpg',
                'job': 'Acting'
            }, {
                'name': 'Bill Hunter',
                'role': 'Dentist (voice)',
                'image_path': '/gvrRsTfx47KupgRwTKp0gqryHPe.jpg',
                'job': 'Acting'
            }, {
                'name': 'LuLu Ebeling',
                'role': 'Darla (voice)',
                'image_path': None,
                'job': 'Acting'
            }, {
                'name': 'Jordan Ranft',
                'role': 'Tad (voice)',
                'image_path': None,
                'job': 'Acting'
            }, {
                'name': 'Erica Beck',
                'role': 'Pearl (voice)',
                'image_path': '/k4R1E1aXQ2hwjFUCu9Wnz0PU1H8.jpg',
                'job': 'Acting'
            }, {
                'name': 'Erik Per Sullivan',
                'role': 'Sheldon (voice)',
                'image_path': '/87eGn2O4NCz6Q1MFCQUCWxF0N6x.jpg',
                'job': 'Acting'
            }, {
                'name': 'John Ratzenberger',
                'role': 'Fish School (voice)',
                'image_path': '/oRtDEOuIO1yDhTz5dORBdxXuLMO.jpg',
                'job': 'Acting'
            }, {
                'name': 'Jack Angel',
                'role': 'Additional Voices (voice)',
                'image_path': '/jPOuOHzYV7VYC4Ozy3u4nvnDZxO.jpg',
                'job': 'Acting'
            }, {
                'name': 'Mickie McGowan',
                'role': 'Additional Voices (voice)',
                'image_path': '/4K1HF10EvDjdaIoDAnWqFZjnmvk.jpg',
                'job': 'Acting'
            }],
            'directors': [{
                'name': 'Andrew Stanton',
                'image_path': '/gasNitCwepbqNcYBmDHpsCgZH0I.jpg'
            }]
        }

    def get_tv_details(self: object, external_id: str, tv_id: int) -> dict:
        return {
            'code':
            1399,
            'title':
            'Game of Thrones',
            'genres': [{
                'name': 'Sci-Fi & Fantasy'
            }, {
                'name': 'Drama'
            }, {
                'name': 'Action & Adventure'
            }],
            'overview':
            "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
            'popularity':
            485.212,
            'rating_average':
            8.4,
            'rating_count':
            14600,
            'first_air_date':
            '2011-04-17',
            'last_air_date':
            '2019-05-19',
            'status':
            'Ended',
            'creators': [{
                'name': 'David Benioff',
                'image_path': '/xvNN5huL0X8yJ7h3IZfGG4O2zBD.jpg'
            }, {
                'name': 'D. B. Weiss',
                'image_path': '/2RMejaT793U9KRk2IEbFfteQntE.jpg'
            }],
            'number_of_episodes':
            73,
            'number_of_seasons':
            8,
            'backdrop_path':
            '/suopoADq0k8YZr4dQXcU6pToj6s.jpg',
            'poster_path':
            '/u3bZgnGQ9T01sWNhyveQz0wH0Hl.jpg',
            'runtime':
            60
        }

    def get_tv_providers(self: object, external_id: str, tv_id: int) -> dict:
        return {'providers': [{'name': 'Sky Go'}, {'name': 'Sky Ticket'}]}

    def get_tv_credits(self: object, tv_id: int) -> dict:
        return {
            'cast': [{
                'name': 'Emilia Clarke',
                'role': 'Daenerys Targaryen',
                'image_path': '/86jeYFV40KctQMDQIWhJ5oviNGj.jpg',
                'job': 'Acting'
            }, {
                'name': 'Lena Headey',
                'role': 'Cersei Lannister',
                'image_path': '/xR2IBnBlUdyBe5hecaVdtRuQqUE.jpg',
                'job': 'Acting'
            }, {
                'name': 'Sophie Turner',
                'role': 'Sansa Stark',
                'image_path': '/1hUAKYvSi4vZSYvTnD2TlqF6VVx.jpg',
                'job': 'Acting'
            }, {
                'name': 'Kit Harington',
                'role': 'Jon Snow',
                'image_path': '/wWTG27LBVTuHhIZ96aJcrkHuy8Z.jpg',
                'job': 'Acting'
            }, {
                'name': 'Peter Dinklage',
                'role': 'Tyrion Lannister',
                'image_path': '/lRsRgnksAhBRXwAB68MFjmTtLrk.jpg',
                'job': 'Acting'
            }, {
                'name': 'Nikolaj Coster-Waldau',
                'role': 'Jaime Lannister',
                'image_path': '/dv1zRmSvSg8lDrxeM0SswYze6Z0.jpg',
                'job': 'Acting'
            }, {
                'name': 'Maisie Williams',
                'role': 'Arya Stark',
                'image_path': '/zLTq39cdRjS43dEzb78c1p1QcbT.jpg',
                'job': 'Acting'
            }, {
                'name': 'Liam Cunningham',
                'role': 'Davos Seaworth',
                'image_path': '/ljmFT9zYqh4k2bmEcNU6rxoE7fW.jpg',
                'job': 'Acting'
            }, {
                'name': 'John Bradley',
                'role': 'Samwell Tarly',
                'image_path': '/eLcisM9qqCLWnf0iImHuSn08FOi.jpg',
                'job': 'Acting'
            }, {
                'name': 'Conleth Hill',
                'role': 'Varys',
                'image_path': '/eeTnNiustUbShHU09EQ6LoOpzcg.jpg',
                'job': 'Acting'
            }, {
                'name': 'Gwendoline Christie',
                'role': 'Brienne of Tarth',
                'image_path': '/kmlv5i02n3zKryBr2W3kSeWVKTD.jpg',
                'job': 'Acting'
            }, {
                'name': 'Jacob Anderson',
                'role': 'Grey Worm',
                'image_path': '/atkSptvQU7XdRVGrL5hiymbXwhd.jpg',
                'job': 'Acting'
            }, {
                'name': 'Jerome Flynn',
                'role': 'Bronn',
                'image_path': '/yI5xxWITp2YjMgiwac72Nen60jq.jpg',
                'job': 'Acting'
            }, {
                'name': 'Rory McCann',
                'role': 'Sandor Clegane',
                'image_path': '/meEHyiCRXTTCiYQMzP4VEdvEuD0.jpg',
                'job': 'Acting'
            }, {
                'name': 'Joe Dempsie',
                'role': 'Gendry',
                'image_path': '/lnR0AMIwxQR6zUCOhp99GnMaRet.jpg',
                'job': 'Acting'
            }, {
                'name': 'Isaac Hempstead-Wright',
                'role': 'Bran Stark',
                'image_path': '/b6hQvID3oXPXnyrrXs22MBv2lyN.jpg',
                'job': 'Acting'
            }]
        }

    def get_season_details(self: object, external_id: str, tv_id: int,
                           season_number: int) -> dict:
        return {
            'code': 3624,
            'tv_code': 1399,
            'season_number': 1,
            'title': 'Season 1',
            'overview':
            "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring.",
            'air_date': '2011-04-17',
            'number_of_episodes': 10,
            'poster_path': '/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg'
        }

    def get_episode_details(self: object, external_id: str, tv_id: int, season_number: int,
                            episode_number: int) -> dict:
        return {
            'code': 63056,
            'title': 'Winter Is Coming',
            'episode_number': 1,
            'season_number': 1,
            'overview':
            "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
            'air_date': '2011-04-17',
            'rating_average': 7.661,
            'still_path': '/xIfvIM7YgkADTrqp23rm3CLaOVQ.jpg'
        }

    def get_search_result(self: object, external_id: str, keyword: str, page: int) -> dict:
        return {
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
                'first_air_date': '2005-09-17',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/ecxpOnYv7iTUVNUmZRoxRksaC1f.jpg',
                'poster_path': '/rn5YbXP4UunS0BLhmjqndHJYhp.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/1769',
                'runtime': None,
                'rating_count': 80
            }, {
                'code': 226979,
                'title': 'Test',
                'genres': None,
                'overview':
                'San Francisco, 1985. Two opposites attract at a modern dance company. Together, their courage and resilience are tested as they navigate a world full of risks and promise, against the backdrop of a disease no one seems to know anything about.',
                'popularity': 5.496,
                'rating_average': 6.6,
                'release_date': '2013-06-29',
                'runtime': None,
                'status': None,
                'backdrop_path': '/xySCWwZVuU03xOsJfs1Qk8yG2DF.jpg',
                'poster_path': '/tTWRomgIMOoIB3CJLPlVbqSawEm.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/226979',
                'rating_count': 105
            }, {
                'code': 401123,
                'title': 'Beta Test',
                'genres': None,
                'overview':
                "While testing the latest first person shooter from global game developer, Sentinel, video game champion Max Troy discovers the events happening within the game are being reflected in the real world. He soon determines that the game's protagonist is real-life Orson Creed, an ex-Sentinel employee who is being remotely controlled by the corporation for reasons unknown. As virtual and real worlds collide, Max and Creed must join forces to unravel the conspiracy before the game's sinister events escalate and overwhelm the city.",
                'popularity': 5.633,
                'rating_average': 5.3,
                'release_date': '2016-07-22',
                'runtime': None,
                'status': None,
                'backdrop_path': '/rG2jdLdj4U55MgI3g9f85w2th1y.jpg',
                'poster_path': '/zKisJfMxpp0KfX4P3VyDrH0edg6.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/401123',
                'rating_count': 137
            }, {
                'code': 71761,
                'title': 'Bäst i test',
                'genres': None,
                'overview': 'Swedish version of Taskmaster.',
                'popularity': 8.346,
                'rating_average': 5.8,
                'first_air_date': '2017-03-10',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/gNzlviwUtStMOxNiLYmU0GDswV5.jpg',
                'poster_path': '/nnT18R49fIKFmmfaQqMXcBEaplK.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/71761',
                'runtime': None,
                'rating_count': 4
            }, {
                'code': 43155,
                'title': 'Test Pilot',
                'genres': None,
                'overview':
                'Jim is a test pilot. His wife Ann and best friend Gunner try their best to keep him sober. But the life of a test pilot is anything but safe.',
                'popularity': 5.171,
                'rating_average': 6.5,
                'release_date': '1938-04-16',
                'runtime': None,
                'status': None,
                'backdrop_path': '/qyM5OA9UfIlNWocQrI3BH7CZhxo.jpg',
                'poster_path': '/j3Xn5Zl9IGOHyEqNYU31eyiLTQE.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/43155',
                'rating_count': 43
            }, {
                'code': 4591,
                'title': "America's Test Kitchen",
                'genres': None,
                'overview':
                "America's Test Kitchen is a half-hour cooking show distributed to public television stations in the United States, also airing in Canada. The show's host is Cook's Illustrated editor-in-chief Christopher Kimball; the show and the magazine are affiliated, and the magazine's test kitchen facility in Brookline, Massachusetts, is used as a set for the show.\n\nCook's Illustrated's parent company, Boston Common Press, renamed itself America's Test Kitchen in 2004.",
                'popularity': 7.658,
                'rating_average': 8,
                'first_air_date': '2001-08-04',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/2UwBG0nStY7JhLQnP5LKVSGPNx4.jpg',
                'poster_path': '/eZjnMVcVgdSwJJB6aLfcqefxq0z.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/4591',
                'runtime': None,
                'rating_count': 6
            }, {
                'code': 679548,
                'title': 'The Alpha Test',
                'genres': None,
                'overview':
                'A suburban family drives their new gadget, The Alpha Home Assistant, to a killing rampage after mistreating and abusing it, leading to a full A.I. uprising…',
                'popularity': 5.356,
                'rating_average': 7,
                'release_date': '2021-02-04',
                'runtime': None,
                'status': None,
                'backdrop_path': '/6Hw9TxmY0PV93VB2CCQFFqqRFI4.jpg',
                'poster_path': '/ozbvCucRf3ZXUH5oQSdAayjLVdg.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/679548',
                'rating_count': 2
            }, {
                'code': 67102,
                'title': "Pilot Pirx's Inquest",
                'genres': None,
                'overview':
                'This movie is about a rocket pilot named Pirx who is hired to go on a mission to evaluate some nonlinears (robots) for use as crewmembers on future space flights. Pirx and his crew, made up of nonlinears and humans, are sent out to launch two satellites into the rings of Saturn. Upon returning to Earth there is an inquest to determine if Pirx was responsible for the "accident." In the end, it is found that one of the robots caused the malfunction in an attempt to kill the human crewmembers and Pirx is cleared of all charges. In this tale Lem puts forth the idea that what is perceived a human weakness is in fact an advantage over a perfect machine. Pirx defeats the robot, because a human can hesitate, make wrong decisions, have doubts, but a robot cannot. A similar idea is present in Isaac Asimov\'s Robot Series, where putting a robot in a position where it cannot chose between the Three laws of robotics fries its positronic brain.',
                'popularity': 3.977,
                'rating_average': 5.8,
                'release_date': '1979-05-27',
                'runtime': None,
                'status': None,
                'backdrop_path': '/xE3Y5ntcbqDz9FzwLWSVVR5qF7H.jpg',
                'poster_path': '/pqjWWjZlCGIW1dsdeLqS9mR0DbB.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/67102',
                'rating_count': 17
            }, {
                'code': 456768,
                'title': 'Crash Test Aglaé',
                'genres': None,
                'overview':
                "Aglaé, a young factory worker, has only one focus in life: her job at a car crash test site. When she learns that the factory is going to be relocated abroad, she accepts, to everyone's surprise, to go to India in order to hold on to her job. Accompanied by two colleagues, she sets out on a perilous road trip to the other side of the world.",
                'popularity': 3.53,
                'rating_average': 6.1,
                'release_date': '2017-08-02',
                'runtime': None,
                'status': None,
                'backdrop_path': '/qCfcrZdYCMB7GOr7971T6jLR5kl.jpg',
                'poster_path': '/8dTtG54rJbg3HWxFptUageWcfBD.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/456768',
                'rating_count': 61
            }, {
                'code': 617120,
                'title': 'Test',
                'genres': None,
                'overview':
                'Kurt Longson tries to avenge his daughters death. To succeed he has to battle with his conscience and morality to realize true love.',
                'popularity': 2.16,
                'rating_average': 4.7,
                'release_date': '2018-05-22',
                'runtime': None,
                'status': None,
                'backdrop_path': None,
                'poster_path': '/5F6eKWJNHfYgHf2PDsb73fmAdK8.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/617120',
                'rating_count': 23
            }, {
                'code': 637254,
                'title': 'Test Pattern',
                'genres': None,
                'overview':
                'A relationship is put to the test after the girlfriend is sexually assaulted and the boyfriend drives her from hospital to hospital in search of a rape kit.',
                'popularity': 2.772,
                'rating_average': 7.3,
                'release_date': '2021-02-19',
                'runtime': None,
                'status': None,
                'backdrop_path': '/x5t4isLoBmetWszgZRD1LI1VgQX.jpg',
                'poster_path': '/26TUusJoyE5G1KVpu2IijUi9hbi.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/637254',
                'rating_count': 4
            }, {
                'code': 67506,
                'title': 'Test Pilot Donald',
                'genres': None,
                'overview':
                "Donald flies his model airplane into Chip 'n Dale's tree. Dale climbs in and proceeds to cause trouble.",
                'popularity': 3.63,
                'rating_average': 5.8,
                'release_date': '1951-06-08',
                'runtime': None,
                'status': None,
                'backdrop_path': '/cHgjAltr4EuNlSKeUhAb1N4OYGo.jpg',
                'poster_path': '/5hQ4AozcvTmr74xDHotE8UG4yDN.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/67506',
                'rating_count': 11
            }, {
                'code': 160647,
                'title': '3 Day Test',
                'genres': None,
                'overview':
                "Martin Taylor has totally lost touch with his family. He has no clue who his teenage daughter's friends are, why his son only communicates with an electronic sign outside his bedroom door, or why his youngest child only watches faith TV. Convinced the family needs to reconnect, Martin surprises the wife and kids with a little experiment-he locks them in their own home with no power, no heat, no running water, and absolutely no contact with the world outside! The sudden holiday staycation isn't what the Taylors had in mind for the weekend, but they'll have to team up to prove they can survive Dad's wacky mission. With a heartfelt message and some persistence, one little member of the family helps put their priorities back in the pews, because they'll need all the faith they have to get through this!",
                'popularity': 3.487,
                'rating_average': 5.3,
                'release_date': '2012-11-05',
                'runtime': None,
                'status': None,
                'backdrop_path': '/e8RKGOcU1QpNoDpBzwCxfTDSQep.jpg',
                'poster_path': '/tU92SyvB0YKjgkZx3qW6iu89BQq.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/160647',
                'rating_count': 17
            }, {
                'code': 749645,
                'title': 'The Beta Test',
                'genres': None,
                'overview':
                'A married Hollywood agent receives a mysterious letter for an anonymous sexual encounter and becomes ensnared in a sinister world of lying, infidelity, and digital data.',
                'popularity': 2.744,
                'rating_average': 0,
                'release_date': '2021-06-18',
                'runtime': None,
                'status': None,
                'backdrop_path': '/dS933c3Yv9Qxi4DU9yaW1WfFhCC.jpg',
                'poster_path': '/rqX3bH4h46U9hQTReEjWWHBTbnv.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/749645',
                'rating_count': 0
            }, {
                'code': 355161,
                'title': 'Crash Test',
                'genres': None,
                'overview':
                'Adapted from their beloved comedy show at Upright Citizens Brigade, Crash Test showcases Rob Huebel and Paul Scheer on a state-of-the-art party bus adventure, picking up famous comedians and celebrities as they go on a sightseeing tour of Los Angeles. Ben Stiller, Stuart Cornfeld and Mike Rosenstein of Red Hour executive produced the special.',
                'popularity': 1.738,
                'rating_average': 5.8,
                'release_date': '2015-08-18',
                'runtime': None,
                'status': None,
                'backdrop_path': None,
                'poster_path': '/aYyVunZFovilRWCiQMhgWu99ZIa.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/355161',
                'rating_count': 8
            }]
        }

    def get_popular_movies(self: object, external_id: str, page: int) -> dict:
        return {
            'total_pages':
            500,
            'results': [{
                'code': 337404,
                'title': 'Cruella',
                'genres': None,
                'overview':
                'In 1970s London amidst the punk rock revolution, a young grifter named Estella is determined to make a name for herself with her designs. She befriends a pair of young thieves who appreciate her appetite for mischief, and together they are able to build a life for themselves on the London streets. One day, Estella’s flair for fashion catches the eye of the Baroness von Hellman, a fashion legend who is devastatingly chic and terrifyingly haute. But their relationship sets in motion a course of events and revelations that will cause Estella to embrace her wicked side and become the raucous, fashionable and revenge-bent Cruella.',
                'popularity': 6821.402,
                'rating_average': 8.8,
                'rating_count': 1560,
                'release_date': '2021-05-27',
                'runtime': None,
                'status': None,
                'backdrop_path': '/6MKr3KgOLmzOP6MSuZERO41Lpkt.jpg',
                'poster_path': '/A0knvX7rlwTyZSKj8H5NiARb45.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/337404'
            }, {
                'code': 637649,
                'title': 'Wrath of Man',
                'genres': None,
                'overview':
                "A cold and mysterious new security guard for a Los Angeles cash truck company surprises his co-workers when he unleashes precision skills during a heist. The crew is left wondering who he is and where he came from. Soon, the marksman's ultimate motive becomes clear as he takes dramatic and irrevocable steps to settle a score.",
                'popularity': 3381.321,
                'rating_average': 8,
                'rating_count': 606,
                'release_date': '2021-05-20',
                'runtime': None,
                'status': None,
                'backdrop_path': '/77tui163estZrQ78NBggqDB4n2C.jpg',
                'poster_path': '/YxopfHpsCV1oF8CZaL4M3Eodqa.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/637649'
            }, {
                'code': 503736,
                'title': 'Army of the Dead',
                'genres': None,
                'overview':
                'Following a zombie outbreak in Las Vegas, a group of mercenaries take the ultimate gamble: venturing into the quarantine zone to pull off the greatest heist ever attempted.',
                'popularity': 2615.629,
                'rating_average': 6.6,
                'rating_count': 1290,
                'release_date': '2021-05-21',
                'runtime': None,
                'status': None,
                'backdrop_path': '/9WlJFhOSCPnaaSmsrv0B4zA8iUb.jpg',
                'poster_path': '/z8CExJekGrEThbpMXAmCFvvgoJR.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/503736'
            }, {
                'code': 460465,
                'title': 'Mortal Kombat',
                'genres': None,
                'overview':
                "Washed-up MMA fighter Cole Young, unaware of his heritage, and hunted by Emperor Shang Tsung's best warrior, Sub-Zero, seeks out and trains with Earth's greatest champions as he prepares to stand against the enemies of Outworld in a high stakes battle for the universe.",
                'popularity': 1641.256,
                'rating_average': 7.6,
                'rating_count': 2837,
                'release_date': '2021-05-06',
                'runtime': None,
                'status': None,
                'backdrop_path': '/mPBI506o7gITnjoSkcyPneK9s8n.jpg',
                'poster_path': '/nkayOAUBUu4mMvyNf9iHSUiPjF1.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/460465'
            }, {
                'code': 567189,
                'title': "Tom Clancy's Without Remorse",
                'genres': None,
                'overview':
                'An elite Navy SEAL uncovers an international conspiracy while seeking justice for the murder of his pregnant wife.',
                'popularity': 1361.356,
                'rating_average': 7.2,
                'rating_count': 1087,
                'release_date': '2021-04-30',
                'runtime': None,
                'status': None,
                'backdrop_path': '/fPGeS6jgdLovQAKunNHX8l0avCy.jpg',
                'poster_path': '/rEm96ib0sPiZBADNKBHKBv5bve9.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/567189'
            }, {
                'code': 399566,
                'title': 'Godzilla vs. Kong',
                'genres': None,
                'overview':
                'In a time when monsters walk the Earth, humanity’s fight for its future sets Godzilla and Kong on a collision course that will see the two most powerful forces of nature on the planet collide in a spectacular battle for the ages.',
                'popularity': 1399.418,
                'rating_average': 8.1,
                'rating_count': 5808,
                'release_date': '2021-03-25',
                'runtime': None,
                'status': None,
                'backdrop_path': '/inJjDhCjfhh3RtrJWBmmDqeuSYC.jpg',
                'poster_path': '/pgqgaUx1cJb5oZQQ5v0tNARCeBp.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/399566'
            }, {
                'code': 578701,
                'title': 'Those Who Wish Me Dead',
                'genres': None,
                'overview':
                'A young boy finds himself pursued by two assassins in the Montana wilderness with a survival expert determined to protecting him - and a forest fire threatening to consume them all.',
                'popularity': 1243.188,
                'rating_average': 7,
                'rating_count': 374,
                'release_date': '2021-06-03',
                'runtime': None,
                'status': None,
                'backdrop_path': '/iDdpiUnCeXvBmrkBFpL6lKsZt33.jpg',
                'poster_path': '/xCEg6KowNISWvMh8GvPSxtdf9TO.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/578701'
            }, {
                'code': 527774,
                'title': 'Raya and the Last Dragon',
                'genres': None,
                'overview':
                'Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.',
                'popularity': 1055.191,
                'rating_average': 8.2,
                'rating_count': 3001,
                'release_date': '2021-03-05',
                'runtime': None,
                'status': None,
                'backdrop_path': '/hJuDvwzS0SPlsE6MNFOpznQltDZ.jpg',
                'poster_path': '/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/527774'
            }, {
                'code': 615457,
                'title': 'Nobody',
                'genres': None,
                'overview':
                'Hutch Mansell, a suburban dad, overlooked husband, nothing neighbor — a "nobody." When two thieves break into his home one night, Hutch\'s unknown long-simmering rage is ignited and propels him on a brutal path that will uncover dark secrets he fought to leave behind.',
                'popularity': 1048.459,
                'rating_average': 8.5,
                'rating_count': 1804,
                'release_date': '2021-06-10',
                'runtime': None,
                'status': None,
                'backdrop_path': '/6zbKgwgaaCyyBXE4Sun4oWQfQmi.jpg',
                'poster_path': '/oBgWY00bEFeZ9N25wWVyuQddbAo.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/615457'
            }, {
                'code': 520763,
                'title': 'A Quiet Place Part II',
                'genres': None,
                'overview':
                'Following the events at home, the Abbott family now face the terrors of the outside world. Forced to venture into the unknown, they realize that the creatures that hunt by sound are not the only threats that lurk beyond the sand path.',
                'popularity': 1040.555,
                'rating_average': 7.4,
                'rating_count': 117,
                'release_date': '2021-06-24',
                'runtime': None,
                'status': None,
                'backdrop_path': '/z2UtGA1WggESspi6KOXeo66lvLx.jpg',
                'poster_path': '/4q2hz2m8hubgvijz8Ez0T2Os2Yv.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/520763'
            }, {
                'code': 726684,
                'title':
                'Miraculous World: Shanghai – The Legend of Ladydragon',
                'genres': None,
                'overview':
                'On school break, Marinette heads to Shanghai to meet Adrien. But after arriving, Marinette loses all her stuff, including the Miraculous that allows her to turn into Ladybug!',
                'popularity': 964.043,
                'rating_average': 7.9,
                'rating_count': 375,
                'release_date': '2021-05-23',
                'runtime': None,
                'status': None,
                'backdrop_path': '/rlNnwObbMu5G2FaOUlacnUIdIIA.jpg',
                'poster_path': '/msI5a9TPnepx47JUb2vl88hb80R.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/726684'
            }, {
                'code': 635302,
                'title':
                'Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train',
                'genres': None,
                'overview':
                "Tanjirō Kamado, joined with Inosuke Hashibira, a boy raised by boars who wears a boar's head, and Zenitsu Agatsuma, a scared boy who reveals his true power when he sleeps, boards the Infinity Train on a new mission with the Fire Hashira, Kyōjurō Rengoku, to defeat a demon who has been tormenting the people and killing the demon slayers who oppose it!",
                'popularity': 1011.75,
                'rating_average': 8.4,
                'rating_count': 1110,
                'release_date': '2021-05-20',
                'runtime': None,
                'status': None,
                'backdrop_path': '/xPpXYnCWfjkt3zzE0dpCNME1pXF.jpg',
                'poster_path': '/h8Rb9gBr48ODIwYUttZNYeMWeUU.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/635302'
            }, {
                'code': 791373,
                'title': "Zack Snyder's Justice League",
                'genres': None,
                'overview':
                "Determined to ensure Superman's ultimate sacrifice was not in vain, Bruce Wayne aligns forces with Diana Prince with plans to recruit a team of metahumans to protect the world from an approaching threat of catastrophic proportions.",
                'popularity': 907.096,
                'rating_average': 8.5,
                'rating_count': 5661,
                'release_date': '2021-03-18',
                'runtime': None,
                'status': None,
                'backdrop_path': '/pcDc2WJAYGJTTvRSEIpRZwM3Ola.jpg',
                'poster_path': '/tnAuB8q5vv7Ax9UAEje5Xi4BXik.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/791373'
            }, {
                'code': 811367,
                'title': '22 vs. Earth',
                'genres': None,
                'overview':
                'Set before the events of ‘Soul’, 22 refuses to go to Earth, enlisting a gang of 5 new souls in attempt of rebellion. However, 22’s subversive plot leads to a surprising revelation about the meaning of life.',
                'popularity': 725.881,
                'rating_average': 7.2,
                'rating_count': 117,
                'release_date': '2021-04-30',
                'runtime': None,
                'status': None,
                'backdrop_path': '/n2y7T8wJVjJ8yLhQXQgNCpsC3ga.jpg',
                'poster_path': '/32vLDKSzcCMh55zqqaSqqUA8naz.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/811367'
            }, {
                'code': 586047,
                'title': 'Seobok',
                'genres': None,
                'overview':
                'A former intelligence agent gets involved with the first human clone, Seo Bok, who others seek, causing trouble.',
                'popularity': 745.953,
                'rating_average': 7.7,
                'rating_count': 54,
                'release_date': '2021-07-23',
                'runtime': None,
                'status': None,
                'backdrop_path': '/yC4DRg5aGgNpkHpUDpLtBqzownS.jpg',
                'poster_path': '/nxxuWC32Y6TULj4VnVwMPUFLIpK.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/586047'
            }, {
                'code': 259693,
                'title': 'The Conjuring 2',
                'genres': None,
                'overview':
                'Lorraine and Ed Warren travel to north London to help a single mother raising four children alone in a house plagued by malicious spirits.',
                'popularity': 919.148,
                'rating_average': 7.2,
                'rating_count': 5907,
                'release_date': '2016-06-16',
                'runtime': None,
                'status': None,
                'backdrop_path': '/sWHlCeJ2RunM5eq3FYA4VuTUNqY.jpg',
                'poster_path': '/zEqyD0SBt6HL7W9JQoWwtd5Do1T.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/259693'
            }, {
                'code': 647302,
                'title': 'Benny Loves You',
                'genres': None,
                'overview':
                'Jack, a man desperate to improve his life, throws away his beloved childhood plush, Benny. It’s a move that has disastrous consequences when Benny springs to life with deadly intentions!',
                'popularity': 650.09,
                'rating_average': 6.1,
                'rating_count': 30,
                'release_date': '2021-07-16',
                'runtime': None,
                'status': None,
                'backdrop_path': '/czHYg6LQ5926OL8wj5kC09pNR12.jpg',
                'poster_path': '/mQ8vALvqA0z0qglG3gI6xpVcslo.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/647302'
            }, {
                'code': 643586,
                'title': "Willy's Wonderland",
                'genres': None,
                'overview':
                "When his car breaks down, a quiet loner agrees to clean an abandoned family fun center in exchange for repairs. He soon finds himself waging war against possessed animatronic mascots while trapped inside Willy's Wonderland.",
                'popularity': 584.484,
                'rating_average': 6.7,
                'rating_count': 235,
                'release_date': '2021-05-21',
                'runtime': None,
                'status': None,
                'backdrop_path': '/jFINtstDUh0vHOGImpMAmLrPcXy.jpg',
                'poster_path': '/keEnkeAvifw8NSEC4f6WsqeLJgF.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/643586'
            }, {
                'code': 138843,
                'title': 'The Conjuring',
                'genres': None,
                'overview':
                'Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse. Forced to confront a powerful entity, the Warrens find themselves caught in the most terrifying case of their lives.',
                'popularity': 814.365,
                'rating_average': 7.5,
                'rating_count': 8233,
                'release_date': '2013-08-01',
                'runtime': None,
                'status': None,
                'backdrop_path': '/l5yp73psXVRYy2ce09lD8yDuu2g.jpg',
                'poster_path': '/wVYREutTvI2tmxr6ujrHT704wGF.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/138843'
            }, {
                'code': 587807,
                'title': 'Tom & Jerry',
                'genres': None,
                'overview':
                'Tom the cat and Jerry the mouse get kicked out of their home and relocate to a fancy New York hotel, where a scrappy employee named Kayla will lose her job if she can’t evict Jerry before a high-class wedding at the hotel. Her solution? Hiring Tom to get rid of the pesky mouse.',
                'popularity': 540.018,
                'rating_average': 7.3,
                'rating_count': 1428,
                'release_date': '2021-06-17',
                'runtime': None,
                'status': None,
                'backdrop_path': '/9ns9463dwOeo1CK1JU2wirL5Yi1.jpg',
                'poster_path': '/8XZI9QZ7Pm3fVkigWJPbrXCMzjq.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/587807'
            }]
        }

    def get_popular_tv(self: object, external_id: str, page: int) -> dict:
        return {
            'total_pages':
            500,
            'results': [{
                'code': 63174,
                'title': 'Lucifer',
                'genres': None,
                'overview':
                "Bored and unhappy as the Lord of Hell, Lucifer Morningstar abandoned his throne and retired to Los Angeles, where he has teamed up with LAPD detective Chloe Decker to take down criminals.\xa0But the longer he's away from the underworld, the greater the threat that the worst of humanity could escape.",
                'popularity': 1642.45,
                'rating_average': 8.5,
                'rating_count': 9007,
                'first_air_date': '2016-01-25',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/h48Dpb7ljv8WQvVdyFWVLz64h4G.jpg',
                'poster_path': '/4EYPN5mVIhKLfxGruy7Dy41dTVn.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/63174',
                'runtime': None
            }, {
                'code': 91557,
                'title': 'Ragnarok',
                'genres': None,
                'overview':
                'A small Norwegian town experiencing warm winters and violent downpours seems to be headed for another Ragnarök -- unless someone intervenes in time.',
                'popularity': 1251.74,
                'rating_average': 8,
                'rating_count': 431,
                'first_air_date': '2020-01-31',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/wu444tM9YBllq9UcBv5TeidO3j3.jpg',
                'poster_path': '/xUtOM1QO4r8w8yeE00QvBdq58N5.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/91557',
                'runtime': None
            }, {
                'code': 60735,
                'title': 'The Flash',
                'genres': None,
                'overview':
                'After a particle accelerator causes a freak storm, CSI Investigator Barry Allen is struck by lightning and falls into a coma. Months later he awakens with the power of super speed, granting him the ability to move through Central City like an unseen guardian angel. Though initially excited by his newfound powers, Barry is shocked to discover he is not the only "meta-human" who was created in the wake of the accelerator explosion -- and not everyone is using their new powers for good. Barry partners with S.T.A.R. Labs and dedicates his life to protect the innocent. For now, only a few close friends and associates know that Barry is literally the fastest man alive, but it won\'t be long before the world learns what Barry Allen has become...The Flash.',
                'popularity': 1051.034,
                'rating_average': 7.7,
                'rating_count': 7739,
                'first_air_date': '2014-10-07',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/9Jmd1OumCjaXDkpllbSGi2EpJvl.jpg',
                'poster_path': '/lJA2RCMfsWoskqlQhXPSLFQGXEJ.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/60735',
                'runtime': None
            }, {
                'code': 71712,
                'title': 'The Good Doctor',
                'genres': None,
                'overview':
                "A young surgeon with Savant syndrome is recruited into the surgical unit of a prestigious hospital. The question will arise: can a person who doesn't have the ability to relate to people actually save their lives",
                'popularity': 1045.696,
                'rating_average': 8.6,
                'rating_count': 8551,
                'first_air_date': '2017-09-25',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/iDbIEpCM9nhoayUDTwqFL1iVwzb.jpg',
                'poster_path': '/6tfT03sGp9k4c0J3dypjrI8TSAI.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/71712',
                'runtime': None
            }, {
                'code': 120168,
                'title': 'Who Killed Sara?',
                'genres': None,
                'overview':
                "Hell-bent on exacting revenge and proving he was framed for his sister's murder, Álex sets out to unearth much more than the crime's real culprit.",
                'popularity': 798.923,
                'rating_average': 7.8,
                'rating_count': 761,
                'first_air_date': '2021-03-24',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/dYvIUzdh6TUv4IFRq8UBkX7bNNu.jpg',
                'poster_path': '/o7uk5ChRt3quPIv8PcvPfzyXdMw.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/120168',
                'runtime': None
            }, {
                'code': 95057,
                'title': 'Superman & Lois',
                'genres': None,
                'overview':
                "After years of facing megalomaniacal supervillains, monsters wreaking havoc on Metropolis, and alien invaders intent on wiping out the human race, The Man of Steel aka Clark Kent and Lois Lane come face to face with one of their greatest challenges ever: dealing with all the stress, pressures and complexities that come with being working parents in today's society.",
                'popularity': 748.941,
                'rating_average': 8.3,
                'rating_count': 901,
                'first_air_date': '2021-02-23',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/pPKiIJEEcV0E1hpVcWRXyp73ZpX.jpg',
                'poster_path': '/vlv1gn98GqMnKHLSh0dNciqGfBl.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/95057',
                'runtime': None
            }, {
                'code': 1416,
                'title': "Grey's Anatomy",
                'genres': None,
                'overview':
                'Follows the personal and professional lives of a group of doctors at Seattle’s Grey Sloan Memorial Hospital.',
                'popularity': 746.89,
                'rating_average': 8.2,
                'rating_count': 6164,
                'first_air_date': '2005-03-27',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/edmk8xjGBsYVIf4QtLY9WMaMcXZ.jpg',
                'poster_path': '/clnyhPqj1SNgpAdeSS6a6fwE6Bo.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/1416',
                'runtime': None
            }, {
                'code': 88396,
                'title': 'The Falcon and the Winter Soldier',
                'genres': None,
                'overview':
                'Following the events of “Avengers: Endgame”, the Falcon, Sam Wilson and the Winter Soldier, Bucky Barnes team up in a global adventure that tests their abilities, and their patience.',
                'popularity': 662.98,
                'rating_average': 7.9,
                'rating_count': 5721,
                'first_air_date': '2021-03-19',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/b0WmHGc8LHTdGCVzxRb3IBMur57.jpg',
                'poster_path': '/6kbAMLteGO8yyewYau6bJ683sw7.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/88396',
                'runtime': None
            }, {
                'code': 95557,
                'title': 'Invincible',
                'genres': None,
                'overview':
                'Mark Grayson is a normal teenager except for the fact that his father is the most powerful superhero on the planet. Shortly after his seventeenth birthday, Mark begins to develop powers of his own and enters into his father’s tutelage.',
                'popularity': 599.292,
                'rating_average': 8.9,
                'rating_count': 1934,
                'first_air_date': '2021-03-26',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/6UH52Fmau8RPsMAbQbjwN3wJSCj.jpg',
                'poster_path': '/yDWJYRAwMNKbIYT8ZB33qy84uzO.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/95557',
                'runtime': None
            }, {
                'code': 80240,
                'title': 'The Queen of Flow',
                'genres': None,
                'overview':
                'After spending seventeen years in prison unfairly, a talented songwriter seeks revenge on the men who sank her and killed her family.',
                'popularity': 585.628,
                'rating_average': 8,
                'rating_count': 809,
                'first_air_date': '2018-06-12',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/pnyT1foDmmXTsho2DfxN2ePI8ix.jpg',
                'poster_path': '/fuVuDYrs8sxvEolnYr0wCSvtyTi.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/80240',
                'runtime': None
            }, {
                'code': 62286,
                'title': 'Fear the Walking Dead',
                'genres': None,
                'overview':
                'What did the world look like as it was transforming into the horrifying apocalypse depicted in "The Walking Dead"? This spin-off set in Los Angeles, following new characters as they face the beginning of the end of the world, will answer that question.',
                'popularity': 499.94,
                'rating_average': 7.6,
                'rating_count': 3587,
                'first_air_date': '2015-08-23',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/58PON1OrnBiX6CqEHgeWKVwrCn6.jpg',
                'poster_path': '/4UjiPdFKJGJYdxwRs2Rzg7EmWqr.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/62286',
                'runtime': None
            }, {
                'code': 69050,
                'title': 'Riverdale',
                'genres': None,
                'overview':
                'Set in the present, the series offers a bold, subversive take on Archie, Betty, Veronica and their friends, exploring the surreality of small-town life, the darkness and weirdness bubbling beneath Riverdale’s wholesome facade.',
                'popularity': 496.441,
                'rating_average': 8.6,
                'rating_count': 11367,
                'first_air_date': '2017-01-26',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/qZtAf4Z1lazGQoYVXiHOrvLr5lI.jpg',
                'poster_path': '/wRbjVBdDo5qHAEOVYoMWpM58FSA.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/69050',
                'runtime': None
            }, {
                'code': 1399,
                'title': 'Game of Thrones',
                'genres': None,
                'overview':
                "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
                'popularity': 485.212,
                'rating_average': 8.4,
                'rating_count': 14592,
                'first_air_date': '2011-04-17',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/suopoADq0k8YZr4dQXcU6pToj6s.jpg',
                'poster_path': '/u3bZgnGQ9T01sWNhyveQz0wH0Hl.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/1399',
                'runtime': None
            }, {
                'code': 69478,
                'title': "The Handmaid's Tale",
                'genres': None,
                'overview':
                "Set in a dystopian future, a woman is forced to live as a concubine under a fundamentalist theocratic dictatorship. A TV adaptation of Margaret Atwood's novel.",
                'popularity': 469.53,
                'rating_average': 8.2,
                'rating_count': 1405,
                'first_air_date': '2017-04-26',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/jXB3OoWPkojsOP2O2OoLCeAIDRS.jpg',
                'poster_path': '/oIkxqt6ug5zT5ZSUUyc1Iqopf02.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/69478',
                'runtime': None
            }, {
                'code': 93484,
                'title': "Jupiter's Legacy",
                'genres': None,
                'overview':
                "As the world's first generation of superheroes (who received their powers in the 1930s) become the revered elder guard in the present, their superpowered children struggle to live up to the legendary feats of their parents.",
                'popularity': 439.21,
                'rating_average': 7.5,
                'rating_count': 290,
                'first_air_date': '2021-05-07',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/4YKkS95v9o9c0tBVA46xIn6M1tx.jpg',
                'poster_path': '/9yxep7oJdkj3Pla9TD9gKflRApY.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/93484',
                'runtime': None
            }, {
                'code': 1402,
                'title': 'The Walking Dead',
                'genres': None,
                'overview':
                "Sheriff's deputy Rick Grimes awakens from a coma to find a post-apocalyptic world dominated by flesh-eating zombies. He sets out to find his family and encounters many other survivors along the way.",
                'popularity': 436.463,
                'rating_average': 8.1,
                'rating_count': 10891,
                'first_air_date': '2010-10-31',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/uro2Khv7JxlzXtLb8tCIbRhkb9E.jpg',
                'poster_path': '/rqeYMLryjcawh2JeRpCVUDXYM5b.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/1402',
                'runtime': None
            }, {
                'code': 18165,
                'title': 'The Vampire Diaries',
                'genres': None,
                'overview':
                'The story of two vampire brothers obsessed with the same girl, who bears a striking resemblance to the beautiful but ruthless vampire they knew and loved in 1864.',
                'popularity': 418.904,
                'rating_average': 8.3,
                'rating_count': 5967,
                'first_air_date': '2009-09-10',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/k7T9xRyzP41wBVNyNeLmh8Ch7gD.jpg',
                'poster_path': '/kLEha9zVVv8acGFKTX4gjvSR2Q0.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/18165',
                'runtime': None
            }, {
                'code': 79008,
                'title': 'Luis Miguel: The Series',
                'genres': None,
                'overview':
                'The series dramatizes the life story of Mexican superstar singer Luis Miguel, who has captivated audiences in Latin America and beyond for decades.',
                'popularity': 415.006,
                'rating_average': 8,
                'rating_count': 453,
                'first_air_date': '2018-04-22',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/wkyzeBBKLhSg1Oqhky5yoiFF2hG.jpg',
                'poster_path': '/34FaY8qpjBAVysSfrJ1l7nrAQaD.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/79008',
                'runtime': None
            }, {
                'code': 79460,
                'title': 'Legacies',
                'genres': None,
                'overview':
                'In a place where young witches, vampires, and werewolves are nurtured to be their best selves in spite of their worst impulses, Klaus Mikaelson’s daughter, 17-year-old Hope Mikaelson, Alaric Saltzman’s twins, Lizzie and Josie Saltzman, among others, come of age into heroes and villains at The Salvatore School for the Young and Gifted.',
                'popularity': 396.064,
                'rating_average': 8.6,
                'rating_count': 1908,
                'first_air_date': '2018-10-25',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/fRYwdeNjMqC30EhofPx5PlDpdun.jpg',
                'poster_path': '/qTZIgXrBKURBK1KrsT7fe3qwtl9.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/79460',
                'runtime': None
            }, {
                'code': 105971,
                'title': 'The Bad Batch',
                'genres': None,
                'overview':
                'Follow the elite and experimental Clones of the Bad Batch as they find their way in a rapidly changing galaxy in the aftermath of the Clone Wars.',
                'popularity': 386.457,
                'rating_average': 8.7,
                'rating_count': 246,
                'first_air_date': '2021-05-04',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/sjxtIUCWR74yPPcZFfTsToepfWm.jpg',
                'poster_path': '/WjQmEWFrOf98nT5aEfUfVYz9N2.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/105971',
                'runtime': None
            }]
        }

    def get_movies_by_rating(self: object, user: str,
                             vote_avg: float, votes: int, released_from: str,
                             page: int) -> dict:
        return {
            'total_pages':
            5,
            'results': [{
                'code': 337404,
                'title': 'Cruella',
                'genres': None,
                'overview':
                'In 1970s London amidst the punk rock revolution, a young grifter named Estella is determined to make a name for herself with her designs. She befriends a pair of young thieves who appreciate her appetite for mischief, and together they are able to build a life for themselves on the London streets. One day, Estella’s flair for fashion catches the eye of the Baroness von Hellman, a fashion legend who is devastatingly chic and terrifyingly haute. But their relationship sets in motion a course of events and revelations that will cause Estella to embrace her wicked side and become the raucous, fashionable and revenge-bent Cruella.',
                'popularity': 6821.402,
                'rating_average': 8.8,
                'rating_count': 1560,
                'release_date': '2021-05-27',
                'runtime': None,
                'status': None,
                'backdrop_path': '/6MKr3KgOLmzOP6MSuZERO41Lpkt.jpg',
                'poster_path': '/A0knvX7rlwTyZSKj8H5NiARb45.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/337404'
            }, {
                'code': 663558,
                'title': 'New Gods: Nezha Reborn',
                'genres': None,
                'overview':
                '3000 years after the boy-god Nezha conquers the Dragon King then disappears in mythological times, he returns as an ordinary man to find his own path to becoming a true hero.',
                'popularity': 408.949,
                'rating_average': 8.6,
                'rating_count': 169,
                'release_date': '2021-04-12',
                'runtime': None,
                'status': None,
                'backdrop_path': '/y0SiXoTLQp93NbLQ4XhgVz18UAS.jpg',
                'poster_path': '/6goDkAD6J3br81YMQf0Gat8Bqjy.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/663558'
            }, {
                'code': 791373,
                'title': "Zack Snyder's Justice League",
                'genres': None,
                'overview':
                "Determined to ensure Superman's ultimate sacrifice was not in vain, Bruce Wayne aligns forces with Diana Prince with plans to recruit a team of metahumans to protect the world from an approaching threat of catastrophic proportions.",
                'popularity': 907.096,
                'rating_average': 8.5,
                'rating_count': 5661,
                'release_date': '2021-03-18',
                'runtime': None,
                'status': None,
                'backdrop_path': '/pcDc2WJAYGJTTvRSEIpRZwM3Ola.jpg',
                'poster_path': '/tnAuB8q5vv7Ax9UAEje5Xi4BXik.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/791373'
            }, {
                'code': 615457,
                'title': 'Nobody',
                'genres': None,
                'overview':
                'Hutch Mansell, a suburban dad, overlooked husband, nothing neighbor — a "nobody." When two thieves break into his home one night, Hutch\'s unknown long-simmering rage is ignited and propels him on a brutal path that will uncover dark secrets he fought to leave behind.',
                'popularity': 1048.459,
                'rating_average': 8.5,
                'rating_count': 1804,
                'release_date': '2021-06-10',
                'runtime': None,
                'status': None,
                'backdrop_path': '/6zbKgwgaaCyyBXE4Sun4oWQfQmi.jpg',
                'poster_path': '/oBgWY00bEFeZ9N25wWVyuQddbAo.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/615457'
            }, {
                'code': 423108,
                'title': 'The Conjuring: The Devil Made Me Do It',
                'genres': None,
                'overview':
                "Paranormal investigators Ed and Lorraine Warren encounter what would become one of the most sensational cases from their files. The fight for the soul of a young boy takes them beyond anything they'd ever seen before, to mark the first time in U.S. history that a murder suspect would claim demonic possession as a defense.",
                'popularity': 300.334,
                'rating_average': 7.8,
                'rating_count': 34,
                'release_date': '2021-07-01',
                'runtime': None,
                'status': None,
                'backdrop_path': '/gr2bdQ12cK4VA7EaIgtmDcbdALP.jpg',
                'poster_path': '/isghxwTkgHsSfoEmXK1QZEYTjUl.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/423108'
            }, {
                'code': 385128,
                'title': 'F9',
                'genres': None,
                'overview':
                'Dom Toretto is leading a quiet life off the grid with Letty and his son, little Brian, but little do they know, is that danger always lurks just over their peaceful horizon. This time, that threat will force Dom to confront the sins of his past if he’s going to save those he loves most. His crew joins together to stop a world-shattering plot led by the most skilled assassin and high-performance driver they’ve ever encountered: a man who also happens to be Dom’s forsaken brother, Jakob.',
                'popularity': 489.72,
                'rating_average': 8.3,
                'rating_count': 82,
                'release_date': '2021-07-08',
                'runtime': None,
                'status': None,
                'backdrop_path': '/xXHZeb1yhJvnSHPzZDqee0zfMb6.jpg',
                'poster_path': '/bOFaAXmWWXC3Rbv4u4uM9ZSzRXP.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/385128'
            }, {
                'code': 785534,
                'title': 'Paper Lives',
                'genres': None,
                'overview':
                'In the streets of Istanbul, ailing waste warehouse worker Mehmet takes a small boy under his wing and must soon confront his own traumatic childhood.',
                'popularity': 75.203,
                'rating_average': 8.3,
                'rating_count': 216,
                'release_date': '2021-03-12',
                'runtime': None,
                'status': None,
                'backdrop_path': '/ctckqAvz9aTZDtfXLmDUdMflesU.jpg',
                'poster_path': '/cmru6N6Hnw2pJwuo1ctH1CxKqKZ.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/785534'
            }, {
                'code': 527774,
                'title': 'Raya and the Last Dragon',
                'genres': None,
                'overview':
                'Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.',
                'popularity': 1055.191,
                'rating_average': 8.2,
                'rating_count': 3001,
                'release_date': '2021-03-05',
                'runtime': None,
                'status': None,
                'backdrop_path': '/hJuDvwzS0SPlsE6MNFOpznQltDZ.jpg',
                'poster_path': '/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/527774'
            }, {
                'code': 399566,
                'title': 'Godzilla vs. Kong',
                'genres': None,
                'overview':
                'In a time when monsters walk the Earth, humanity’s fight for its future sets Godzilla and Kong on a collision course that will see the two most powerful forces of nature on the planet collide in a spectacular battle for the ages.',
                'popularity': 1399.418,
                'rating_average': 8.1,
                'rating_count': 5808,
                'release_date': '2021-03-25',
                'runtime': None,
                'status': None,
                'backdrop_path': '/inJjDhCjfhh3RtrJWBmmDqeuSYC.jpg',
                'poster_path': '/pgqgaUx1cJb5oZQQ5v0tNARCeBp.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/399566'
            }, {
                'code': 458220,
                'title': 'Palmer',
                'genres': None,
                'overview':
                "After 12 years in prison, former high school football star Eddie Palmer returns home to put his life back together—and forms an unlikely bond with Sam, an outcast boy from a troubled home. But Eddie's past threatens to ruin his new life and family.",
                'popularity': 61.618,
                'rating_average': 8,
                'rating_count': 473,
                'release_date': '2021-01-29',
                'runtime': None,
                'status': None,
                'backdrop_path': '/bblKpucB0XbyQBmfXsaRN985Rgh.jpg',
                'poster_path': '/xSDdRAjxKAGi8fUBLOqSrBhJmF0.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/458220'
            }, {
                'code': 501929,
                'title': 'The Mitchells vs. the Machines',
                'genres': None,
                'overview':
                "A quirky, dysfunctional family's road trip is upended when they find themselves in the middle of the robot apocalypse and suddenly become humanity's unlikeliest last hope.",
                'popularity': 121.52,
                'rating_average': 8,
                'rating_count': 859,
                'release_date': '2021-04-30',
                'runtime': None,
                'status': None,
                'backdrop_path': '/qXMXmhsJeW28DYp5iOar9BGepVS.jpg',
                'poster_path': '/mI2Di7HmskQQ34kz0iau6J1vr70.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/501929'
            }, {
                'code': 637649,
                'title': 'Wrath of Man',
                'genres': None,
                'overview':
                "A cold and mysterious new security guard for a Los Angeles cash truck company surprises his co-workers when he unleashes precision skills during a heist. The crew is left wondering who he is and where he came from. Soon, the marksman's ultimate motive becomes clear as he takes dramatic and irrevocable steps to settle a score.",
                'popularity': 3381.321,
                'rating_average': 8,
                'rating_count': 606,
                'release_date': '2021-05-20',
                'runtime': None,
                'status': None,
                'backdrop_path': '/77tui163estZrQ78NBggqDB4n2C.jpg',
                'poster_path': '/YxopfHpsCV1oF8CZaL4M3Eodqa.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/637649'
            }, {
                'code': 736069,
                'title': 'Justice Society: World War II',
                'genres': None,
                'overview':
                'While speeding off to help in an impromptu battle, The Flash blazes and rips through time, only to find himself dropped into the middle of World War II. It’s here that The Flash meets Wonder Woman and her top secret team, known as the Justice Society of America. Amidst the raging tides of war, gripping combat and the velocity of valor, The Flash must fight to return to his own timeline.',
                'popularity': 372.224,
                'rating_average': 7.9,
                'rating_count': 218,
                'release_date': '2021-04-27',
                'runtime': None,
                'status': None,
                'backdrop_path': '/8LHSDyRizQ4kQz5rEHPKyXPvMG3.jpg',
                'poster_path': '/e4REOC6CZW8J6FslA4nRvdQXFXR.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/736069'
            }, {
                'code': 726684,
                'title':
                'Miraculous World: Shanghai – The Legend of Ladydragon',
                'genres': None,
                'overview':
                'On school break, Marinette heads to Shanghai to meet Adrien. But after arriving, Marinette loses all her stuff, including the Miraculous that allows her to turn into Ladybug!',
                'popularity': 964.043,
                'rating_average': 7.9,
                'rating_count': 375,
                'release_date': '2021-05-23',
                'runtime': None,
                'status': None,
                'backdrop_path': '/rlNnwObbMu5G2FaOUlacnUIdIIA.jpg',
                'poster_path': '/msI5a9TPnepx47JUb2vl88hb80R.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/726684'
            }, {
                'code': 586047,
                'title': 'Seobok',
                'genres': None,
                'overview':
                'A former intelligence agent gets involved with the first human clone, Seo Bok, who others seek, causing trouble.',
                'popularity': 745.953,
                'rating_average': 7.7,
                'rating_count': 54,
                'release_date': '2021-07-23',
                'runtime': None,
                'status': None,
                'backdrop_path': '/yC4DRg5aGgNpkHpUDpLtBqzownS.jpg',
                'poster_path': '/nxxuWC32Y6TULj4VnVwMPUFLIpK.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/586047'
            }, {
                'code': 809236,
                'title': 'Have You Ever Seen Fireflies?',
                'genres': None,
                'overview':
                'Rebellious, irreverent wunderkind Gülseren navigates loneliness, love and loss against the current of political turmoil and social change.',
                'popularity': 2.908,
                'rating_average': 7.6,
                'rating_count': 15,
                'release_date': '2021-04-09',
                'runtime': None,
                'status': None,
                'backdrop_path': '/lVhSW3OcQ6Z6M4f4yMhrlHgPzc1.jpg',
                'poster_path': '/lZucbxHPkb5Xla5ivOcKim7A1NO.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/809236'
            }, {
                'code': 460465,
                'title': 'Mortal Kombat',
                'genres': None,
                'overview':
                "Washed-up MMA fighter Cole Young, unaware of his heritage, and hunted by Emperor Shang Tsung's best warrior, Sub-Zero, seeks out and trains with Earth's greatest champions as he prepares to stand against the enemies of Outworld in a high stakes battle for the universe.",
                'popularity': 1641.256,
                'rating_average': 7.6,
                'rating_count': 2837,
                'release_date': '2021-05-06',
                'runtime': None,
                'status': None,
                'backdrop_path': '/mPBI506o7gITnjoSkcyPneK9s8n.jpg',
                'poster_path': '/nkayOAUBUu4mMvyNf9iHSUiPjF1.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/460465'
            }, {
                'code': 773736,
                'title': 'TINA',
                'genres': None,
                'overview':
                'Tina Turner overcame impossible odds to become one of the first female African American artists to reach a mainstream international audience. Her road to superstardom is an undeniable story of triumph over adversity. It’s the ultimate story of survival – and an inspirational story of our times.',
                'popularity': 15.184,
                'rating_average': 7.6,
                'rating_count': 26,
                'release_date': '2021-03-02',
                'runtime': None,
                'status': None,
                'backdrop_path': '/rv3bNtqYpARfJNPFctMeZrxq6bL.jpg',
                'poster_path': '/bL2FNPhiPqDyirzU3rfaXDiWRXs.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/773736'
            }, {
                'code': 583689,
                'title': 'Moxie',
                'genres': None,
                'overview':
                "Inspired by her mom's rebellious past and a confident new friend, a shy 16-year-old publishes an anonymous zine calling out sexism at her school.",
                'popularity': 74.43,
                'rating_average': 7.5,
                'rating_count': 463,
                'release_date': '2021-03-03',
                'runtime': None,
                'status': None,
                'backdrop_path': '/aKIrKbszS7Kq0aTGTCRTYMp1EDX.jpg',
                'poster_path': '/aLBo1Ca9PggcWY98ItW5ZkdxTuA.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/583689'
            }, {
                'code': 785976,
                'title': 'Pelé',
                'genres': None,
                'overview':
                "Against the backdrop of a turbulent era in Brazil, this documentary captures Pelé's extraordinary path from breakthrough talent to national hero. Mixing rare archival footage and exclusive interviews, this documentary celebrates the legendary Brazilian footballer who personified football as art.",
                'popularity': 30.496,
                'rating_average': 7.5,
                'rating_count': 89,
                'release_date': '2021-02-23',
                'runtime': None,
                'status': None,
                'backdrop_path': '/t0kHIE4ERtw3h4qwTSmzt5LyhRY.jpg',
                'poster_path': '/tX2gco2U4MlKEWwM4UkiIf1C74e.jpg',
                'providers': None,
                'cast': None,
                'directors': None,
                'tmdb_url': 'https://www.themoviedb.org/movie/785976'
            }]
        }

    def get_tv_by_rating(self: object, user: str,
                         vote_avg: float, votes: int, released_from: str,
                         page: int) -> dict:
        return {
            'total_pages':
            7,
            'results': [{
                'code': 115194,
                'title': 'A Perfect Planet',
                'genres': None,
                'overview':
                'A unique fusion of blue chip natural history and earth science that explains how our living planet operates. This five-part series shows how the forces of nature drive, shape and support Earth’s great diversity of wildlife.',
                'popularity': 35.725,
                'rating_average': 9.5,
                'rating_count': 14,
                'first_air_date': '2021-01-03',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/59amxr7vKdeaWfv09y8UG8yZ6v.jpg',
                'poster_path': '/8JJa4gduVytwpXQzFtZNibRA6S.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/115194',
                'runtime': None
            }, {
                'code': 114547,
                'title': 'Secrets of Sulphur Springs',
                'genres': None,
                'overview':
                '12-year-old Griffin Campbell and his family move to the small town of Sulphur Springs and take ownership of an abandoned hotel rumored to be haunted by the ghost of a girl who disappeared decades ago. Griffin befriends Harper, a bright-eyed, mystery-obsessed classmate and together, they uncover a secret portal that allows them to travel back in time. In the past, they’ll attempt to uncover the key to solving this unsolved mystery, a mystery that affects everyone close to them.',
                'popularity': 10.137,
                'rating_average': 9.1,
                'rating_count': 17,
                'first_air_date': '2021-01-15',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/5zTeE4HqzzhN3w6FgyfVMPgtkqc.jpg',
                'poster_path': '/30MqitTOgIfeOhvwdMHkrM9p5mD.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/114547',
                'runtime': None
            }, {
                'code': 110309,
                'title': 'SK8 the Infinity',
                'genres': None,
                'overview':
                '"S" is a dangerous, top secret, no-holds-barred downhill skateboarding race down an abandoned mine. When avid skateboarder Reki takes Langa to the mountain where "S" is held, Langa, who’s never been on a skateboard in his life, finds himself sucked into the world of "S" and...?!',
                'popularity': 57.449,
                'rating_average': 9.2,
                'rating_count': 10,
                'first_air_date': '2021-01-10',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/ohOrfdh80HVY5QBD8kV2FYYSVwF.jpg',
                'poster_path': '/ksb6QlSCsRLr3MNmxc8ojOOLK6V.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/110309',
                'runtime': None
            }, {
                'code': 116386,
                'title': 'Doom at Your Service',
                'genres': None,
                'overview':
                'Dong-kyung has been working hard ever since her parents passed away. Her life seems to get stable after working as an web novel editor for 6 years, but one day she gets diagnosed with a brain cancer. She blames her unlucky life and wishes to curse everything to disappear, which unintentionally calls Myul Mang, a messenger between humans and gods, to appear. He says that he can grant her wishes. As her last hope, she makes a contract with Myul Mang for hundred days to live as how she wants, risking her everything.',
                'popularity': 19.571,
                'rating_average': 9,
                'rating_count': 11,
                'first_air_date': '2021-05-10',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/uMLihaxfbeCvraDmER37t2jTNKi.jpg',
                'poster_path': '/tgsWD4dJI5YFY8Kyk6vVjZoIKfO.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/116386',
                'runtime': None
            }, {
                'code': 121509,
                'title': 'The Upshaws',
                'genres': None,
                'overview':
                'Bennie Upshaw, the head of a Black working class family in Indianapolis, is a charming, well-intentioned mechanic and lifelong mess just trying his best to step up and care for his family and tolerate his sardonic sister-in-law, all without a blueprint for success.',
                'popularity': 5.407,
                'rating_average': 8.9,
                'rating_count': 10,
                'first_air_date': '2021-05-12',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/2etWIt4JMD4wHzJIZVi7YeI5UZa.jpg',
                'poster_path': '/bgtpwAsKNfqJmgp3zBxuSHMBAaW.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/121509',
                'runtime': None
            }, {
                'code': 95557,
                'title': 'Invincible',
                'genres': None,
                'overview':
                'Mark Grayson is a normal teenager except for the fact that his father is the most powerful superhero on the planet. Shortly after his seventeenth birthday, Mark begins to develop powers of his own and enters into his father’s tutelage.',
                'popularity': 599.292,
                'rating_average': 8.9,
                'rating_count': 1934,
                'first_air_date': '2021-03-26',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/6UH52Fmau8RPsMAbQbjwN3wJSCj.jpg',
                'poster_path': '/yDWJYRAwMNKbIYT8ZB33qy84uzO.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/95557',
                'runtime': None
            }, {
                'code': 99071,
                'title': 'Redo of Healer',
                'genres': None,
                'overview':
                'In a world of monsters, adventurers and magic, some of the most gifted healers are subjugated to brute force. Keyaru gains the ability to rewind time and turns the tables on those who’ve exploited him in this dark fantasy tale of vengeance and fury.',
                'popularity': 65.563,
                'rating_average': 8.8,
                'rating_count': 363,
                'first_air_date': '2021-01-13',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/e30T3teKp6VZlIXhI0AhTDksvoy.jpg',
                'poster_path': '/hynFI7MltF1BBvroh3iJplnBZyc.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/99071',
                'runtime': None
            }, {
                'code': 117376,
                'title': 'Vincenzo',
                'genres': None,
                'overview':
                'Vincenzo Cassano is an Italian lawyer and Mafia consigliere who moves back to Korea due to a conflict within his organization. He ends up crossing paths with a sharp-tongued lawyer named Cha-young, and the two join forces in using villainous methods to take down villains who cannot be punished by the law.',
                'popularity': 98.999,
                'rating_average': 8.8,
                'rating_count': 169,
                'first_air_date': '2021-02-20',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/sf7NCqyVUNoyjYuwW5oJke1T1lH.jpg',
                'poster_path': '/dvXJgEDQXhL9Ouot2WkBHpQiHGd.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/117376',
                'runtime': None
            }, {
                'code': 116249,
                'title': 'Kid Cosmic',
                'genres': None,
                'overview':
                "A boy's superhero dreams come true when he finds five powerful cosmic stones. But saving the day is harder than he imagined — and he can't do it alone.",
                'popularity': 21.83,
                'rating_average': 8.8,
                'rating_count': 33,
                'first_air_date': '2021-02-02',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/3twr9PEWUxb6FHVZ8hzOaBpSh8u.jpg',
                'poster_path': '/88HdcCMumGqGAt2kR3vVOr8NYiA.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/116249',
                'runtime': None
            }, {
                'code': 95205,
                'title': 'The Equalizer',
                'genres': None,
                'overview':
                'Robyn McCall, an enigmatic former CIA operative with a mysterious background, uses her extensive skills to help those with nowhere else to turn.',
                'popularity': 11.024,
                'rating_average': 8.7,
                'rating_count': 57,
                'first_air_date': '2021-02-07',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/3C032MHjf4sXV3XpmvRLbsibAmZ.jpg',
                'poster_path': '/gAgShytJMWSYkjxa7ZDjSZhsnlc.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/95205',
                'runtime': None
            }, {
                'code': 105971,
                'title': 'The Bad Batch',
                'genres': None,
                'overview':
                'Follow the elite and experimental Clones of the Bad Batch as they find their way in a rapidly changing galaxy in the aftermath of the Clone Wars.',
                'popularity': 386.457,
                'rating_average': 8.7,
                'rating_count': 246,
                'first_air_date': '2021-05-04',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/sjxtIUCWR74yPPcZFfTsToepfWm.jpg',
                'poster_path': '/WjQmEWFrOf98nT5aEfUfVYz9N2.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/105971',
                'runtime': None
            }, {
                'code': 110070,
                'title': 'Horimiya',
                'genres': None,
                'overview':
                'A secret life is the one thing they have in common. At school, Hori is a prim and perfect social butterfly, but the truth is she’s a brash homebody. Meanwhile, under a gloomy facade, Miyamura hides a gentle heart, along with piercings and tattoos. In a chance meeting, they both reveal a side they’ve never shown. Could this blossom into something new?',
                'popularity': 102.268,
                'rating_average': 8.7,
                'rating_count': 204,
                'first_air_date': '2021-01-10',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/4u64tHtUkna1y4OkJcrXLEhhLLy.jpg',
                'poster_path': '/917VL7zHTaltnEBDrKWVITTsvLy.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/110070',
                'runtime': None
            }, {
                'code': 105009,
                'title': 'Tokyo Revengers',
                'genres': None,
                'overview':
                'Takemichi Hanagaki is a freelancer that’s reached the absolute pits of despair in his life. He finds out that the only girlfriend he ever had, in middle school, Hinata Tachibana, had been killed by the ruthless Tokyo Manji Gang. The day after hearing about her death, he’s standing on the station platform and ends up being pushed over onto the tracks by a herd of people. He closes his eyes thinking he’s about to die, but when he opens his eyes back up, he somehow had gone back in time 12 years. Now that he’s back living the best days of his life, Takemichi decides to get revenge on his life.',
                'popularity': 156.682,
                'rating_average': 8.7,
                'rating_count': 11,
                'first_air_date': '2021-04-11',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/wjw3wrmkjjApu83Y4SxmQ5gP2mZ.jpg',
                'poster_path': '/qSEKyf0fWhrCEQ3LTwLqe41eSvR.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/105009',
                'runtime': None
            }, {
                'code': 112160,
                'title': 'The Way of the Househusband',
                'genres': None,
                'overview':
                'Tatsu, a notorious and feared yakuza leader nicknamed "The Immortal Dragon," withdraws from the criminal syndicate and becomes a housekeeper to help his wife, Miku. The series features a variety of comedic settings, typically showing Tatsu\'s domestic activities and intimidating inequality with his looks, as well as multiple encounters with his former colleagues and rivals in the Japanese Criminal Syndicate.',
                'popularity': 18.938,
                'rating_average': 8.6,
                'rating_count': 129,
                'first_air_date': '2021-04-08',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/3bC5QIJ3P1ebC7PKwzUVfgub8I.jpg',
                'poster_path': '/p63rAZt0s8kedJtdxGwD5VYZafc.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/112160',
                'runtime': None
            }, {
                'code': 106158,
                'title': 'Law & Order: Organized Crime',
                'genres': None,
                'overview':
                'Detective Elliot Stabler returns to the NYPD to battle organized crime after a devastating personal loss. The city and police department have changed dramatically in the decade he’s been away, and he must adapt to a criminal justice system in the midst of its own moment of reckoning. Stabler journeys to find absolution and rebuild his life, while leading a new elite task force that is taking apart the city’s most powerful criminal syndicates one by one.',
                'popularity': 14.692,
                'rating_average': 8.6,
                'rating_count': 15,
                'first_air_date': '2021-04-01',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/tjogqNxMYdXb7UMr4DofAAUdzyb.jpg',
                'poster_path': '/ur8ZV6Dn4FzsU2zIQK7iDQKZcTE.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/106158',
                'runtime': None
            }, {
                'code': 120462,
                'title': 'THEM',
                'genres': None,
                'overview':
                'A limited anthology series that explores terror in America.',
                'popularity': 12.714,
                'rating_average': 8.5,
                'rating_count': 35,
                'first_air_date': '2021-04-09',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/nRifrfdncHTRKUbk0MrAcuQmDFN.jpg',
                'poster_path': '/bJw1VZ4ACt5TnAvJbHcprzgYc1E.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/120462',
                'runtime': None
            }, {
                'code': 112162,
                'title': 'Pacific Rim: The Black',
                'genres': None,
                'overview':
                'Two siblings - an idealistic teenage boy and his naïve younger sister - are forced to pilot an abandoned Jaeger across a hostile landscape in a desperate attempt to find their missing parents.',
                'popularity': 44.881,
                'rating_average': 8.5,
                'rating_count': 193,
                'first_air_date': '2021-03-04',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/o56X5GUWgzkGJ90QDWn6NNkGEN7.jpg',
                'poster_path': '/s3mOpPwrcKCPVkSWGqEwOah4jdX.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/112162',
                'runtime': None
            }, {
                'code': 112163,
                'title': 'High-Rise Invasion',
                'genres': None,
                'overview':
                "High-school girl Yuri suddenly finds herself on the rooftop of a high-rise building. She's trapped in a bizarre world surrounded by skyscrapers, where a masked man cracked open a man's head with an axe before her eyes. Finding a way to survive this bizarre world, find her beloved brother, and escape becomes her top priority, but she is beset by danger not just from the mysterious Masks, which possess both inhuman strength and cruelty, but other survivors turned cruel or desparate by the insanity of the high-rise world.",
                'popularity': 63.022,
                'rating_average': 8.5,
                'rating_count': 348,
                'first_air_date': '2021-02-25',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/cT0o6RFi36TkMFG1wWyTyGb2jrR.jpg',
                'poster_path': '/5uXaWe0LXTpBQVBBXL1ynae1DED.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/112163',
                'runtime': None
            }, {
                'code': 116174,
                'title': "It's a Sin",
                'genres': None,
                'overview':
                'A chronicle of five friends during a decade in which everything changed, including the rise of AIDS.',
                'popularity': 27.236,
                'rating_average': 8.5,
                'rating_count': 33,
                'first_air_date': '2021-01-22',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/aveywEVwIppkrHRQavbB4ybnZPe.jpg',
                'poster_path': '/hkoQ9Ut0mmQC8BmlScrGD78PlXw.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/116174',
                'runtime': None
            }, {
                'code': 80828,
                'title': 'The Nevers',
                'genres': None,
                'overview':
                'In the last years of Victoria\'s reign, London is beset by the "Touched": people — mostly women — who suddenly manifest abnormal abilities, some charming, some very disturbing. Among them are Amalia True, a mysterious, quick-fisted widow, and Penance Adair, a brilliant young inventor. They are the champions of this new underclass, making a home for the Touched, while fighting the forces of… well, pretty much all the forces — to make room for those whom history as we know it has no place.',
                'popularity': 65.552,
                'rating_average': 8.5,
                'rating_count': 321,
                'first_air_date': '2021-04-11',
                'last_air_date': None,
                'status': None,
                'backdrop_path': '/6x8vW5utEZahp6V3sSWxCTW0mHW.jpg',
                'poster_path': '/v6Xmj8Fy7ZruVTz3y2Po7O0TQh4.jpg',
                'providers': None,
                'creators': None,
                'cast': None,
                'number_of_episodes': None,
                'number_of_seasons': None,
                'tmdb_url': 'https://www.themoviedb.org/tv/80828',
                'runtime': None
            }]
        }
