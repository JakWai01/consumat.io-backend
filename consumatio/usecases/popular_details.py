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
        dict = {}
        if type == "Movie":
            dict_movie_results = tmdb.get_popular_movies(country, user, page)
            dict_search_total_pages = tmdb.get_popular_movies_total_pages(
                country, page)
            dict = {
                "total_pages": dict_search_total_pages.get("total_pages"),
                "results": dict_movie_results.get("results")
            }

        elif type == "TV":
            dict_tv_results = tmdb.get_popular_tv(user, page)
            dict_search_total_pages = tmdb.get_popular_tv_total_pages(page)
            dict = {
                "total_pages": dict_search_total_pages.get("total_pages"),
                "results": dict_tv_results.get("results")
            }

        return dict
