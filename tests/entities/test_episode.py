from consumatio.entities.episode import Episode


def test_episode():
    episode = Episode(
        code=63056,
        name="Winter Is Coming",
        episode_number=1,
        season_number=1,
        overview="Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        air_date="2011-04-17",
        vote_average=7.11904761904762,
        still = "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        watch_status="WATCHED",
        rating = 5.4,
        favorite = False
    )

    assert episode.code == 63056
    assert episode.name == "Winter Is Coming"
    assert episode.episode_number == 1
    assert episode.season_number == 1
    assert episode.overview == "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."
    assert episode.air_date == "2011-04-17"
    assert episode.vote_average == 7.11904761904762
    assert episode.still == "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg"
    assert episode.watch_status == "WATCHED"
    assert episode.rating == 5.4
    assert episode.favorite == False


def test_episode_from_dict():
    dict = {
        "code": 63056,
        "name": "Winter Is Coming",
        "episode_number": 1,
        "season_number": 1,
        "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "air_date": "2011-04-17",
        "vote_average": 7.11904761904762,
        "still": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "watch_status": "WATCHED",
        "rating": 5.4,
        "favorite": False
    }

    episode = Episode.from_dict(dict)

    assert episode.code == 63056
    assert episode.name == "Winter Is Coming"
    assert episode.episode_number == 1
    assert episode.season_number == 1
    assert episode.overview == "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."
    assert episode.air_date == "2011-04-17"
    assert episode.vote_average == 7.11904761904762
    assert episode.still == "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg"
    assert episode.watch_status == "WATCHED"
    assert episode.rating == 5.4
    assert episode.favorite == False


def test_episode_to_dict():
    dict = {
        "code": 63056,
        "name": "Winter Is Coming",
        "episode_number": 1,
        "season_number": 1,
        "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "air_date": "2011-04-17",
        "vote_average": 7.11904761904762,
        "still": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "watch_status": "WATCHED",
        "rating": 5.4,
        "favorite": False
    }

    episode = Episode.from_dict(dict)

    assert episode.to_dict() == dict


def test_episode_model_comparison():
    dict = {
        "code": 63056,
        "name": "Winter Is Coming",
        "episode_number": 1,
        "season_number": 1,
        "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "air_date": "2011-04-17",
        "vote_average": 7.11904761904762,
        "still": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "watch_status": "WATCHED",
        "rating": 5.4,
        "favorite": False
    }

    episode1 = Episode.from_dict(dict)
    episode2 = Episode.from_dict(dict)

    assert episode1 == episode2
