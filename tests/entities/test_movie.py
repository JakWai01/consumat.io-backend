from consumatio.entities.movie import Movie


def test_movie():
    movie = Movie(
        code=550,
        title="Fight Club",
        genres=[{
            "name": "Drama"
        }],
        overview=
        "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        popularity=0.5,
        rating_average=5.7,
        release_date="1999-10-12",
        runtime=139,
        status="Released",
        backdrop_path="/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
        poster_path="/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
        providers=[{
            "name": "Apple iTunes"
        }, {
            "name": "Google Play Movies"
        }, {
            "name": "Chili"
        }, {
            "name": "Sky Store"
        }, {
            "name": "Amazon Video"
        }, {
            "name": "YouTube"
        }, {
            "name": "maxdome Store"
        }, {
            "name": "Rakuten TV"
        }, {
            "name": "EntertainTV"
        }, {
            "name": "Microsoft Store"
        }],
        cast=[{
            "name": "Edward Norton",
            "role": "The Narrator",
            "image": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
            "job": "Acting"
        }],
        directors=[{
            "name": "Christopher Nolan"
        }],
        tmdb_url="https://www.themoviedb.org/movie/508442",
        watch_status="WATCHED",
        rating_user=7.9,
        favorite=True)

    assert movie.code == 550
    assert movie.title == "Fight Club"
    assert movie.genres == [{"name": "Drama"}]
    assert movie.overview == "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion."
    assert movie.popularity == 0.5
    assert movie.rating_average == 5.7
    assert movie.release_date == "1999-10-12"
    assert movie.runtime == 139
    assert movie.status == "Released"
    assert movie.backdrop_path == "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg"
    assert movie.poster_path == "/fpemzjF623QVTe98pCVlwwtFC5N.jpg"
    assert movie.providers == [{
        "name": "Apple iTunes"
    }, {
        "name": "Google Play Movies"
    }, {
        "name": "Chili"
    }, {
        "name": "Sky Store"
    }, {
        "name": "Amazon Video"
    }, {
        "name": "YouTube"
    }, {
        "name": "maxdome Store"
    }, {
        "name": "Rakuten TV"
    }, {
        "name": "EntertainTV"
    }, {
        "name": "Microsoft Store"
    }]
    assert movie.cast == [{
        "name": "Edward Norton",
        "role": "The Narrator",
        "image": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
        "job": "Acting"
    }]
    assert movie.directors == [{"name": "Christopher Nolan"}]
    assert movie.tmdb_url == "https://www.themoviedb.org/movie/508442"
    assert movie.watch_status == "WATCHED"
    assert movie.rating_user == 7.9
    assert movie.favorite == True


def test_movie_from_dict():
    dict = {
        "code":
        550,
        "title":
        "Fight Club",
        "genres": [{
            "name": "Drama"
        }],
        "overview":
        "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity":
        0.5,
        "rating_average":
        5.7,
        "release_date":
        "1999-10-12",
        "runtime":
        139,
        "status":
        "Released",
        "backdrop_path":
        "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
        "poster_path":
        "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
        "providers": [{
            "name": "Apple iTunes"
        }, {
            "name": "Google Play Movies"
        }, {
            "name": "Chili"
        }, {
            "name": "Sky Store"
        }, {
            "name": "Amazon Video"
        }, {
            "name": "YouTube"
        }, {
            "name": "maxdome Store"
        }, {
            "name": "Rakuten TV"
        }, {
            "name": "EntertainTV"
        }, {
            "name": "Microsoft Store"
        }],
        "cast": [{
            "name": "Edward Norton",
            "role": "The Narrator",
            "image": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
            "job": "Acting"
        }],
        "directors": [{
            "name": "Christopher Nolan"
        }],
        "tmdb_url":
        "https://www.themoviedb.org/movie/508442",
        "watch_status":
        "WATCHED",
        "rating_user":
        7.9,
        "favorite":
        True
    }

    movie = Movie.from_dict(dict)

    assert movie.code == 550
    assert movie.title == "Fight Club"
    assert movie.genres == [{"name": "Drama"}]
    assert movie.overview == "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion."
    assert movie.popularity == 0.5
    assert movie.rating_average == 5.7
    assert movie.release_date == "1999-10-12"
    assert movie.runtime == 139
    assert movie.status == "Released"
    assert movie.backdrop_path == "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg"
    assert movie.poster_path == "/fpemzjF623QVTe98pCVlwwtFC5N.jpg"
    assert movie.providers == [{
        "name": "Apple iTunes"
    }, {
        "name": "Google Play Movies"
    }, {
        "name": "Chili"
    }, {
        "name": "Sky Store"
    }, {
        "name": "Amazon Video"
    }, {
        "name": "YouTube"
    }, {
        "name": "maxdome Store"
    }, {
        "name": "Rakuten TV"
    }, {
        "name": "EntertainTV"
    }, {
        "name": "Microsoft Store"
    }]
    assert movie.cast == [{
        "name": "Edward Norton",
        "role": "The Narrator",
        "image": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
        "job": "Acting"
    }]
    assert movie.directors == [{"name": "Christopher Nolan"}]
    assert movie.tmdb_url == "https://www.themoviedb.org/movie/508442"
    assert movie.watch_status == "WATCHED"
    assert movie.rating_user == 7.9
    assert movie.favorite == True


def test_movie_to_dict():
    dict = {
        "code":
        550,
        "title":
        "Fight Club",
        "genres": [{
            "name": "Drama"
        }],
        "overview":
        "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity":
        0.5,
        "rating_average":
        5.7,
        "release_date":
        "1999-10-12",
        "runtime":
        139,
        "status":
        "Released",
        "backdrop_path":
        "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
        "poster_path":
        "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
        "providers": [{
            "name": "Apple iTunes"
        }, {
            "name": "Google Play Movies"
        }, {
            "name": "Chili"
        }, {
            "name": "Sky Store"
        }, {
            "name": "Amazon Video"
        }, {
            "name": "YouTube"
        }, {
            "name": "maxdome Store"
        }, {
            "name": "Rakuten TV"
        }, {
            "name": "EntertainTV"
        }, {
            "name": "Microsoft Store"
        }],
        "cast": [{
            "name": "Edward Norton",
            "role": "The Narrator",
            "image": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
            "job": "Acting"
        }],
        "directors": [{
            "name": "Christopher Nolan"
        }],
        "tmdb_url":
        "https://www.themoviedb.org/movie/508442",
        "watch_status":
        "WATCHED",
        "rating_user":
        7.9,
        "favorite":
        True
    }

    movie = Movie.from_dict(dict)

    assert movie.to_dict() == dict


def test_movie_model_comparison():
    dict = {
        "code":
        550,
        "title":
        "Fight Club",
        "genres": [{
            "name": "Drama"
        }],
        "overview":
        "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
        "popularity":
        0.5,
        "rating_average":
        5.7,
        "release_date":
        "1999-10-12",
        "runtime":
        139,
        "status":
        "Released",
        "backdrop_path":
        "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
        "poster_path":
        "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
        "providers": [{
            "name": "Apple iTunes"
        }, {
            "name": "Google Play Movies"
        }, {
            "name": "Chili"
        }, {
            "name": "Sky Store"
        }, {
            "name": "Amazon Video"
        }, {
            "name": "YouTube"
        }, {
            "name": "maxdome Store"
        }, {
            "name": "Rakuten TV"
        }, {
            "name": "EntertainTV"
        }, {
            "name": "Microsoft Store"
        }],
        "cast": [{
            "name": "Edward Norton",
            "role": "The Narrator",
            "image": "/5XBzD5WuTyVQZeS4VI25z2moMeY.jpg",
            "job": "Acting"
        }],
        "directors": [{
            "name": "Christopher Nolan"
        }],
        "tmdb_url":
        "https://www.themoviedb.org/movie/508442",
        "watch_status":
        "WATCHED",
        "rating_user":
        7.9,
        "favorite":
        True
    }

    movie1 = Movie.from_dict(dict)
    movie2 = Movie.from_dict(dict)

    assert movie1 == movie2
