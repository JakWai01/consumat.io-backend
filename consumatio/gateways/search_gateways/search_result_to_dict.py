def search_result_to_dict(data: dict) -> dict:
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
            if result.get("media_type") == "tv":
                dict = {
                    "code": result.get("id"),
                    "media_type": result.get("media_type"),
                    "title": result.get("name"),
                    "overview": result.get("overview"),
                    "release_date": result.get("first_air_date"),
                    "poster_path": result.get("poster_path"),
                    "watch_status": None
                }
            elif result.get("media_type") == "movie":
                dict = {
                    "code": result.get("id"),
                    "media_type": result.get("media_type"),
                    "title": result.get("title"),
                    "overview": result.get("overview"),
                    "release_date": result.get("release_date"),
                    "poster_path": result.get("poster_path"),
                    "watch_status": None
                }
            result_list.append(dict)
        return result_list
