from consumatio.entities.episode import Episode


def test_episode():
    episode = Episode(
        code=63056,
        title="Winter Is Coming",
        episode_number=1,
        season_number=1,
        overview=
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        air_date="2011-04-17",
        rating_average=7.11904761904762,
        still_path="/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        favorite=False,
    )

    assert episode.code == 63056
    assert episode.title == "Winter Is Coming"
    assert episode.episode_number == 1
    assert episode.season_number == 1
    assert episode.overview == "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."
    assert episode.air_date == "2011-04-17"
    assert episode.rating_average == 7.11904761904762
    assert episode.still_path == "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg"
    assert episode.favorite == False


def test_episode_from_dict():
    dict = {
        "code": 63056,
        "title": "Winter Is Coming",
        "episode_number": 1,
        "season_number": 1,
        "overview":
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "air_date": "2011-04-17",
        "rating_average": 7.11904761904762,
        "still_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "favorite": False
    }

    episode = Episode.from_dict(dict)

    assert episode.code == 63056
    assert episode.title == "Winter Is Coming"
    assert episode.episode_number == 1
    assert episode.season_number == 1
    assert episode.overview == "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."
    assert episode.air_date == "2011-04-17"
    assert episode.rating_average == 7.11904761904762
    assert episode.still_path == "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg"
    assert episode.favorite == False


def test_episode_to_dict():
    dict = {
        "code": 63056,
        "title": "Winter Is Coming",
        "episode_number": 1,
        "season_number": 1,
        "overview":
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "air_date": "2011-04-17",
        "rating_average": 7.11904761904762,
        "still_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "favorite": False
    }

    episode = Episode.from_dict(dict)

    assert episode.to_dict() == dict


def test_episode_model_comparison():
    dict = {
        "code": 63056,
        "title": "Winter Is Coming",
        "episode_number": 1,
        "season_number": 1,
        "overview":
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "air_date": "2011-04-17",
        "rating_average": 7.11904761904762,
        "still_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "favorite": False
    }

    episode1 = Episode.from_dict(dict)
    episode2 = Episode.from_dict(dict)

    assert episode1 == episode2
