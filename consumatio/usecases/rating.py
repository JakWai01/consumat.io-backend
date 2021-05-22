class Rating:
    def rating(self, tmdb, database, external_id, media, code, seasonNumber,
               episodeNumber, rating):
        user_id = 0

        if not database.user_exists(external_id):
            database.user(external_id)
        user_id = database.get_user_id(external_id)

        if media == "Season":
            code = tmdb.get_season_details(code, seasonNumber).get("code")

        if media == "Episode":
            code = tmdb.get_episode_details(code, seasonNumber,
                                            episodeNumber).get("code")

        if not database.media_data_exists(user_id, media, code):
            database.media_Data(user_id, media, code)

        database.rating(user_id, media, code, rating)
        return {"status": True}