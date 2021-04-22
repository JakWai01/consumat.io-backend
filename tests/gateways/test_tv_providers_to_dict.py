from consumatio.gateways.tv_providers_to_dict import *


def test_tv_providers_to_dict():
    json = {
        "link":
        "https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=AR",
        "flatrate": [{
            "display_priority": 4,
            "logo_path": "/2slPVV21kaPDx0NwjVtcUjdvzXz.jpg",
            "provider_id": 31,
            "provider_name": "HBO Go"
        }, {
            "display_priority": 7,
            "logo_path": "/rgbalNWbAuhWklHH5JAnF53Wjey.jpg",
            "provider_id": 339,
            "provider_name": "Movistar Play"
        }, {
            "display_priority": 14,
            "logo_path": "/lUv4RMq0WDcsePlqKPDwIDS1vCB.jpg",
            "provider_id": 467,
            "provider_name": "DIRECTV GO"
        }]
    }

    dict = {'providers': ['HBO Go', 'Movistar Play', 'DIRECTV GO']}

    assert tv_providers_to_dict(json, "DE") == dict
