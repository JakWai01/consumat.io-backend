from consumatio.entities.tv import TV


class TVDetails:
    def get_tv_details(self: object, tmdb: object, code: int,
                       country: str) -> dict:
        """
        Make all relevant API requests for this usecase (details, images, providers, credits) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param code: <int> Id of the tv show to get data for
        :param country: <str> Country abbreveation of the country to get providers for (e.g. "DE" -> Germany)
        :return: <dict> TV details
        """
        dict_tv_details = tmdb.get_tv_details(code)
        # dict_tv_images = tmdb.get_tv_images(code)
        dict_tv_providers = tmdb.get_tv_providers(code, country)
        dict_tv_credits = tmdb.get_tv_credits(code)

        dict = {
            "code": dict_tv_details.get("code"),
            "title": dict_tv_details.get("title"),
            "genres": dict_tv_details.get("genres"),
            "overview": dict_tv_details.get("overview"),
            "popularity": dict_tv_details.get("popularity"),
            "rating_average": dict_tv_details.get("rating_average"),
            "first_air_date": dict_tv_details.get("first_air_date"),
            "last_air_date": dict_tv_details.get("last_air_date"),
            "status": dict_tv_details.get("status"),
            "backdrop_path": dict_tv_details.get("backdrop_path"),
            "poster_path": dict_tv_details.get("poster_path"),
            "providers": dict_tv_providers.get("providers"),
            "cast": dict_tv_credits.get("cast"),
            "creators": dict_tv_details.get("creators"),
            "number_of_episodes": dict_tv_details.get("number_of_episodes"),
            "number_of_seasons": dict_tv_details.get("number_of_seasons"),
            "tmdb_url":
            f'https://www.themoviedb.org/tv/{dict_tv_details.get("code")}',
            "watch_status": None,
            "rating_user": None,
            "favorite": None
        }

        tv = TV.from_dict(dict)

        return tv.to_dict()
