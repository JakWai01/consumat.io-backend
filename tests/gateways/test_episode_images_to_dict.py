from consumatio.gateways.episode_images_to_dict import *


def test_episode_images_to_dict():
    json = {
        "id":
        63056,
        "stills": [{
            "aspect_ratio": 1.77777777777778,
            "file_path": "/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg",
            "height": 1080,
            "iso_639_1": None,
            "vote_average": 5.30505952380952,
            "vote_count": 1,
            "width": 1920
        }]
    }

    dict = {'still': '/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg'}

    assert episode_images_to_dict(json) == dict
