class SearchDetails:
    def get_search_details(self: object, tmdb: object, keyword: str) -> dict:
        """
        Make all relevant API request for this usecase (search) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param keyword: <str> Search string
        :return: <dict> Search details
        """
        dict_search_details = tmdb.get_search(keyword)
        results = []
        for result in dict_search_details:
            dict = {
                "code": result.get("code"),
                "media_type": result.get("media_type"),
                "title": result.get("title"),
                "overview": result.get("overview"),
                "release_date": result.get("release_date"),
                "poster_path": result.get("poster_path"),
                "watch_status": result.get("watch_status")
            }
            results.append(dict)
        return results
