from consumatio.gateways.episode_gateways.episode_details_to_dict import *


def test_episode_details_to_dict():
    json = {
        "air_date":
        "2011-04-17",
        "crew": [{
            "id": 44797,
            "credit_id": "5256c8a219c2956ff6046e77",
            "name": "Tim Van Patten",
            "department": "Directing",
            "job": "Director",
            "profile_path": "/6b7l9YbkDHDOzOKUFNqBVaPjcgm.jpg"
        }],
        "episode_number":
        1,
        "guest_stars": [{
            "id": 117642,
            "name": "Jason Momoa",
            "credit_id": "5256c8a219c2956ff6046f40",
            "character": "Khal Drogo",
            "order": 0,
            "profile_path": "/PSK6GmsVwdhqz9cd1lwzC6a7EA.jpg"
        }],
        "name":
        "Winter Is Coming",
        "overview":
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        "id":
        63056,
        "production_code":
        "101",
        "season_number":
        1,
        "still_path":
        "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
        "vote_average":
        7.11904761904762,
        "vote_count":
        21
    }

    dict = {
        'code': 63056,
        'title': 'Winter Is Coming',
        'episode_number': 1,
        'season_number': 1,
        'overview':
        "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
        'air_date': '2011-04-17',
        'rating_average': 7.11904761904762,
        'still_path': '/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg'
    }

    assert episode_details_to_dict(json) == dict
