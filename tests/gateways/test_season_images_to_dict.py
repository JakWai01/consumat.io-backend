from consumatio.gateways.season_images_to_dict import *


def test_season_images_to_dict():
    json = {
        "id":
        3624,
        "posters": [{
            "aspect_ratio": 0.666666666666667,
            "file_path": "/olJ6ivXxCMq3cfujo1IRw30OrsQ.jpg",
            "height": 1425,
            "iso_639_1": "en",
            "vote_average": 5.37612146307798,
            "vote_count": 6,
            "width": 950
        }]
    }

    dict = {
        'posters':
        str([{
            'aspect_ratio': 0.666666666666667,
            'file_path': '/olJ6ivXxCMq3cfujo1IRw30OrsQ.jpg',
            'height': 1425,
            'iso_639_1': 'en',
            'vote_average': 5.37612146307798,
            'vote_count': 6,
            'width': 950
        }])
    }

    assert season_images_to_dict(json) == dict
