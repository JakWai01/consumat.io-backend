from consumatio.gateways.season_gateways.season_details_to_dict import *


def test_season_details_to_dict():
    json = {
        "_id": "5256c89f19c2956ff6046d47",
        "air_date": "2011-04-17",
        "name": "Season 1",
        "overview":
        "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring.",
        "id": 3624,
        "poster_path": "/zwaj4egrhnXOBIit1tyb4Sbt3KP.jpg",
        "season_number": 1
    }

    dict = {
        'code':
        3624,
        'tv_code':
        1399,
        'season_number':
        1,
        'name':
        'Season 1',
        'overview':
        "Trouble is brewing in the Seven Kingdoms of Westeros. For the driven inhabitants of this visionary world, control of Westeros' Iron Throne holds the lure of great power. But in a land where the seasons can last a lifetime, winter is coming...and beyond the Great Wall that protects them, an ancient evil has returned. In Season One, the story centers on three primary areas: the Stark and the Lannister families, whose designs on controlling the throne threaten a tenuous peace; the dragon princess Daenerys, heir to the former dynasty, who waits just over the Narrow Sea with her malevolent brother Viserys; and the Great Wall--a massive barrier of ice where a forgotten danger is stirring."
    }

    assert season_details_to_dict(json, 1399) == dict
