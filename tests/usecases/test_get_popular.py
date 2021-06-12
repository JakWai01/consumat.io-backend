from tests.tmdb.tmdb_mock import TmdbMock
from consumatio.usecases.get_popular import get_popular
import os
from consumatio.external.db.models import *
from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI
from tests.utils.setup_app import setup_app


def test_get_popular_movie():
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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
            None,
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

    assert dict == get_popular("8ecf8427e@8ecf8427e.com", tmdb, "Movie", 1)


def test_get_popular_tv():
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
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
            'favorite': None,
            'runtime': None,
            '__typename': 'TV'
        }]
    }

    assert dict == get_popular("8ecf8427e@8ecf8427e.com", tmdb, "TV", 1)