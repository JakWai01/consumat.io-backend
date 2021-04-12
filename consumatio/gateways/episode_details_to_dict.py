def episode_details_to_dict(data):
    dict = {
        "code": data["id"],
        "name": data["name"],
        "episode_number": data["episode_number"],
        "season_number": data["season_number"],
        "overview": data["overview"],
        "air_data": data["air_date"],
        "vote_average": data["vote_average"],
        "vote_count": data["vote_count"],
        "still_path": data["still_path"]
    }

    return dict