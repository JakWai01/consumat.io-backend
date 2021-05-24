def get_search_details(user: str, tmdb: object, keyword: str,
                       page: int) -> dict:
    """
    Make all relevant API request for this usecase (search) and assemble them into a dictionary
    :param tmdb: <object> Tmdb object
    :param keyword: <str> Search string
    :param page: <int> Search page (minimum:1 maximum:1000)
    :return: <dict> Search details
    """
    dict_search_details = tmdb.get_search_result(user, keyword, page)
    dict = {
        "total_pages": dict_search_details.get("total_pages"),
        "results": dict_search_details.get("results")
    }
    return dict
