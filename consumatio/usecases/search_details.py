
def search_details(tmdb, str):
    dict_search_details = tmdb.get_search_details(str)

    # "media_type": dict_search_details.get("media_type"),
    # "code": dict_search_details.get("code"),
    # "title": dict_search_details.get("title"),
    # "overview": dict_search_details.get("overview"),
    # "releaseDate": dict_search_details.get("release_date"),
    # "posters": dict_search_details.get("posters"),
    # "numberOfSeasons": dict_search_details.get(),
    # "watchStatus": None

    return dict_search_details
