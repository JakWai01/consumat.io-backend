from consumatio.gateways.tv_images_to_dict import *


def test_tv_images_to_dict():
    json = {
        "backdrops": [
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
        "id": 1399,
        "posters": [
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
    }

    dict = {
        'backdrops': [
            {'aspect_ratio': 1.77777777777778, 'file_path': '/mUkuc2wyV9dHLG0D0Loaw5pO2s8.jpg', 'height': 1080,
                'iso_639_1': None, 'vote_average': 5.6265664160401, 'vote_count': 13, 'width': 1920}
        ],
        'posters': [
            {'aspect_ratio': 0.666666666666667, 'file_path': '/hDd5Zd9VMOqBeHa2agbnHZ98WWr.jpg', 'height': 3000,
                'iso_639_1': 'en', 'vote_average': 5.57744937055282, 'vote_count': 24, 'width': 2000}
        ]
    }

    assert tv_images_to_dict(json) == dict
