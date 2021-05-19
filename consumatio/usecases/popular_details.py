class PopularDetails:
    def get_popular_details(self: object, user: str, tmdb: object, type: str,
                            country: str, page: int) -> dict:
        """
        Make all relevant API request for this usecase (popular items) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param type: <str> popular item type "movie" or "tv"
        :param country: <str> country code (uppercase) currently only applicable for movies
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> popular media
        """
        search_data = []
        if type == "Movie":
            search_data.extend(tmdb.get_popular_movies(country, user, page))

        elif type == "TV":
            search_data.extend(tmdb.get_popular_tv(user, page))

        return search_data
