from consumatio.entities.episode import Episode


def test_episode():
    episode = Episode(
        air_date="2011-04-17",
        episode_number=1,
        name="Winter Is Coming",
        overview="Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        code=63056,
        season_number=1,
        still_path="/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        vote_averag=7.11904761904762,
        vote_count=21,
        watch_status="WATCHED"
    )

    assert episode.air_date == "2011-04-17"
    assert episode.episode_number == 1
    assert episode.name == "Winter Is Coming"
    assert episode.overview == "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."
    assert episode.code == 63056
    assert episode.season_number == 1
    assert episode.still_path == "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg"
    assert episode.vote_average == 7.11904761904762
    assert episode.vote_count == 21
    assert episode.watch_status == "WATCHED"


def test_movie_from_dict():
    dict = {
        "air_date": "2011-04-17",
        "episode_number": 1,
        "name": "Winter Is Coming",
        "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "code": 63056,
        "season_number": 1,
        "still_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "vote_averag": 7.11904761904762,
        "vote_count": 21,
        "watch_status": "WATCHED"
    }

    episode = Episode.from_dict(dict)

    assert episode.air_date == "2011-04-17"
    assert episode.episode_number == 1
    assert episode.name == "Winter Is Coming"
    assert episode.overview == "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."
    assert episode.code == 63056
    assert episode.season_number == 1
    assert episode.still_path == "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg"
    assert episode.vote_average == 7.11904761904762
    assert episode.vote_count == 21
    assert episode.watch_status == "WATCHED"


def test_episode_to_dict():
    dict = {
        "air_date": "2011-04-17",
        "episode_number": 1,
        "name": "Winter Is Coming",
        "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "code": 63056,
        "season_number": 1,
        "still_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "vote_averag": 7.11904761904762,
        "vote_count": 21,
        "watch_status": "WATCHED"
    }

    episode = Episode.from_dict(dict)

    assert episode.to_dict() == dict


def test_episode_model_comparison():
    dict = {
        "air_date": "2011-04-17",
        "episode_number": 1,
        "name": "Winter Is Coming",
        "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "code": 63056,
        "season_number": 1,
        "still_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "vote_averag": 7.11904761904762,
        "vote_count": 21,
        "watch_status": "WATCHED"
    }

    episode1 = Episode.from_dict(dict)
    episode2 = Episode.from_dict(dict)

    assert episode1 == episode2
