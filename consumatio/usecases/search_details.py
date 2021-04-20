
def search_details(tmdb, str):
    dict_search_details = tmdb.get_search(str)

    dict = {
        "code": dict_search_details.get("code"),
        "mediaType": dict_search_details.get("media_type"),
        "title": dict_search_details.get("title"),
        "overview": dict_search_details.get("overview"),
        "releaseDate": dict_search_details.get("release_date"),
        "posterPath": dict_search_details.get("poster_path"),
        "seasonCount": dict_search_details.get("season_count"),
        "watchStatus": dict_search_details.get("watch_status")
    }

    return dict_search_details
