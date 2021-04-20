import consumatio.external.api as Api


def search_result_to_dict(data):

    # TODO @Danny: check if enumeration of api-data works
    results = data["results"]
    result_list = []
    # results_filtered = []

    for result in results:
        if result.get("media_type") == "tv":
            tmp = Api.resolve_tv(code=result.get("id"), country="DE")
            dict = {
                "code": result.get("id"),
                "media_type": result.get("media_type"),
                "title": result.get("name"),
                "overview": result.get("overview"),
                "release_date": result.get("first_air_date"),
                "poster_path": result.get("poster_path"),
                "season_count": tmp.get("season_number"),
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
                "season_count": None,
                "watch_status": None
            }
        result_list.append(dict)
    return result_list
