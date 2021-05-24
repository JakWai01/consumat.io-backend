def get_tv_episode_details(tmdb: object, code: int,
                           season_number: int) -> list:
    """
    Get a list of all episodes of a Season from a TV show
    :param tmdb: <object> tmdb object to make API requests
    :param code: <int> Id of the TV show
    :param season_number: <int> Number of the season from a certain TV show
    :return: <list> List of Episodes
    """
    season_details = tmdb.get_season_details(code, season_number)

    number_of_episodes = season_details.get("number_of_episodes")

    result = []
    for i in range(1, number_of_episodes + 1):
        episode = tmdb.get_episode_details(code, season_number, i)
        result.append(episode)

    return result