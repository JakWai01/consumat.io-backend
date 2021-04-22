from consumatio.entities.tv import TV

def test_tv():
    tv = TV(
        code = 1399,
        name = "Game of Thrones",
        genres  = [
            {
            "name": "Sci-Fi & Fantasy"
            }
        ],
        overview = "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
        popularity =  369.594,
        vote_average = 8.3,
        first_air_date = "2011-04-17",
        last_air_date = "2019-05-19",
        status = "Ended",
        backdrop = "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg",
        poster = "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg",
        providers = [{
            "name": "netflix"
        }],
        creators = [{
            "name": "Hans Werner Sinn"
        }],
        cast = [{
            "name": "edward norton",
            "role": "the narrator",
            "image": "/5xbzd5wutyvqzes4vi25z2momey.jpg",
            "job": "acting"
        }],
        number_of_episodes = 60,
        number_of_seasons = 8,
        tmdb = "https://www.themoviedb.org/movie/508442",
        watch_status = "WATCHED",
        rating = 7.7,
        favorite = False
    )

    assert tv.code == 1399
    assert tv.name == "Game of Thrones"
    assert tv.genres == [
        {
        "name": "Sci-Fi & Fantasy"
        }
    ]
    assert tv.overview == "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond."
    assert tv.popularity == 369.594
    assert tv.vote_average == 8.3
    assert tv.first_air_date == "2011-04-17"
    assert tv.last_air_date == "2019-05-19"
    assert tv.status == "Ended"
    assert tv.backdrop == "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg"
    assert tv.poster == "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg"
    assert tv.providers == [{
            "name": "netflix"
        }]
    assert tv.creators == [{
            "name": "Hans Werner Sinn"
        }]
    assert tv.cast == [{
            "name": "edward norton",
            "role": "the narrator",
            "image": "/5xbzd5wutyvqzes4vi25z2momey.jpg",
            "job": "acting"
        }]
    assert tv.number_of_episodes == 60
    assert tv.number_of_seasons == 8
    assert tv.tmdb == "https://www.themoviedb.org/movie/508442"
    assert tv.watch_status == "WATCHED"
    assert tv.rating == 7.7
    assert tv.favorite == False

def test_tv_from_dict():
    dict = {
        "code" : 1399,
        "name" : "Game of Thrones",
        "genres" : [
            {
            "name": "Sci-Fi & Fantasy"
            }
        ],
        "overview" : "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
        "popularity" :  369.594,
        "vote_average" : 8.3,
        "first_air_date" : "2011-04-17",
        "last_air_date" : "2019-05-19",
        "status" : "Ended",
        "backdrop" : "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg",
        "poster" : "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg",
        "providers" : [{
            "name": "netflix"
        }],
        "creators" : [{
            "name": "Hans Werner Sinn"
        }],
        "cast" : [{
            "name": "edward norton",
            "role": "the narrator",
            "image": "/5xbzd5wutyvqzes4vi25z2momey.jpg",
            "job": "acting"
        }],
        "number_of_episodes" : 60,
        "number_of_seasons" : 8,
        "tmdb" : "https://www.themoviedb.org/movie/508442", 
        "watch_status" : "WATCHED",
        "rating" : 7.7,
        "favorite" : False
    }

    tv = TV.from_dict(dict)

    assert tv.code == 1399
    assert tv.name == "Game of Thrones"
    assert tv.genres == [
        {
        "name": "Sci-Fi & Fantasy"
        }
    ]
    assert tv.overview == "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond."
    assert tv.popularity == 369.594
    assert tv.vote_average == 8.3
    assert tv.first_air_date == "2011-04-17"
    assert tv.last_air_date == "2019-05-19"
    assert tv.status == "Ended"
    assert tv.backdrop == "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg"
    assert tv.poster == "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg"
    assert tv.providers == [{
            "name": "netflix"
        }]
    assert tv.creators == [{
            "name": "Hans Werner Sinn"
        }]
    assert tv.cast == [{
            "name": "edward norton",
            "role": "the narrator",
            "image": "/5xbzd5wutyvqzes4vi25z2momey.jpg",
            "job": "acting"
        }]
    assert tv.number_of_episodes == 60
    assert tv.number_of_seasons == 8
    assert tv.tmdb == "https://www.themoviedb.org/movie/508442"
    assert tv.watch_status == "WATCHED"
    assert tv.rating == 7.7
    assert tv.favorite == False
    
def test_tv_to_dict():
    dict = {
        "code" : 1399,
        "name" : "Game of Thrones",
        "genres" : [
            {
            "name": "Sci-Fi & Fantasy"
            }
        ],
        "overview" : "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
        "popularity" :  369.594,
        "vote_average" : 8.3,
        "first_air_date" : "2011-04-17",
        "last_air_date" : "2019-05-19",
        "status" : "Ended",
        "backdrop" : "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg",
        "poster" : "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg",
        "providers" : [{
            "name": "netflix"
        }],
        "creators" : [{
            "name": "Hans Werner Sinn"
        }],
        "cast" : [{
            "name": "edward norton",
            "role": "the narrator",
            "image": "/5xbzd5wutyvqzes4vi25z2momey.jpg",
            "job": "acting"
        }],
        "number_of_episodes" : 60,
        "number_of_seasons" : 8,
        "tmdb" : "https://www.themoviedb.org/movie/508442", 
        "watch_status" : "WATCHED",
        "rating" : 7.7,
        "favorite" : False
    } 

    tv = TV.from_dict(dict)

    assert tv.to_dict() == dict

def test_tv_model_comparison():
    dict = {
        "code" : 1399,
        "name" : "Game of Thrones",
        "genres" : [
            {
            "name": "Sci-Fi & Fantasy"
            }
        ],
        "overview" : "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
        "popularity" :  369.594,
        "vote_average" : 8.3,
        "first_air_date" : "2011-04-17",
        "last_air_date" : "2019-05-19",
        "status" : "Ended",
        "backdrop" : "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg",
        "poster" : "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg",
        "providers" : [{
            "name": "netflix"
        }],
        "creators" : [{
            "name": "Hans Werner Sinn"
        }],
        "cast" : [{
            "name": "edward norton",
            "role": "the narrator",
            "image": "/5xbzd5wutyvqzes4vi25z2momey.jpg",
            "job": "acting"
        }],
        "number_of_episodes" : 60,
        "number_of_seasons" : 8,
        "tmdb" : "https://www.themoviedb.org/movie/508442", 
        "watch_status" : "WATCHED",
        "rating" : 7.7,
        "favorite" : False
    }

    tv1 = TV.from_dict(dict)
    tv2 = TV.from_dict(dict)

    assert tv1 == tv2
