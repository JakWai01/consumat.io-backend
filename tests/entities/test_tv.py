from consumatio.entities.tv import TV

def test_tv():
    tv = TV(
        code = 1399,
        name = "Game of Thrones",
        genres  = [
            {
            "id": 10765,
            "name": "Sci-Fi & Fantasy"
            }
        ],
        overview = "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
        popularity =  369.594,
        vote_average = 8.3,
        first_air_date = "2011-04-17",
        last_air_date = "2019-05-19",
        status = "Ended",
        backdrops = [
            {
                "aspect_ratio": 1.77777777777778,
                "file_path": "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg",
                "height": 1080,
                "iso_639_1": None,
                "vote_average": 5.6265664160401,
                "vote_count": 13,
                "width": 1920
            }
        ],
        posters = [
            {
                "aspect_ratio": 0.666666666666667,
                "file_path": "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg",
                "height": 3000,
                "iso_639_1": "en",
                "vote_average": 5.57744937055282,
                "vote_count": 24,
                "width": 2000
            }
        ],
        providers = [
            {
                "display_priority": 2,
                "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
                "provider_id": 2,
                "provider_name": "Apple iTunes"
            }
        ],
        watch_status = "WATCHED",
        rating = 7.7,
        favorite = False
    )

    assert tv.code == 1399
    assert tv.name == "Game of Thrones"
    assert tv.genres == [
        {
        "id": 10765,
        "name": "Sci-Fi & Fantasy"
        }
    ]
    assert tv.overview == "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond."
    assert tv.popularity == 369.594
    assert tv.vote_average == 8.3
    assert tv.first_air_date == "2011-04-17"
    assert tv.last_air_date == "2019-05-19"
    assert tv.status == "Ended"
    assert tv.backdrops == [
        {
            "aspect_ratio": 1.77777777777778,
            "file_path": "/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg",
            "height": 1080,
            "iso_639_1": None,
            "vote_average": 5.6265664160401,
            "vote_count": 13,
            "width": 1920
        }
    ]
    assert tv.posters == [
        {
            "aspect_ratio": 0.666666666666667,
            "file_path": "/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg",
            "height": 3000,
            "iso_639_1": "en",
            "vote_average": 5.57744937055282,
            "vote_count": 24,
            "width": 2000
        }
    ]
    assert tv.providers == [
        {
            "display_priority": 2,
            "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
            "provider_id": 2,
            "provider_name": "Apple iTunes"
        }
    ]
    assert tv.watch_status == "WATCHED"
    assert tv.rating == 7.7
    assert tv.favorite == False