def popular_tv_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    if "results" not in data:
        return []
    elif len(data["results"]) == 0:
        return []
    else:
        results = data["results"]
        result_list = []

        for result in results:
            dict = {
                "code": result.get("id"),
                "media_type": "tv",
                "title": result.get("name"),
                "overview": result.get("overview"),
                "release_date": result.get("first_air_date"),
                "poster_path": result.get("poster_path"),
                "watch_status": None
            }
            result_list.append(dict)
        return result_list
