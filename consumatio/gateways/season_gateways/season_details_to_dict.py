def season_details_to_dict(data: dict, tv_id: int) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :param tv_id: <int> Id of the TV show to show details for
    :return: <dict> Internal representation
    """

    number_of_episodes = 0

    if "episodes" in data:
        for i in range(len(data["episodes"])):
            number_of_episodes += 1

    dict = {
        "code": data["id"],
        "tv_code": tv_id,
        "season_number": data["season_number"],
        "name": data["name"],
        "overview": data["overview"],
        "air_date": data["air_date"],
        "number_of_episodes": number_of_episodes
    }

    return dict