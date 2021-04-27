from consumatio.entities.tv import TV


class TVDetails:
    def get_tv_details(self, tmdb, code, country):
        dict_tv_details = tmdb.get_tv_details(code)
        dict_tv_images = tmdb.get_tv_images(code)
        dict_tv_providers = tmdb.get_tv_providers(code, country)
        dict_tv_credits = tmdb.get_tv_credits(code)

        dict = {
            "code": dict_tv_details.get("code"),
            "title": dict_tv_details.get("name"),
            "genres": dict_tv_details.get("genres"),
            "overview": dict_tv_details.get("overview"),
            "popularity": dict_tv_details.get("popularity"),
            "ratingAverage": dict_tv_details.get("vote_average"),
            "firstAirDate": dict_tv_details.get("first_air_date"),
            "lastAirDate": dict_tv_details.get("last_air_date"),
            "status": dict_tv_details.get("status"),
            "backdropPath": dict_tv_images.get("backdrop"),
            "posterPath": dict_tv_images.get("poster"),
            "providers": dict_tv_providers.get("providers"),
            "cast": dict_tv_credits.get("cast"),
            "creators": dict_tv_details.get("creators"),
            "numberOfEpisodes": dict_tv_details.get("number_of_episodes"),
            "numberOfSeasons": dict_tv_details.get("number_of_seasons"),
            "tmdbUrl":
            f'https://www.themoviedb.org/tv/{dict_tv_details.get("code")}',
            "watchStatus": None,
            "ratingUser": None,
            "favorite": None
        }

        return dict
