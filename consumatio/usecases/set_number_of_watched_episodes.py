def set_number_of_watched_episodes(tmdb: object, database: object,
                                   external_id: str, code: int,
                                   seasonNumber: int,
                                   numberOfWatchedEpisodes: int) -> dict:
    """
    :param tmdb: <object> TMDB object to make API requests
    :param database: <object> Database object to access the database
    :param external_id: <str> External ID provided by OAuth
    :param code: <int> Code of the media to query
    :param seasonNumber: <int> Number of season to set numberOfWatchedEpisodes for
    :param numberOfWatchedEpisodes: <int> Number of watched episodes of specified season
    :return: <dict> Successful response
    """
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    data = tmdb.get_season_details(code, seasonNumber)

    if not database.media_data_exists(user_id, "Season", data.get("code")):
        database.media_Data(user_id, "Season", data.get("code"), code)

    database.number_of_watched_episodes(user_id, data.get("code"),
                                        numberOfWatchedEpisodes)
    return {"status": True}