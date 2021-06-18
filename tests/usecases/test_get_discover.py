from consumatio.usecases.get_discover import get_discover
from consumatio.external.db.models import *
from tests.utils.setup_app import setup_app


def test_get_discover_movie():
    tmdb = setup_app()[0]

    dict = {
        'results': [{
            '__typename':
            'Movie',
            'backdrop_path':
            '/6MKr3KgOLmzOP6MSuZERO41Lpkt.jpg',
            'cast':
            None,
            'code':
            337404,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'In 1970s London amidst the punk rock revolution, a '
            'young grifter named Estella is determined to make a '
            'name for herself with her designs. She befriends a '
            'pair of young thieves who appreciate her appetite '
            'for mischief, and together they are able to build a '
            'life for themselves on the London streets. One day, '
            'Estella’s flair for fashion catches the eye of the '
            'Baroness von Hellman, a fashion legend who is '
            'devastatingly chic and terrifyingly haute. But '
            'their relationship sets in motion a course of '
            'events and revelations that will cause Estella to '
            'embrace her wicked side and become the raucous, '
            'fashionable and revenge-bent Cruella.',
            'popularity':
            6821.402,
            'poster_path':
            '/A0knvX7rlwTyZSKj8H5NiARb45.jpg',
            'providers':
            None,
            'rating_average':
            8.8,
            'rating_count':
            1560,
            'rating_user':
            None,
            'release_date':
            '2021-05-27',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Cruella',
            'tmdb_url':
            'https://www.themoviedb.org/movie/337404',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/77tui163estZrQ78NBggqDB4n2C.jpg',
            'cast':
            None,
            'code':
            637649,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'A cold and mysterious new security guard for a Los '
            'Angeles cash truck company surprises his co-workers '
            'when he unleashes precision skills during a heist. '
            'The crew is left wondering who he is and where he '
            "came from. Soon, the marksman's ultimate motive "
            'becomes clear as he takes dramatic and irrevocable '
            'steps to settle a score.',
            'popularity':
            3381.321,
            'poster_path':
            '/YxopfHpsCV1oF8CZaL4M3Eodqa.jpg',
            'providers':
            None,
            'rating_average':
            8,
            'rating_count':
            606,
            'rating_user':
            None,
            'release_date':
            '2021-05-20',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Wrath of Man',
            'tmdb_url':
            'https://www.themoviedb.org/movie/637649',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/9WlJFhOSCPnaaSmsrv0B4zA8iUb.jpg',
            'cast':
            None,
            'code':
            503736,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Following a zombie outbreak in Las Vegas, a group '
            'of mercenaries take the ultimate gamble: venturing '
            'into the quarantine zone to pull off the greatest '
            'heist ever attempted.',
            'popularity':
            2615.629,
            'poster_path':
            '/z8CExJekGrEThbpMXAmCFvvgoJR.jpg',
            'providers':
            None,
            'rating_average':
            6.6,
            'rating_count':
            1290,
            'rating_user':
            None,
            'release_date':
            '2021-05-21',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Army of the Dead',
            'tmdb_url':
            'https://www.themoviedb.org/movie/503736',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/mPBI506o7gITnjoSkcyPneK9s8n.jpg',
            'cast':
            None,
            'code':
            460465,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Washed-up MMA fighter Cole Young, unaware of his '
            "heritage, and hunted by Emperor Shang Tsung's best "
            'warrior, Sub-Zero, seeks out and trains with '
            "Earth's greatest champions as he prepares to stand "
            'against the enemies of Outworld in a high stakes '
            'battle for the universe.',
            'popularity':
            1641.256,
            'poster_path':
            '/nkayOAUBUu4mMvyNf9iHSUiPjF1.jpg',
            'providers':
            None,
            'rating_average':
            7.6,
            'rating_count':
            2837,
            'rating_user':
            None,
            'release_date':
            '2021-05-06',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Mortal Kombat',
            'tmdb_url':
            'https://www.themoviedb.org/movie/460465',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/fPGeS6jgdLovQAKunNHX8l0avCy.jpg',
            'cast':
            None,
            'code':
            567189,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'An elite Navy SEAL uncovers an international '
            'conspiracy while seeking justice for the murder of '
            'his pregnant wife.',
            'popularity':
            1361.356,
            'poster_path':
            '/rEm96ib0sPiZBADNKBHKBv5bve9.jpg',
            'providers':
            None,
            'rating_average':
            7.2,
            'rating_count':
            1087,
            'rating_user':
            None,
            'release_date':
            '2021-04-30',
            'runtime':
            None,
            'status':
            None,
            'title':
            "Tom Clancy's Without Remorse",
            'tmdb_url':
            'https://www.themoviedb.org/movie/567189',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/inJjDhCjfhh3RtrJWBmmDqeuSYC.jpg',
            'cast':
            None,
            'code':
            399566,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'In a time when monsters walk the Earth, humanity’s '
            'fight for its future sets Godzilla and Kong on a '
            'collision course that will see the two most '
            'powerful forces of nature on the planet collide in '
            'a spectacular battle for the ages.',
            'popularity':
            1399.418,
            'poster_path':
            '/pgqgaUx1cJb5oZQQ5v0tNARCeBp.jpg',
            'providers':
            None,
            'rating_average':
            8.1,
            'rating_count':
            5808,
            'rating_user':
            None,
            'release_date':
            '2021-03-25',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Godzilla vs. Kong',
            'tmdb_url':
            'https://www.themoviedb.org/movie/399566',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/iDdpiUnCeXvBmrkBFpL6lKsZt33.jpg',
            'cast':
            None,
            'code':
            578701,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'A young boy finds himself pursued by two assassins '
            'in the Montana wilderness with a survival expert '
            'determined to protecting him - and a forest fire '
            'threatening to consume them all.',
            'popularity':
            1243.188,
            'poster_path':
            '/xCEg6KowNISWvMh8GvPSxtdf9TO.jpg',
            'providers':
            None,
            'rating_average':
            7,
            'rating_count':
            374,
            'rating_user':
            None,
            'release_date':
            '2021-06-03',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Those Who Wish Me Dead',
            'tmdb_url':
            'https://www.themoviedb.org/movie/578701',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/hJuDvwzS0SPlsE6MNFOpznQltDZ.jpg',
            'cast':
            None,
            'code':
            527774,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Long ago, in the fantasy world of Kumandra, humans '
            'and dragons lived together in harmony. But when an '
            'evil force threatened the land, the dragons '
            'sacrificed themselves to save humanity. Now, 500 '
            'years later, that same evil has returned and it’s '
            'up to a lone warrior, Raya, to track down the '
            'legendary last dragon to restore the fractured land '
            'and its divided people.',
            'popularity':
            1055.191,
            'poster_path':
            '/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg',
            'providers':
            None,
            'rating_average':
            8.2,
            'rating_count':
            3001,
            'rating_user':
            None,
            'release_date':
            '2021-03-05',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Raya and the Last Dragon',
            'tmdb_url':
            'https://www.themoviedb.org/movie/527774',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/6zbKgwgaaCyyBXE4Sun4oWQfQmi.jpg',
            'cast':
            None,
            'code':
            615457,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Hutch Mansell, a suburban dad, overlooked husband, '
            'nothing neighbor — a "nobody." When two thieves '
            "break into his home one night, Hutch's unknown "
            'long-simmering rage is ignited and propels him on a '
            'brutal path that will uncover dark secrets he '
            'fought to leave behind.',
            'popularity':
            1048.459,
            'poster_path':
            '/oBgWY00bEFeZ9N25wWVyuQddbAo.jpg',
            'providers':
            None,
            'rating_average':
            8.5,
            'rating_count':
            1804,
            'rating_user':
            None,
            'release_date':
            '2021-06-10',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Nobody',
            'tmdb_url':
            'https://www.themoviedb.org/movie/615457',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/z2UtGA1WggESspi6KOXeo66lvLx.jpg',
            'cast':
            None,
            'code':
            520763,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Following the events at home, the Abbott family now '
            'face the terrors of the outside world. Forced to '
            'venture into the unknown, they realize that the '
            'creatures that hunt by sound are not the only '
            'threats that lurk beyond the sand path.',
            'popularity':
            1040.555,
            'poster_path':
            '/4q2hz2m8hubgvijz8Ez0T2Os2Yv.jpg',
            'providers':
            None,
            'rating_average':
            7.4,
            'rating_count':
            117,
            'rating_user':
            None,
            'release_date':
            '2021-06-24',
            'runtime':
            None,
            'status':
            None,
            'title':
            'A Quiet Place Part II',
            'tmdb_url':
            'https://www.themoviedb.org/movie/520763',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/rlNnwObbMu5G2FaOUlacnUIdIIA.jpg',
            'cast':
            None,
            'code':
            726684,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'On school break, Marinette heads to Shanghai to '
            'meet Adrien. But after arriving, Marinette loses '
            'all her stuff, including the Miraculous that allows '
            'her to turn into Ladybug!',
            'popularity':
            964.043,
            'poster_path':
            '/msI5a9TPnepx47JUb2vl88hb80R.jpg',
            'providers':
            None,
            'rating_average':
            7.9,
            'rating_count':
            375,
            'rating_user':
            None,
            'release_date':
            '2021-05-23',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Miraculous World: Shanghai – The Legend of Ladydragon',
            'tmdb_url':
            'https://www.themoviedb.org/movie/726684',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/xPpXYnCWfjkt3zzE0dpCNME1pXF.jpg',
            'cast':
            None,
            'code':
            635302,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Tanjirō Kamado, joined with Inosuke Hashibira, a '
            "boy raised by boars who wears a boar's head, and "
            'Zenitsu Agatsuma, a scared boy who reveals his true '
            'power when he sleeps, boards the Infinity Train on '
            'a new mission with the Fire Hashira, Kyōjurō '
            'Rengoku, to defeat a demon who has been tormenting '
            'the people and killing the demon slayers who oppose '
            'it!',
            'popularity':
            1011.75,
            'poster_path':
            '/h8Rb9gBr48ODIwYUttZNYeMWeUU.jpg',
            'providers':
            None,
            'rating_average':
            8.4,
            'rating_count':
            1110,
            'rating_user':
            None,
            'release_date':
            '2021-05-20',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train',
            'tmdb_url':
            'https://www.themoviedb.org/movie/635302',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/pcDc2WJAYGJTTvRSEIpRZwM3Ola.jpg',
            'cast':
            None,
            'code':
            791373,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            "Determined to ensure Superman's ultimate sacrifice "
            'was not in vain, Bruce Wayne aligns forces with '
            'Diana Prince with plans to recruit a team of '
            'metahumans to protect the world from an approaching '
            'threat of catastrophic proportions.',
            'popularity':
            907.096,
            'poster_path':
            '/tnAuB8q5vv7Ax9UAEje5Xi4BXik.jpg',
            'providers':
            None,
            'rating_average':
            8.5,
            'rating_count':
            5661,
            'rating_user':
            None,
            'release_date':
            '2021-03-18',
            'runtime':
            None,
            'status':
            None,
            'title':
            "Zack Snyder's Justice League",
            'tmdb_url':
            'https://www.themoviedb.org/movie/791373',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/n2y7T8wJVjJ8yLhQXQgNCpsC3ga.jpg',
            'cast':
            None,
            'code':
            811367,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Set before the events of ‘Soul’, 22 refuses to go '
            'to Earth, enlisting a gang of 5 new souls in '
            'attempt of rebellion. However, 22’s subversive plot '
            'leads to a surprising revelation about the meaning '
            'of life.',
            'popularity':
            725.881,
            'poster_path':
            '/32vLDKSzcCMh55zqqaSqqUA8naz.jpg',
            'providers':
            None,
            'rating_average':
            7.2,
            'rating_count':
            117,
            'rating_user':
            None,
            'release_date':
            '2021-04-30',
            'runtime':
            None,
            'status':
            None,
            'title':
            '22 vs. Earth',
            'tmdb_url':
            'https://www.themoviedb.org/movie/811367',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/yC4DRg5aGgNpkHpUDpLtBqzownS.jpg',
            'cast':
            None,
            'code':
            586047,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'A former intelligence agent gets involved with the '
            'first human clone, Seo Bok, who others seek, '
            'causing trouble.',
            'popularity':
            745.953,
            'poster_path':
            '/nxxuWC32Y6TULj4VnVwMPUFLIpK.jpg',
            'providers':
            None,
            'rating_average':
            7.7,
            'rating_count':
            54,
            'rating_user':
            None,
            'release_date':
            '2021-07-23',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Seobok',
            'tmdb_url':
            'https://www.themoviedb.org/movie/586047',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/sWHlCeJ2RunM5eq3FYA4VuTUNqY.jpg',
            'cast':
            None,
            'code':
            259693,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Lorraine and Ed Warren travel to north London to '
            'help a single mother raising four children alone in '
            'a house plagued by malicious spirits.',
            'popularity':
            919.148,
            'poster_path':
            '/zEqyD0SBt6HL7W9JQoWwtd5Do1T.jpg',
            'providers':
            None,
            'rating_average':
            7.2,
            'rating_count':
            5907,
            'rating_user':
            None,
            'release_date':
            '2016-06-16',
            'runtime':
            None,
            'status':
            None,
            'title':
            'The Conjuring 2',
            'tmdb_url':
            'https://www.themoviedb.org/movie/259693',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/czHYg6LQ5926OL8wj5kC09pNR12.jpg',
            'cast':
            None,
            'code':
            647302,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Jack, a man desperate to improve his life, throws '
            'away his beloved childhood plush, Benny. It’s a '
            'move that has disastrous consequences when Benny '
            'springs to life with deadly intentions!',
            'popularity':
            650.09,
            'poster_path':
            '/mQ8vALvqA0z0qglG3gI6xpVcslo.jpg',
            'providers':
            None,
            'rating_average':
            6.1,
            'rating_count':
            30,
            'rating_user':
            None,
            'release_date':
            '2021-07-16',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Benny Loves You',
            'tmdb_url':
            'https://www.themoviedb.org/movie/647302',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/jFINtstDUh0vHOGImpMAmLrPcXy.jpg',
            'cast':
            None,
            'code':
            643586,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'When his car breaks down, a quiet loner agrees to '
            'clean an abandoned family fun center in exchange '
            'for repairs. He soon finds himself waging war '
            'against possessed animatronic mascots while trapped '
            "inside Willy's Wonderland.",
            'popularity':
            584.484,
            'poster_path':
            '/keEnkeAvifw8NSEC4f6WsqeLJgF.jpg',
            'providers':
            None,
            'rating_average':
            6.7,
            'rating_count':
            235,
            'rating_user':
            None,
            'release_date':
            '2021-05-21',
            'runtime':
            None,
            'status':
            None,
            'title':
            "Willy's Wonderland",
            'tmdb_url':
            'https://www.themoviedb.org/movie/643586',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/l5yp73psXVRYy2ce09lD8yDuu2g.jpg',
            'cast':
            None,
            'code':
            138843,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Paranormal investigators Ed and Lorraine Warren '
            'work to help a family terrorized by a dark presence '
            'in their farmhouse. Forced to confront a powerful '
            'entity, the Warrens find themselves caught in the '
            'most terrifying case of their lives.',
            'popularity':
            814.365,
            'poster_path':
            '/wVYREutTvI2tmxr6ujrHT704wGF.jpg',
            'providers':
            None,
            'rating_average':
            7.5,
            'rating_count':
            8233,
            'rating_user':
            None,
            'release_date':
            '2013-08-01',
            'runtime':
            None,
            'status':
            None,
            'title':
            'The Conjuring',
            'tmdb_url':
            'https://www.themoviedb.org/movie/138843',
            'watch_status':
            None
        }, {
            '__typename':
            'Movie',
            'backdrop_path':
            '/9ns9463dwOeo1CK1JU2wirL5Yi1.jpg',
            'cast':
            None,
            'code':
            587807,
            'directors':
            None,
            'favorite':
            False,
            'genres':
            None,
            'overview':
            'Tom the cat and Jerry the mouse get kicked out of '
            'their home and relocate to a fancy New York hotel, '
            'where a scrappy employee named Kayla will lose her '
            'job if she can’t evict Jerry before a high-class '
            'wedding at the hotel. Her solution? Hiring Tom to '
            'get rid of the pesky mouse.',
            'popularity':
            540.018,
            'poster_path':
            '/8XZI9QZ7Pm3fVkigWJPbrXCMzjq.jpg',
            'providers':
            None,
            'rating_average':
            7.3,
            'rating_count':
            1428,
            'rating_user':
            None,
            'release_date':
            '2021-06-17',
            'runtime':
            None,
            'status':
            None,
            'title':
            'Tom & Jerry',
            'tmdb_url':
            'https://www.themoviedb.org/movie/587807',
            'watch_status':
            None
        }],
        'total_pages':
        500
    }

    assert dict == get_discover("8ecf8427e@8ecf8427e.com", tmdb, "Movie", None,
                                None, 1, db)


def test_get_discover_tv():
    tmdb = setup_app()[0]

    dict = {
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/63174',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/91557',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/60735',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/71712',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/120168',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/95057',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1416',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/88396',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/95557',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/80240',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/62286',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/69050',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1399',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/69478',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/93484',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1402',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/18165',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/79008',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/79460',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
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
            'cast': None,
            'creators': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/105971',
            'watch_status': None,
            'rating_user': None,
            'favorite': False,
            'runtime': None,
            '__typename': 'TV'
        }]
    }

    assert dict == get_discover("8ecf8427e@8ecf8427e.com", tmdb, "TV", None,
                                None, 1, db)


def test_get_discover_recommended_movie():
    tmdb = setup_app()[0]

    dict = {
        'total_pages':
        2,
        'results': [{
            '__typename': 'Movie',
            'code': 155,
            'title': 'The Dark Knight',
            'genres': None,
            'overview':
            'Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.',
            'popularity': 52.584,
            'rating_average': 8.467,
            'rating_count': 25260,
            'release_date': '2008-07-16',
            'runtime': None,
            'status': None,
            'backdrop_path': '/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg',
            'poster_path': '/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/155'
        }, {
            '__typename': 'Movie',
            'code': 49026,
            'title': 'The Dark Knight Rises',
            'genres': None,
            'overview':
            "Following the death of District Attorney Harvey Dent, Batman assumes responsibility for Dent's crimes to protect the late attorney's reputation and is subsequently hunted by the Gotham City Police Department. Eight years later, Batman encounters the mysterious Selina Kyle and the villainous Bane, a new terrorist leader who overwhelms Gotham's finest. The Dark Knight resurfaces to protect a city that has branded him an enemy.",
            'popularity': 43.484,
            'rating_average': 7.75,
            'rating_count': 17890,
            'release_date': '2012-07-16',
            'runtime': None,
            'status': None,
            'backdrop_path': '/cKPfiu9IcCW0fMdKdQBXe3PRtTZ.jpg',
            'poster_path': '/vzvKcPQ4o7TjWeGIn0aGC9FeVNu.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/49026'
        }, {
            '__typename': 'Movie',
            'code': 603,
            'title': 'The Matrix',
            'genres': None,
            'overview':
            'Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.',
            'popularity': 41.347,
            'rating_average': 8.152,
            'rating_count': 19321,
            'release_date': '1999-03-30',
            'runtime': None,
            'status': None,
            'backdrop_path': '/8K9qHeM6G6QjQN0C5XKFGvK5lzM.jpg',
            'poster_path': '/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/603'
        }, {
            '__typename': 'Movie',
            'code': 11324,
            'title': 'Shutter Island',
            'genres': None,
            'overview':
            'World War II soldier-turned-U.S. Marshal Teddy Daniels investigates the disappearance of a patient from a hospital for the criminally insane, but his efforts are compromised by his troubling visions and also by a mysterious doctor.',
            'popularity': 36.033,
            'rating_average': 8.166,
            'rating_count': 17984,
            'release_date': '2010-02-14',
            'runtime': None,
            'status': None,
            'backdrop_path': '/8xt8AMb1OKC63AdhNSaYBWxB4Iq.jpg',
            'poster_path': '/kve20tXwUZpu4GUX8l6X7Z4jmL6.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/11324'
        }, {
            '__typename': 'Movie',
            'code': 550,
            'title': 'Fight Club',
            'genres': None,
            'overview':
            'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.',
            'popularity': 34.195,
            'rating_average': 8.427,
            'rating_count': 21858,
            'release_date': '1999-10-15',
            'runtime': None,
            'status': None,
            'backdrop_path': '/rr7E0NoGKxvbkb89eR1GwfoYjpA.jpg',
            'poster_path': '/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/550'
        }, {
            '__typename': 'Movie',
            'code': 120,
            'title': 'The Lord of the Rings: The Fellowship of the Ring',
            'genres': None,
            'overview':
            'Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home in order to keep it from falling into the hands of its evil creator. Along the way, a fellowship is formed to protect the ringbearer and make sure that the ring arrives at its final destination: Mt. Doom, the only place where it can be destroyed.',
            'popularity': 60.948,
            'rating_average': 8.352,
            'rating_count': 19211,
            'release_date': '2001-12-18',
            'runtime': None,
            'status': None,
            'backdrop_path': '/vRQnzOn4HjIMX4LBq9nHhFXbsSu.jpg',
            'poster_path': '/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/120'
        }, {
            '__typename': 'Movie',
            'code': 122,
            'title': 'The Lord of the Rings: The Return of the King',
            'genres': None,
            'overview':
            "Aragorn is revealed as the heir to the ancient kings as he, Gandalf and the other members of the broken fellowship struggle to save Gondor from Sauron's forces. Meanwhile, Frodo and Sam take the ring closer to the heart of Mordor, the dark lord's realm.",
            'popularity': 47.776,
            'rating_average': 8.468,
            'rating_count': 17748,
            'release_date': '2003-12-01',
            'runtime': None,
            'status': None,
            'backdrop_path': '/pm0RiwNpSja8gR0BTWpxo5a9Bbl.jpg',
            'poster_path': '/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/122'
        }, {
            '__typename': 'Movie',
            'code': 68718,
            'title': 'Django Unchained',
            'genres': None,
            'overview':
            'With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.',
            'popularity': 36.574,
            'rating_average': 8.115,
            'rating_count': 20738,
            'release_date': '2012-12-25',
            'runtime': None,
            'status': None,
            'backdrop_path': '/lVcI3MOtumvEbOdS1Og7QoV6Lfc.jpg',
            'poster_path': '/4E4TTsCXVFyhBtYu9fKy0gIT3Ih.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/68718'
        }, {
            '__typename': 'Movie',
            'code': 19995,
            'title': 'Avatar',
            'genres': None,
            'overview':
            'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.',
            'popularity': 65.724,
            'rating_average': 7.471,
            'rating_count': 23522,
            'release_date': '2009-12-10',
            'runtime': None,
            'status': None,
            'backdrop_path': '/AmHOQ7rpHwiaUMRjKXztnauSJb7.jpg',
            'poster_path': '/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/19995'
        }, {
            '__typename': 'Movie',
            'code': 272,
            'title': 'Batman Begins',
            'genres': None,
            'overview':
            'Driven by tragedy, billionaire Bruce Wayne dedicates his life to uncovering and defeating the corruption that plagues his home, Gotham City.  Unable to work within the system, he instead creates a new identity, a symbol of fear for the criminal underworld - The Batman.',
            'popularity': 48.495,
            'rating_average': 7.671,
            'rating_count': 16215,
            'release_date': '2005-06-10',
            'runtime': None,
            'status': None,
            'backdrop_path': '/lh5lbisD4oDbEKgUxoRaZU8HVrk.jpg',
            'poster_path': '/1P3ZyEq02wcTMd3iE4ebtLvncvH.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/272'
        }, {
            '__typename': 'Movie',
            'code': 121,
            'title': 'The Lord of the Rings: The Two Towers',
            'genres': None,
            'overview':
            'Frodo and Sam are trekking to Mordor to destroy the One Ring of Power while Gimli, Legolas and Aragorn search for the orc-captured Merry and Pippin. All along, nefarious wizard Saruman awaits the Fellowship members at the Orthanc Tower in Isengard.',
            'popularity': 54.077,
            'rating_average': 8.335,
            'rating_count': 16596,
            'release_date': '2002-12-18',
            'runtime': None,
            'status': None,
            'backdrop_path': '/kWYfW2Re0rUDE6IHhy4CRuKWeFr.jpg',
            'poster_path': '/5VTN0pR8gcqV3EPUHHfMGnJYN9L.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/121'
        }, {
            '__typename': 'Movie',
            'code': 680,
            'title': 'Pulp Fiction',
            'genres': None,
            'overview':
            "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
            'popularity': 52.119,
            'rating_average': 8.475,
            'rating_count': 21249,
            'release_date': '1994-09-10',
            'runtime': None,
            'status': None,
            'backdrop_path': '/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg',
            'poster_path': '/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/680'
        }, {
            '__typename': 'Movie',
            'code': 37724,
            'title': 'Skyfall',
            'genres': None,
            'overview':
            "When Bond's latest assignment goes gravely wrong and agents around the world are exposed, MI6 is attacked forcing M to relocate the agency. These events cause her authority and position to be challenged by Gareth Mallory, the new Chairman of the Intelligence and Security Committee. With MI6 now compromised from both inside and out, M is left with one ally she can trust: Bond. 007 takes to the shadows - aided only by field agent, Eve - following a trail to the mysterious Silva, whose lethal and hidden motives have yet to reveal themselves.",
            'popularity': 32.854,
            'rating_average': 7.167,
            'rating_count': 12562,
            'release_date': '2012-10-25',
            'runtime': None,
            'status': None,
            'backdrop_path': '/hoQhlAskVNgLQhArnH7reWP4pUp.jpg',
            'poster_path': '/iANstMt9B4unvLMLLOWnBnZIt9b.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/37724'
        }, {
            '__typename': 'Movie',
            'code': 1726,
            'title': 'Iron Man',
            'genres': None,
            'overview':
            'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.',
            'popularity': 69.238,
            'rating_average': 7.614,
            'rating_count': 20740,
            'release_date': '2008-04-30',
            'runtime': None,
            'status': None,
            'backdrop_path': '/7vMqYIHu2E5CbvWr6tmNhYulDfS.jpg',
            'poster_path': '/78lPtwv72eTNqFW9COBYI0dWDJa.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/1726'
        }, {
            '__typename': 'Movie',
            'code': 807,
            'title': 'Se7en',
            'genres': None,
            'overview':
            'Two homicide detectives are on a desperate hunt for a serial killer whose crimes are based on the "seven deadly sins" in this dark and haunting film that takes viewers from the tortured remains of one victim to the next. The seasoned Det. Sommerset researches each sin in an effort to get inside the killer\'s mind, while his novice partner, Mills, scoffs at his efforts to unravel the case.',
            'popularity': 33.071,
            'rating_average': 8.337,
            'rating_count': 15255,
            'release_date': '1995-09-22',
            'runtime': None,
            'status': None,
            'backdrop_path': '/4U4q1zjIwCZTNkp6RKWkWPuC7uI.jpg',
            'poster_path': '/69Sns8WoET6CfaYlIkHbla4l7nC.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/807'
        }, {
            '__typename': 'Movie',
            'code': 10528,
            'title': 'Sherlock Holmes',
            'genres': None,
            'overview':
            'Eccentric consulting detective, Sherlock Holmes and Doctor John Watson battle to bring down a new nemesis and unravel a deadly plot that could destroy England.',
            'popularity': 28.101,
            'rating_average': 7.184,
            'rating_count': 11424,
            'release_date': '2009-12-23',
            'runtime': None,
            'status': None,
            'backdrop_path': '/oLmifRdaETboot2PXxpZN8NqHhK.jpg',
            'poster_path': '/momkKuWburNTqKBF6ez7rvhYVhE.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/10528'
        }, {
            '__typename': 'Movie',
            'code': 24428,
            'title': 'The Avengers',
            'genres': None,
            'overview':
            'When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!',
            'popularity': 107.23,
            'rating_average': 7.684,
            'rating_count': 24827,
            'release_date': '2012-04-25',
            'runtime': None,
            'status': None,
            'backdrop_path': '/nNmJRkg8wWnRmzQDe2FwKbPIsJV.jpg',
            'poster_path': '/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/24428'
        }, {
            '__typename': 'Movie',
            'code': 59967,
            'title': 'Looper',
            'genres': None,
            'overview':
            "In the futuristic action thriller Looper, time travel will be invented but it will be illegal and only available on the black market. When the mob wants to get rid of someone, they will send their target 30 years into the past where a looper, a hired gun, like Joe is waiting to mop up. Joe is getting rich and life is good until the day the mob decides to close the loop, sending back Joe's future self for assassination.",
            'popularity': 15.575,
            'rating_average': 6.843,
            'rating_count': 8284,
            'release_date': '2012-09-26',
            'runtime': None,
            'status': None,
            'backdrop_path': '/4bAwGmE9Sl4FeXoHWVWLXkURHbe.jpg',
            'poster_path': '/sNjL6SqErDBE8OUZlrDLkexfsCj.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/59967'
        }, {
            '__typename': 'Movie',
            'code': 1124,
            'title': 'The Prestige',
            'genres': None,
            'overview':
            'A mysterious story of two magicians whose intense rivalry leads them on a life-long battle for supremacy -- full of obsession, deceit and jealousy with dangerous and deadly consequences.',
            'popularity': 26.038,
            'rating_average': 8.184,
            'rating_count': 11790,
            'release_date': '2006-10-19',
            'runtime': None,
            'status': None,
            'backdrop_path': '/mfJepkInUbiZ0mFXFhDNz8ko6Zr.jpg',
            'poster_path': '/gcphM7ZLxS5HPeCZgjZobfz907x.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/1124'
        }, {
            '__typename': 'Movie',
            'code': 77,
            'title': 'Memento',
            'genres': None,
            'overview':
            "Leonard Shelby is tracking down the man who raped and murdered his wife. The difficulty of locating his wife's killer, however, is compounded by the fact that he suffers from a rare, untreatable form of short-term memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why.",
            'popularity': 20.014,
            'rating_average': 8.196,
            'rating_count': 11099,
            'release_date': '2000-10-11',
            'runtime': None,
            'status': None,
            'backdrop_path': '/q2CtXYjp9IlnfBcPktNkBPsuAEO.jpg',
            'poster_path': '/yuNs09hvpHVU1cBTCAk9zxsL2oW.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/77'
        }, {
            '__typename': 'Movie',
            'code': 16869,
            'title': 'Inglourious Basterds',
            'genres': None,
            'overview':
            'In Nazi-occupied France during World War II, a group of Jewish-American soldiers known as "The Basterds" are chosen specifically to spread fear throughout the Third Reich by scalping and brutally killing Nazis. The Basterds, lead by Lt. Aldo Raine soon cross paths with a French-Jewish teenage girl who runs a movie theater in Paris which is targeted by the soldiers.',
            'popularity': 32.46,
            'rating_average': 8.204,
            'rating_count': 16978,
            'release_date': '2009-08-19',
            'runtime': None,
            'status': None,
            'backdrop_path': '/8pEnePgGyfUqj8Qa6d91OZQ6Aih.jpg',
            'poster_path': '/7sfbEnaARXDDhKm0CZ7D7uc2sbo.jpg',
            'providers': None,
            'cast': None,
            'directors': None,
            'tmdb_url': 'https://www.themoviedb.org/movie/16869'
        }]
    }

    assert dict == get_discover("8ecf8427e@8ecf8427e.com", tmdb, "Movie", None,
                                27205, 1, db)


def test_get_discover_recommended_tv():
    tmdb = setup_app()[0]

    dict = {
        'total_pages':
        2,
        'results': [{
            '__typename': 'TV',
            'code': 61222,
            'title': 'BoJack Horseman',
            'genres': None,
            'overview':
            'Meet the most beloved sitcom horse of the 90s - 20 years later. BoJack Horseman was the star of the hit TV show "Horsin\' Around," but today he\'s washed up, living in Hollywood, complaining about everything, and wearing colorful sweaters.',
            'popularity': 123.435,
            'rating_average': 8.586,
            'rating_count': 1193,
            'first_air_date': '2014-08-22',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/y64WatnpvoeudfapTPx9QFVKbqM.jpg',
            'poster_path': '/pB9L0jAnEQLMKgexqCEocEW8TA.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/61222',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 615,
            'title': 'Futurama',
            'genres': None,
            'overview':
            'The adventures of a late-20th-century New York City pizza delivery boy, Philip J. Fry, who, after being unwittingly cryogenically frozen for one thousand years, finds employment at Planet Express, an interplanetary delivery company in the retro-futuristic 31st century.',
            'popularity': 101.931,
            'rating_average': 8.339,
            'rating_count': 1865,
            'first_air_date': '1999-03-28',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/fTCoAXkLRxg9mWXzCFK2RTC4PFr.jpg',
            'poster_path': '/k5e8kAq9jpaSmgvFM10su5LXGFR.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/615',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 32726,
            'title': "Bob's Burgers",
            'genres': None,
            'overview':
            'Bob\'s Burgers follows a third-generation restaurateur, Bob, as he runs Bob\'s Burgers with the help of his wife and their three kids. Bob and his quirky family have big ideas about burgers, but fall short on service and sophistication. Despite the greasy counters, lousy location and a dearth of customers, Bob and his family are determined to make Bob\'s Burgers "grand re-re-re-opening" a success.',
            'popularity': 66.798,
            'rating_average': 7.915,
            'rating_count': 507,
            'first_air_date': '2011-01-09',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/cIXaqUB2pOIEiQsgO85r9RMKzpe.jpg',
            'poster_path': '/gGlX58u2tJuGFEAYM3VKWz3MEu2.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/32726',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 2190,
            'title': 'South Park',
            'genres': None,
            'overview':
            'Follows the misadventures of four irreverent grade-schoolers in the quiet, dysfunctional town of South Park, Colorado.',
            'popularity': 165.607,
            'rating_average': 8.241,
            'rating_count': 2418,
            'first_air_date': '1997-08-13',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/7uihCghJiyYFTXSh1BOPdHQN8xK.jpg',
            'poster_path': '/iiCY2QIGSnmtVkIdjkKAfwDs0KF.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/2190',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 42009,
            'title': 'Black Mirror',
            'genres': None,
            'overview':
            "A contemporary British re-working of The Twilight Zone with stories that tap into the collective unease about our modern world.\xa0\n\nOver the last ten years, technology has transformed almost every aspect of our lives before we've had time to stop and question it. In every home; on every desk; in every palm - a plasma screen; a monitor; a smartphone - a black mirror of our 21st Century existence.",
            'popularity': 78.483,
            'rating_average': 8.285,
            'rating_count': 2613,
            'first_air_date': '2011-12-04',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/b92npz1sZwvmjUfVIrWXehrk3pc.jpg',
            'poster_path': '/7PRddO7z7mcPi21nZTCMGShAyy1.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/42009',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 40075,
            'title': 'Gravity Falls',
            'genres': None,
            'overview':
            'Twin brother and sister Dipper and Mabel Pines are in for an unexpected adventure when they spend the summer helping their great uncle Stan run a tourist trap in the mysterious town of Gravity Falls, Oregon.',
            'popularity': 103.485,
            'rating_average': 8.38,
            'rating_count': 1563,
            'first_air_date': '2012-06-15',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/l0XvAI856XdyDYEfr1njztjH7u0.jpg',
            'poster_path': '/t9inzSLIttATX6RdnmDjL7T4WN7.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/40075',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 10283,
            'title': 'Archer',
            'genres': None,
            'overview':
            "Sterling Archer is the world's most daunting spy. He works for ISIS, a spy agency run by his mother. In between dealing with his boss and his co-workers - one of whom is his ex-girlfriend - Archer manages to annoy or seduce everyone that crosses his path. His antics are only excusable because at the end of the day, he still somehow always manages to thwart whatever crises was threatening mankind.",
            'popularity': 40.446,
            'rating_average': 7.928,
            'rating_count': 732,
            'first_air_date': '2009-09-17',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/zs9bqvFH3GH5ZZXGeGhT8IwEvFY.jpg',
            'poster_path': '/7v1eODxlqBuOJk5HTtTWURRd1Ke.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/10283',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 74204,
            'title': 'Big Mouth',
            'genres': None,
            'overview':
            'Teenage friends find their lives upended by the wonders and horrors of puberty in this edgy comedy from real-life pals Nick Kroll and Andrew Goldberg.',
            'popularity': 62.446,
            'rating_average': 7.882,
            'rating_count': 521,
            'first_air_date': '2017-09-29',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/uM6WJodeCyTp7h7NhE4rgd0RbRZ.jpg',
            'poster_path': '/1Zio9w1tAd3r5Gu4d9AzTSx2hnT.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/74204',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 1434,
            'title': 'Family Guy',
            'genres': None,
            'overview':
            "Sick, twisted, politically incorrect and Freakin' Sweet animated series featuring the adventures of the dysfunctional Griffin family. Bumbling Peter and long-suffering Lois have three kids. Stewie (a brilliant but sadistic baby bent on killing his mother and taking over the world), Meg (the oldest, and is the most unpopular girl in town) and Chris (the middle kid, he's not very bright but has a passion for movies). The final member of the family is Brian - a talking dog and much more than a pet, he keeps Stewie in check whilst sipping Martinis and sorting through his own life issues.",
            'popularity': 234.717,
            'rating_average': 7.03,
            'rating_count': 2807,
            'first_air_date': '1999-01-31',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/jbTqU6BJMufoMnPSlO4ThrcXs3Y.jpg',
            'poster_path': '/eWWCRjBfLyePh2tfZdvNcIvKSJe.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1434',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 1433,
            'title': 'American Dad!',
            'genres': None,
            'overview':
            'The series focuses on an eccentric motley crew that is the Smith family and their three housemates: Father, husband, and breadwinner Stan Smith; his better half housewife, Francine Smith; their college-aged daughter, Hayley Smith; and their high-school-aged son, Steve Smith. Outside of the Smith family, there are three additional main characters, including Hayley\'s boyfriend turned husband, Jeff Fischer; the family\'s man-in-a-goldfish-body pet, Klaus; and most notably the family\'s zany alien, Roger, who is "full of masquerades, brazenness, and shocking antics."',
            'popularity': 160.886,
            'rating_average': 6.759,
            'rating_count': 1305,
            'first_air_date': '2005-02-06',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/hxez7Xn6Xc5bTtK3oTSnl594XYr.jpg',
            'poster_path': '/aC1q422YhQR7k82GB8gW4KoD91p.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1433',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 19885,
            'title': 'Sherlock',
            'genres': None,
            'overview':
            'A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.',
            'popularity': 44.911,
            'rating_average': 8.451,
            'rating_count': 3012,
            'first_air_date': '2010-07-25',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/cU2WCPB5UNIyDg0vYgBwy2P4nBG.jpg',
            'poster_path': '/7WTsnHkbA0FaG6R9twfFde0I9hl.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/19885',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 4589,
            'title': 'Arrested Development',
            'genres': None,
            'overview':
            'The story of a wealthy family that lost everything, and the one son who had no choice but to keep them all together.',
            'popularity': 43.754,
            'rating_average': 8.066,
            'rating_count': 782,
            'first_air_date': '2003-11-02',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/ArZwmJl1y6qlnLjuE9FXlEd8RU0.jpg',
            'poster_path': '/qMzwO952hMWQSCfHkp7IL20s4K7.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/4589',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 2710,
            'title': "It's Always Sunny in Philadelphia",
            'genres': None,
            'overview':
            'Four egocentric friends who run a neighborhood Irish pub in Philadelphia try to find their way through the adult world of work and relationships. Unfortunately, their warped views and precarious judgments often lead them to trouble, creating a myriad of uncomfortable situations that usually only get worse before they get better.',
            'popularity': 88.059,
            'rating_average': 8.23,
            'rating_count': 588,
            'first_air_date': '2005-08-04',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/jShJsNrWs2t7sGpk5eDgRx0z8vE.jpg',
            'poster_path': '/xX3vAWdCb828T48HM9OvvD0p4PC.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/2710',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 66732,
            'title': 'Stranger Things',
            'genres': None,
            'overview':
            'When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces, and one strange little girl.',
            'popularity': 166.343,
            'rating_average': 8.604,
            'rating_count': 8393,
            'first_air_date': '2016-07-15',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/rcA17r3hfHtRrk3Xs3hXrgGeSGT.jpg',
            'poster_path': '/x2LSRK2Cm7MZhjluni1msVJ3wDF.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/66732',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 8592,
            'title': 'Parks and Recreation',
            'genres': None,
            'overview':
            'Hilarious ensemble comedy that follows Leslie Knope, a mid-level bureaucrat in the Parks and Recreation Department of Pawnee, Indiana, and her tireless efforts to make her quintessentially American town just a little bit more fun.',
            'popularity': 83.052,
            'rating_average': 8.034,
            'rating_count': 748,
            'first_air_date': '2009-04-09',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/dVISMO3TdX9HfcnA4gt3PSqcfjL.jpg',
            'poster_path': '/dFs6yHxheEGoZSoA0Fdkgy6Jxh0.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/8592',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 1396,
            'title': 'Breaking Bad',
            'genres': None,
            'overview':
            "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
            'popularity': 216.182,
            'rating_average': 8.705,
            'rating_count': 7136,
            'first_air_date': '2008-01-20',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg',
            'poster_path': '/ggFHVNu6YYI5L9pCfOacjizRGt.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/1396',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 18347,
            'title': 'Community',
            'genres': None,
            'overview':
            'Follow the lives of a group of students at what is possibly the world’s worst community college in the fictional locale of Greendale, Colorado.',
            'popularity': 78.283,
            'rating_average': 7.953,
            'rating_count': 831,
            'first_air_date': '2009-09-17',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/7NlcCG8WxQzlYxkDNOmjMVPaFKb.jpg',
            'poster_path': '/3KUjDt8XY7w2Ku70UE0SECmv1zP.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/18347',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 2382,
            'title': 'Freaks and Geeks',
            'genres': None,
            'overview':
            'High school mathlete Lindsay Weir rebels and begins hanging out with a crowd of burnouts (the "freaks"), while her brother Sam Weir navigates a different part of the social universe with his nerdy friends (the "geeks").',
            'popularity': 35.176,
            'rating_average': 8.1,
            'rating_count': 435,
            'first_air_date': '1999-09-25',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/jGH4V7h1p5QWqYMUiUJcwer7LAT.jpg',
            'poster_path': '/5pzYGqYdU9eBzy3gTUtRYLlNJ8B.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/2382',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 73021,
            'title': 'Disenchantment',
            'genres': None,
            'overview':
            'Set in a ruined medieval city called Dreamland, Disenchantment follows the grubby adventures of a hard-drinking princess, her feisty elf companion and her personal demon.',
            'popularity': 34.641,
            'rating_average': 7.523,
            'rating_count': 437,
            'first_air_date': '2018-08-17',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/hHEqDPbO6z4Xje5tOf3Wm1mdMtI.jpg',
            'poster_path': '/1WynayCqKRzrl4cFZR8NOfiDwd6.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/73021',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 63522,
            'title': 'F is for Family',
            'genres': None,
            'overview':
            'Follow the Murphy family back to the 1970s, when kids roamed wild, beer flowed freely and nothing came between a man and his TV.',
            'popularity': 23.717,
            'rating_average': 7.1,
            'rating_count': 158,
            'first_air_date': '2015-12-18',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/etusSQ2nFsxuzauzWL43qBgsHek.jpg',
            'poster_path': '/86hMUI1sRMmDPOWRd6kLa3nO181.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/63522',
            'runtime': None
        }, {
            '__typename': 'TV',
            'code': 74387,
            'title': 'Final Space',
            'genres': None,
            'overview':
            'An astronaut named Gary and his planet-destroying sidekick Mooncake embark on serialized journeys through space in order to unlock the mystery of “Final Space,” the last point in the universe, if it actually does exist.',
            'popularity': 41.489,
            'rating_average': 8.567,
            'rating_count': 452,
            'first_air_date': '2018-02-26',
            'last_air_date': None,
            'status': None,
            'backdrop_path': '/vEMl9RED1HelffdKWxToa3fmyo2.jpg',
            'poster_path': '/zT6tXWsJoBOWJT1PeUEKLTFOoHh.jpg',
            'providers': None,
            'creators': None,
            'cast': None,
            'number_of_episodes': None,
            'number_of_seasons': None,
            'tmdb_url': 'https://www.themoviedb.org/tv/74387',
            'runtime': None
        }]
    }

    assert dict == get_discover("8ecf8427e@8ecf8427e.com", tmdb, "TV", None,
                                60625, 1, db)
