class TVSeasonDetails:
    def get_tv_season_details(self, tmdb: object, code: int):
        tv_details = tmdb.get_tv_details(code)

        number_of_seasons = tv_details.get("number_of_seasons")

        result = []
        for i in range(1, number_of_seasons):
            season = tmdb.get_season_details(code, i)
            result.append(season)

        return result