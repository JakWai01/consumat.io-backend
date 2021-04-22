from consumatio.gateways.tv_providers_to_dict import *


def test_tv_providers_to_dict():
    json = {
        "id": 1399,
        "results": {
            "DE": {
                "link": "https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=DE",
                "buy": [
                    {
                        "display_priority": 2,
                        "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
                        "provider_id": 2,
                        "provider_name": "Apple iTunes"
                    }
                ],
                "flatrate": [
                    {
                        "display_priority": 8,
                        "logo_path": "/zLX0ExkHc8xJ9W4u9JgnldDQLKv.jpg",
                        "provider_id": 29,
                        "provider_name": "Sky Go"
                    }
                ]
            }
        }
    }

    dict = {
        'providers': [{
            "name": "Sky Go"
        }
        ]
    }
    assert tv_providers_to_dict(json, "DE") == dict
