from consumatio.entities.season import Season


class SeasonDetails:
    def get_season_details(self, tmdb, code, season_number):
        dict_season_details = tmdb.get_season_details(code, season_number)
        dict_season_images = tmdb.get_season_images(code, season_number)

        dict = {
            "code": dict_season_details.get("code"),
            "tvCode": code,
            "seasonNumber": dict_season_details.get("season_number"),
            "title": dict_season_details.get("name"),
            "overview": dict_season_details.get("overview"),
            "posterPath": dict_season_images.get("poster"),
            "watchStatus": None,
            "ratingUser": None,
            "favorite": None
        }

        return dict
