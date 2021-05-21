class TVSeasonDetails:
    def get_tv_season_details(self: object, tmdb: object, code: int) -> list:
        """
        Get a list of all seasons of a TV show
        :param tmdb: <object> tmdb object to make API requests
        :param code: <int> Id of the TV show
        :return: <list> List of Seasons
        """
        tv_details = tmdb.get_tv_details(code)

        number_of_seasons = tv_details.get("number_of_seasons")

        result = []
        for i in range(1, number_of_seasons + 1):
            season = tmdb.get_season_details(code, i)
            result.append(season)

        return result