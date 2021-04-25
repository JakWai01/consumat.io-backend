from consumatio.gateways.movie_gateways.movie_images_to_dict import *


def test_movie_images_to_dict():
    json = {
        "id":
        550,
        "backdrops": [{
            "aspect_ratio": 1.77777777777778,
            "file_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
            "height": 720,
            "iso_639_1": None,
            "vote_average": 0,
            "vote_count": 0,
            "width": 1280
        }],
        "posters": [{
            "aspect_ratio": 0.666666666666667,
            "file_path": "/fpemzjF623QVTe98pCVlwwtFC5N.jpg",
            "height": 1800,
            "iso_639_1": "en",
            "vote_average": 0,
            "vote_count": 0,
            "width": 1200
        }]
    }

    dict = {
        'backdrop': '/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg',
        'poster': '/fpemzjF623QVTe98pCVlwwtFC5N.jpg'
    }

    assert movie_images_to_dict(json) == dict
