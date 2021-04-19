
def search_result_to_dict(data):

    # TODO @Danny: check if enumeration of api-data works
    results = data["results"]
    result_list = []
    results_filtered = []

    for result in results:
        if result.get("media_type") == "tv" or result.get("media_type") == "movie":
            results_filtered.append(result)

    for result in results_filtered:
        cache = []
        cache.append(result.get("id"))
        cache.append(result.get("media_type"))
        if result.get("media_type") == "tv":
            cache.append(result.get("name"))
        else:
            cache.append(result.get("titel"))
        cache.append(result.get("overview"))
        if result.get("media_type") == "tv":
            cache.append(result.get("first_air_date"))
        else:
            cache.append(result.get("release_date"))
        cache.append(result.get("poster_path"))
        if result.get("media_type") == "tv":
            cache.append("Number of Seasons")
        cache.append("Watchstatus")

        result_list.append(cache)

    return result_list
