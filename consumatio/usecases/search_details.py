class SearchDetails:
    def get_search_details(self: object, user: str, tmdb: object,
                           keyword: str) -> dict:
        """
        Make all relevant API request for this usecase (search) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param keyword: <str> Search string
        :return: <dict> Search details
        """
        dict_search_details = tmdb.get_search(user, keyword)
        return dict_search_details
