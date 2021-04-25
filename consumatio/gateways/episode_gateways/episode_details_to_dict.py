def episode_details_to_dict(data):
    dict = {
        "code": data["id"],
        "name": data["name"],
        "episode_number": data["episode_number"],
        "season_number": data["season_number"],
        "overview": data["overview"],
        "air_date": data["air_date"],
        "vote_average": data["vote_average"]
    }

    return dict