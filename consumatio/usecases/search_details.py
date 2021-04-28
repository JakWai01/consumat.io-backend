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
                "mediaType": result.get("media_type"),
                "title": result.get("title"),
                "overview": result.get("overview"),
                "releaseDate": result.get("release_date"),
                "posterPath": result.get("poster_path"),
                "watchStatus": result.get("watch_status")
            }
            results.append(dict)
        return results
