from consumatio.entities.movie import Movie

def test_movie():
    movie = Movie(
        id = 550,
        title = "Fight Club",
        genres = [
            {
                "id": 18,
                "name": "Drama"
            }
        ],
        overview = "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        popularity = 0.5,
        release_date = "1999-10-12",
        runtime = 139,
        status = "Released",
        backdrops = [
            {
                "aspect_ratio": 1.77777777777778,
                "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
                "height": 720,
                "iso_639_1": None,
                "vote_average": 0,
                "vote_count": 0,
                "width": 1280
            }
        ],
        posters = [
            {
                "aspect_ratio": 0.666666666666667,
                "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
                "height": 1800,
                "iso_639_1": "en",
                "vote_average": 0,
                "vote_count": 0,
                "width": 1200
            }
        ],
        providers = [
            {
                "display_priority": 2,
                "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
                "provider_id": 2,
                "provider_name": "Apple iTunes"
            },
            {
                "display_priority": 3,
                "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
                "provider_id": 3,
                "provider_name": "Google Play Movies"
            },
            {
                "display_priority": 7,
                "logo_path": "/vjKeS7Y9fNyqNtvp2ROCc71iu1u.jpg",
                "provider_id": 40,
                "provider_name": "Chili"
            },
            {
                "display_priority": 8,
                "logo_path": "/pZgeSWpfvD59x6sY6stT5c6uc2h.jpg",
                "provider_id": 130,
                "provider_name": "Sky Store"
            },
            {
                "display_priority": 10,
                "logo_path": "/sVBEF7q7LqjHAWSnKwDbzmr2EMY.jpg",
                "provider_id": 10,
                "provider_name": "Amazon Video"
            },
            {
                "display_priority": 12,
                "logo_path": "/vDCcryHD32b0yMeSCgBhuYavsmx.jpg",
                "provider_id": 192,
                "provider_name": "YouTube"
            },
            {
                "display_priority": 14,
                "logo_path": "/mosNtwHNCqCmjk7n5odKgYYf2GI.jpg",
                "provider_id": 20,
                "provider_name": "maxdome Store"
            },
            {
                "display_priority": 18,
                "logo_path": "/wuViyDkbFp4r7VqI0efPW5hFfQj.jpg",
                "provider_id": 35,
                "provider_name": "Rakuten TV"
            },
            {
                "display_priority": 25,
                "logo_path": "/6QfNLK9toSu2bvsWN7A0sEsTz3j.jpg",
                "provider_id": 178,
                "provider_name": "EntertainTV"
            },
            {
                "display_priority": 37,
                "logo_path": "/paq2o2dIfQnxcERsVoq7Ys8KYz8.jpg",
                "provider_id": 68,
                "provider_name": "Microsoft Store"
            }
        ],
        watch_status = "WATCHED",
        rating = 7.9,
        favorite = True
    )

    assert movie.id == 550
    assert movie.title == "Fight Club"
    assert movie.genres == [
        {
            "id": 18,
            "name": "Drama"
        }
    ]
    assert movie.overview == "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion."
    assert movie.popularity == 0.5
    assert movie.release_date == "1999-10-12"
    assert movie.runtime == 139
    assert movie.status == "Released"
    assert movie.backdrops == [
        {
            "aspect_ratio": 1.77777777777778,
            "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
            "height": 720,
            "iso_639_1": None,
            "vote_average": 0,
            "vote_count": 0,
            "width": 1280
        }
    ]
    assert movie.posters == [
        {
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }
    ]
    assert movie.providers == [
        {
            "display_priority": 2,
            "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
            "provider_id": 2,
            "provider_name": "Apple iTunes"
        },
        {
            "display_priority": 3,
            "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
            "provider_id": 3,
            "provider_name": "Google Play Movies"
        },
        {
            "display_priority": 7,
            "logo_path": "/vjKeS7Y9fNyqNtvp2ROCc71iu1u.jpg",
            "provider_id": 40,
            "provider_name": "Chili"
        },
        {
            "display_priority": 8,
            "logo_path": "/pZgeSWpfvD59x6sY6stT5c6uc2h.jpg",
            "provider_id": 130,
            "provider_name": "Sky Store"
        },
        {
            "display_priority": 10,
            "logo_path": "/sVBEF7q7LqjHAWSnKwDbzmr2EMY.jpg",
            "provider_id": 10,
            "provider_name": "Amazon Video"
        },
        {
            "display_priority": 12,
            "logo_path": "/vDCcryHD32b0yMeSCgBhuYavsmx.jpg",
            "provider_id": 192,
            "provider_name": "YouTube"
        },
        {
            "display_priority": 14,
            "logo_path": "/mosNtwHNCqCmjk7n5odKgYYf2GI.jpg",
            "provider_id": 20,
            "provider_name": "maxdome Store"
        },
        {
            "display_priority": 18,
            "logo_path": "/wuViyDkbFp4r7VqI0efPW5hFfQj.jpg",
            "provider_id": 35,
            "provider_name": "Rakuten TV"
        },
        {
            "display_priority": 25,
            "logo_path": "/6QfNLK9toSu2bvsWN7A0sEsTz3j.jpg",
            "provider_id": 178,
            "provider_name": "EntertainTV"
        },
        {
            "display_priority": 37,
            "logo_path": "/paq2o2dIfQnxcERsVoq7Ys8KYz8.jpg",
            "provider_id": 68,
            "provider_name": "Microsoft Store"
        }
    ]
    assert movie.watch_status == "WATCHED"
    assert movie.rating == 7.9
    assert movie.favorite == True

def test_movie_from_dict():
    dict = {
        "id": 550,
        "title": "Fight Club",
        "genres": [
            {
                "id": 18,
                "name": "Drama"
            }
        ],
        "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity": 0.5,
        "release_date": "1999-10-12",
        "runtime": 139,
        "status": "Released",
        "backdrops": [
            {
                "aspect_ratio": 1.77777777777778,
                "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
                "height": 720,
                "iso_639_1": None,
                "vote_average": 0,
                "vote_count": 0,
                "width": 1280
            }
        ],
        "posters": [
            {
                "aspect_ratio": 0.666666666666667,
                "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
                "height": 1800,
                "iso_639_1": "en",
                "vote_average": 0,
                "vote_count": 0,
                "width": 1200
            }
        ],
        "providers": [
            {
                "display_priority": 2,
                "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
                "provider_id": 2,
                "provider_name": "Apple iTunes"
            },
            {
                "display_priority": 3,
                "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
                "provider_id": 3,
                "provider_name": "Google Play Movies"
            },
            {
                "display_priority": 7,
                "logo_path": "/vjKeS7Y9fNyqNtvp2ROCc71iu1u.jpg",
                "provider_id": 40,
                "provider_name": "Chili"
            },
            {
                "display_priority": 8,
                "logo_path": "/pZgeSWpfvD59x6sY6stT5c6uc2h.jpg",
                "provider_id": 130,
                "provider_name": "Sky Store"
            },
            {
                "display_priority": 10,
                "logo_path": "/sVBEF7q7LqjHAWSnKwDbzmr2EMY.jpg",
                "provider_id": 10,
                "provider_name": "Amazon Video"
            },
            {
                "display_priority": 12,
                "logo_path": "/vDCcryHD32b0yMeSCgBhuYavsmx.jpg",
                "provider_id": 192,
                "provider_name": "YouTube"
            },
            {
                "display_priority": 14,
                "logo_path": "/mosNtwHNCqCmjk7n5odKgYYf2GI.jpg",
                "provider_id": 20,
                "provider_name": "maxdome Store"
            },
            {
                "display_priority": 18,
                "logo_path": "/wuViyDkbFp4r7VqI0efPW5hFfQj.jpg",
                "provider_id": 35,
                "provider_name": "Rakuten TV"
            },
            {
                "display_priority": 25,
                "logo_path": "/6QfNLK9toSu2bvsWN7A0sEsTz3j.jpg",
                "provider_id": 178,
                "provider_name": "EntertainTV"
            },
            {
                "display_priority": 37,
                "logo_path": "/paq2o2dIfQnxcERsVoq7Ys8KYz8.jpg",
                "provider_id": 68,
                "provider_name": "Microsoft Store"
            }
        ],
        "watch_status": "WATCHED",
        "rating": 7.9,
        "favorite": True
    }

    movie = Movie.from_dict(dict)

    assert movie.id == 550
    assert movie.title == "Fight Club"
    assert movie.genres == [
        {
            "id": 18,
            "name": "Drama"
        }
    ]
    assert movie.overview == "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion."
    assert movie.popularity == 0.5
    assert movie.release_date == "1999-10-12"
    assert movie.runtime == 139
    assert movie.status == "Released"
    assert movie.backdrops == [
        {
            "aspect_ratio": 1.77777777777778,
            "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
            "height": 720,
            "iso_639_1": None,
            "vote_average": 0,
            "vote_count": 0,
            "width": 1280
        }
    ]
    assert movie.posters == [
        {
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }
    ]
    assert movie.providers == [
        {
            "display_priority": 2,
            "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
            "provider_id": 2,
            "provider_name": "Apple iTunes"
        },
        {
            "display_priority": 3,
            "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
            "provider_id": 3,
            "provider_name": "Google Play Movies"
        },
        {
            "display_priority": 7,
            "logo_path": "/vjKeS7Y9fNyqNtvp2ROCc71iu1u.jpg",
            "provider_id": 40,
            "provider_name": "Chili"
        },
        {
            "display_priority": 8,
            "logo_path": "/pZgeSWpfvD59x6sY6stT5c6uc2h.jpg",
            "provider_id": 130,
            "provider_name": "Sky Store"
        },
        {
            "display_priority": 10,
            "logo_path": "/sVBEF7q7LqjHAWSnKwDbzmr2EMY.jpg",
            "provider_id": 10,
            "provider_name": "Amazon Video"
        },
        {
            "display_priority": 12,
            "logo_path": "/vDCcryHD32b0yMeSCgBhuYavsmx.jpg",
            "provider_id": 192,
            "provider_name": "YouTube"
        },
        {
            "display_priority": 14,
            "logo_path": "/mosNtwHNCqCmjk7n5odKgYYf2GI.jpg",
            "provider_id": 20,
            "provider_name": "maxdome Store"
        },
        {
            "display_priority": 18,
            "logo_path": "/wuViyDkbFp4r7VqI0efPW5hFfQj.jpg",
            "provider_id": 35,
            "provider_name": "Rakuten TV"
        },
        {
            "display_priority": 25,
            "logo_path": "/6QfNLK9toSu2bvsWN7A0sEsTz3j.jpg",
            "provider_id": 178,
            "provider_name": "EntertainTV"
        },
        {
            "display_priority": 37,
            "logo_path": "/paq2o2dIfQnxcERsVoq7Ys8KYz8.jpg",
            "provider_id": 68,
            "provider_name": "Microsoft Store"
        }
    ]
    assert movie.watch_status == "WATCHED"
    assert movie.rating == 7.9
    assert movie.favorite == True

    
def test_movie_to_dict():
    dict = {
        "id": 550,
        "title": "Fight Club",
        "genres": [
            {
                "id": 18,
                "name": "Drama"
            }
        ],
        "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity": 0.5,
        "release_date": "1999-10-12",
        "runtime": 139,
        "status": "Released",
        "backdrops": [
            {
                "aspect_ratio": 1.77777777777778,
                "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
                "height": 720,
                "iso_639_1": None,
                "vote_average": 0,
                "vote_count": 0,
                "width": 1280
            }
        ],
        "posters": [
            {
                "aspect_ratio": 0.666666666666667,
                "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
                "height": 1800,
                "iso_639_1": "en",
                "vote_average": 0,
                "vote_count": 0,
                "width": 1200
            }
        ],
        "providers": [
            {
                "display_priority": 2,
                "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
                "provider_id": 2,
                "provider_name": "Apple iTunes"
            },
            {
                "display_priority": 3,
                "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
                "provider_id": 3,
                "provider_name": "Google Play Movies"
            },
            {
                "display_priority": 7,
                "logo_path": "/vjKeS7Y9fNyqNtvp2ROCc71iu1u.jpg",
                "provider_id": 40,
                "provider_name": "Chili"
            },
            {
                "display_priority": 8,
                "logo_path": "/pZgeSWpfvD59x6sY6stT5c6uc2h.jpg",
                "provider_id": 130,
                "provider_name": "Sky Store"
            },
            {
                "display_priority": 10,
                "logo_path": "/sVBEF7q7LqjHAWSnKwDbzmr2EMY.jpg",
                "provider_id": 10,
                "provider_name": "Amazon Video"
            },
            {
                "display_priority": 12,
                "logo_path": "/vDCcryHD32b0yMeSCgBhuYavsmx.jpg",
                "provider_id": 192,
                "provider_name": "YouTube"
            },
            {
                "display_priority": 14,
                "logo_path": "/mosNtwHNCqCmjk7n5odKgYYf2GI.jpg",
                "provider_id": 20,
                "provider_name": "maxdome Store"
            },
            {
                "display_priority": 18,
                "logo_path": "/wuViyDkbFp4r7VqI0efPW5hFfQj.jpg",
                "provider_id": 35,
                "provider_name": "Rakuten TV"
            },
            {
                "display_priority": 25,
                "logo_path": "/6QfNLK9toSu2bvsWN7A0sEsTz3j.jpg",
                "provider_id": 178,
                "provider_name": "EntertainTV"
            },
            {
                "display_priority": 37,
                "logo_path": "/paq2o2dIfQnxcERsVoq7Ys8KYz8.jpg",
                "provider_id": 68,
                "provider_name": "Microsoft Store"
            }
        ],
        "watch_status": "WATCHED",
        "rating": 7.9,
        "favorite": True
    }

    movie = Movie.from_dict(dict)

    assert movie.to_dict() == dict

def test_movie_model_comparison():
    dict = {
        "id": 550,
        "title": "Fight Club",
        "genres": [
            {
                "id": 18,
                "name": "Drama"
            }
        ],
        "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity": 0.5,
        "release_date": "1999-10-12",
        "runtime": 139,
        "status": "Released",
        "backdrops": [
            {
                "aspect_ratio": 1.77777777777778,
                "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
                "height": 720,
                "iso_639_1": None,
                "vote_average": 0,
                "vote_count": 0,
                "width": 1280
            }
        ],
        "posters": [
            {
                "aspect_ratio": 0.666666666666667,
                "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
                "height": 1800,
                "iso_639_1": "en",
                "vote_average": 0,
                "vote_count": 0,
                "width": 1200
            }
        ],
        "providers": [
            {
                "display_priority": 2,
                "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
                "provider_id": 2,
                "provider_name": "Apple iTunes"
            },
            {
                "display_priority": 3,
                "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
                "provider_id": 3,
                "provider_name": "Google Play Movies"
            },
            {
                "display_priority": 7,
                "logo_path": "/vjKeS7Y9fNyqNtvp2ROCc71iu1u.jpg",
                "provider_id": 40,
                "provider_name": "Chili"
            },
            {
                "display_priority": 8,
                "logo_path": "/pZgeSWpfvD59x6sY6stT5c6uc2h.jpg",
                "provider_id": 130,
                "provider_name": "Sky Store"
            },
            {
                "display_priority": 10,
                "logo_path": "/sVBEF7q7LqjHAWSnKwDbzmr2EMY.jpg",
                "provider_id": 10,
                "provider_name": "Amazon Video"
            },
            {
                "display_priority": 12,
                "logo_path": "/vDCcryHD32b0yMeSCgBhuYavsmx.jpg",
                "provider_id": 192,
                "provider_name": "YouTube"
            },
            {
                "display_priority": 14,
                "logo_path": "/mosNtwHNCqCmjk7n5odKgYYf2GI.jpg",
                "provider_id": 20,
                "provider_name": "maxdome Store"
            },
            {
                "display_priority": 18,
                "logo_path": "/wuViyDkbFp4r7VqI0efPW5hFfQj.jpg",
                "provider_id": 35,
                "provider_name": "Rakuten TV"
            },
            {
                "display_priority": 25,
                "logo_path": "/6QfNLK9toSu2bvsWN7A0sEsTz3j.jpg",
                "provider_id": 178,
                "provider_name": "EntertainTV"
            },
            {
                "display_priority": 37,
                "logo_path": "/paq2o2dIfQnxcERsVoq7Ys8KYz8.jpg",
                "provider_id": 68,
                "provider_name": "Microsoft Store"
            }
        ],
        "watch_status": "WATCHED",
        "rating": 7.9,
        "favorite": True
    }

    movie1 = Movie.from_dict(dict)
    movie2 = Movie.from_dict(dict)

    assert movie1 == movie2



    