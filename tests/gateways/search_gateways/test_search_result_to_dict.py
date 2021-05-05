from consumatio.gateways.search_gateways.search_result_to_dict import *


def test_tv_search_results_to_dict():
    tv_json = {
        "results": [{
            "backdrop_path": "/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg",
            "first_air_date": "2008-01-20",
            "genre_ids": [18],
            "id": 1396,
            "media_type": "tv",
            "name": "Breaking Bad",
            "origin_country": ["US"],
            "original_language": "en",
            "original_name": "Breaking Bad",
            "overview":
            "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
            "popularity": 264.148,
            "poster_path": "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
            "vote_average": 8.7,
            "vote_count": 6923
        }]
    }

    tv_dict = [{
        "__typename": "TV",
        "code": 1396,
        "title": "Breaking Bad",
        "genres": None,
        "overview":
        "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
        "popularity": 264.148,
        "rating_average": 8.7,
        "first_air_date": "2008-01-20",
        "last_air_date": None,
        "status": None,
        "backdrop_path": "/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg",
        "poster_path": "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
        "providers": None,
        "creators": None,
        "cast": None,
        "number_of_episodes": None,
        "number_of_seasons": None,
        "tmdb_url": f'https://www.themoviedb.org/tv/1396',
        "watch_status": None,
        "rating_user": None,
        "favorite": None
    }]

    assert search_result_to_dict(tv_json) == tv_dict


def test_movie_search_results_to_dict():
    movie_json = {
        "results": [{
            "adult": False,
            "backdrop_path": "/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
            "genre_ids": [18, 28, 80, 53],
            "id": 155,
            "media_type": "movie",
            "original_language": "en",
            "original_title": "The Dark Knight",
            "overview":
            "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
            "popularity": 50.312,
            "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
            "release_date": "2008-07-16",
            "title": "The Dark Knight",
            "video": False,
            "vote_average": 8.5,
            "vote_count": 24947
        }]
    }

    movie_dict = [{
        "__typename": "Movie",
        "code": 155,
        "title": "The Dark Knight",
        "genres": None,
        "overview":
        "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
        "popularity": 50.312,
        "rating_average": 8.5,
        "release_date": "2008-07-16",
        "runtime": None,
        "status": None,
        "backdrop_path": "/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
        "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "providers": None,
        "cast": None,
        "directors": None,
        "tmdb_url": f'https://www.themoviedb.org/movie/{155}',
        "watch_status": None,
        "rating_user": None,
        "favorite": None
    }]

    assert search_result_to_dict(movie_json) == movie_dict


def test_person_search_results_to_dict():
    person_json = {
        "results": [{
            "adult":
            False,
            "gender":
            2,
            "id":
            17419,
            "known_for": [{
                "adult": False,
                "backdrop_path": "/hjQp148VjWF4KjzhsD90OCMr11h.jpg",
                "genre_ids": [18, 36, 10752],
                "id": 857,
                "media_type": "movie",
                "original_language": "en",
                "original_title": "Saving Private Ryan",
                "overview":
                "As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, with a fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with penetrating German-held territory and bringing the boy home.",
                "poster_path": "/1wY4psJ5NVEhCuOYROwLH2XExM2.jpg",
                "release_date": "1998-07-24",
                "title": "Saving Private Ryan",
                "video": False,
                "vote_average": 8.2,
                "vote_count": 11637
            }, {
                "adult": False,
                "backdrop_path": "/uslmOwQpdRRUwr6AmBP6JdzeHjS.jpg",
                "genre_ids": [18, 53, 80],
                "id": 64690,
                "media_type": "movie",
                "original_language": "en",
                "original_title": "Drive",
                "overview":
                "Driver is a skilled Hollywood stuntman who moonlights as a getaway driver for criminals. Though he projects an icy exterior, lately he's been warming up to a pretty neighbor named Irene and her young son, Benicio. When Irene's husband gets out of jail, he enlists Driver's help in a million-dollar heist. The job goes horribly wrong, and Driver must risk his life to protect Irene and Benicio from the vengeful masterminds behind the robbery.",
                "poster_path": "/602vevIURmpDfzbnv5Ubi6wIkQm.jpg",
                "release_date": "2011-06-17",
                "title": "Drive",
                "video": False,
                "vote_average": 7.6,
                "vote_count": 9271
            }, {
                "backdrop_path": "/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg",
                "first_air_date": "2008-01-20",
                "genre_ids": [18],
                "id": 1396,
                "media_type": "tv",
                "name": "Breaking Bad",
                "origin_country": ["US"],
                "original_language": "en",
                "original_name": "Breaking Bad",
                "overview":
                "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
                "poster_path": "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
                "vote_average": 8.7,
                "vote_count": 6921
            }],
            "known_for_department":
            "Acting",
            "media_type":
            "person",
            "name":
            "Bryan Cranston",
            "popularity":
            8.655,
            "profile_path":
            "/7Jahy5LZX2Fo8fGJltMreAI49hC.jpg"
        }]
    }

    empty_dict = []

    assert search_result_to_dict(person_json) == empty_dict


def test_empty_search_results_to_dict():
    empty_json = {
        "page": 1,
        "results": [],
        "total_pages": 0,
        "total_results": 0
    }

    without_result_json = {"page": 1, "total_pages": 0, "total_results": 0}

    empty_dict = []

    assert search_result_to_dict(empty_json) == empty_dict
    assert search_result_to_dict(without_result_json) == empty_dict
