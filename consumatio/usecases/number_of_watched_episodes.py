def set_number_of_watched_episodes(tmdb, database, external_id, code,
                                   seasonNumber, numberOfWatchedEpisodes):
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    data = tmdb.get_season_details(code, seasonNumber)

    if not database.media_data_exists(user_id, "Season", data.get("code")):
        database.media_Data(user_id, "Season", data.get("code"))

    database.number_of_watched_episodes(user_id, data.get("code"),
                                        numberOfWatchedEpisodes)
    return {"status": True}