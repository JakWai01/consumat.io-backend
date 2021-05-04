from consumatio.entities.season import Season


class SeasonDetails:
    def get_season_details(self: object, tmdb: object, code: int,
                           season_number: int) -> dict:
        """
        Make all relevant API requests for this usecase (details, images) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param code: <int> Id of the tv_show to get season details for
        :param season_number: <int> Number of season to get details for
        :return: <dict> Season details
        """
        dict_season_details = tmdb.get_season_details(code, season_number)
        dict_season_images = tmdb.get_season_images(code, season_number)

        dict = {
            "code": dict_season_details.get("code"),
            "tv_code": code,
            "season_number": dict_season_details.get("season_number"),
            "title": dict_season_details.get("name"),
            "overview": dict_season_details.get("overview"),
            "poster_path": dict_season_details.get("poster_path"),
            "watch_status": None,
            "rating_user": None,
            "favorite": None,
            "number_of_episodes":
            dict_season_details.get("number_of_episodes"),
            "air_date": dict_season_details.get("air_date")
        }

        season = Season.from_dict(dict)

        return season.to_dict()
