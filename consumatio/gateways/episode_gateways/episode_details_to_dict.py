def episode_details_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    dict = {
        "code": data["id"],
        "title": data["name"],
        "episode_number": data["episode_number"],
        "season_number": data["season_number"],
        "overview": data["overview"],
        "air_date": data["air_date"],
        "rating_average": data["vote_average"],
        "still_path": data["still_path"]
    }

    return dict