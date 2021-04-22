from consumatio.entities.season import Season


def test_season():
    season = Season(
        code=3624,
        tv_code=1399,
        season_number=1,
        name="Season 1",
        overview=
        "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring.",
        posters=[{
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }],
        watch_status="WATCHED",
        rating=6.6,
        favorite=False,
    )

    assert season.code == 3624
    assert season.tv_code == 1399
    assert season.season_number == 1
    assert season.name == "Season 1"
    assert season.overview == "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring."
    assert season.posters == [{
        "aspect_ratio": 0.666666666666667,
        "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
        "height": 1800,
        "iso_639_1": "en",
        "vote_average": 0,
        "vote_count": 0,
        "width": 1200
    }]
    assert season.watch_status == "WATCHED"
    assert season.rating == 6.6
    assert season.favorite == False


def test_season_from_dict():
    dict = {
        "code":
        3624,
        "tv_code":
        1399,
        "season_number":
        1,
        "name":
        "Season 1",
        "overview":
        "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring.",
        "posters": [{
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }],
        "watch_status":
        "WATCHED",
        "rating":
        6.6,
        "favorite":
        False,
    }

    season = Season.from_dict(dict)

    assert season.code == 3624
    assert season.tv_code == 1399
    assert season.season_number == 1
    assert season.name == "Season 1"
    assert season.overview == "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring."
    assert season.posters == [{
        "aspect_ratio": 0.666666666666667,
        "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
        "height": 1800,
        "iso_639_1": "en",
        "vote_average": 0,
        "vote_count": 0,
        "width": 1200
    }]
    assert season.watch_status == "WATCHED"
    assert season.rating == 6.6
    assert season.favorite == False


def test_season_to_dict():
    dict = {
        "code":
        3624,
        "tv_code":
        1399,
        "season_number":
        1,
        "name":
        "Season 1",
        "overview":
        "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring.",
        "posters": [{
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }],
        "watch_status":
        "WATCHED",
        "rating":
        6.6,
        "favorite":
        False,
    }

    season = Season.from_dict(dict)

    assert season.to_dict() == dict


def test_season_model_comparison():
    dict = {
        "code":
        3624,
        "tv_code":
        1399,
        "season_number":
        1,
        "name":
        "Season 1",
        "overview":
        "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring.",
        "posters": [{
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }],
        "watch_status":
        "WATCHED",
        "rating":
        6.6,
        "favorite":
        False,
    }

    season1 = Season.from_dict(dict)
    season2 = Season.from_dict(dict)

    assert season1 == season2
