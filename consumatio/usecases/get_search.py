def get_search(external_id: str, tmdb: object, keyword: str,
               page: int) -> dict:
    """
    Assemble search results
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param keyword: <str> Search string
    :param page: <int> Search page (minimum:1 maximum:1000)
    :return: <dict> Search details
    """
    dict_search_details = tmdb.get_search_result(external_id, keyword, page)
    dict = {
        "total_pages": dict_search_details.get("total_pages"),
        "results": dict_search_details.get("results")
    }
    return dict
