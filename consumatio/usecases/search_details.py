
def search_details(tmdb, str):
    dict_search_details = tmdb.get_search(str)
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
