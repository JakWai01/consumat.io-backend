
def search_details(tmdb, str):
    dict_search_details = tmdb.get_search_details(str)

    array = []
    for element in dict_search_details:
        for values in element:
            if dict_search_details.get("media_type") == "movie":
                dict = {
                    "media_type": dict_search_details.get("media_type"),
                    "code": dict_search_details.get("code"),
                    "title": dict_search_details.get("title"),
                    "genres": dict_search_details.get("genres"),
                    "overview": dict_search_details.get("overview"),
                    "popularity": dict_search_details.get("popularity"),
                    "voteAverage": dict_search_details.get("vote_average"),
                    "releaseDate": dict_search_details.get("release_date"),
                    "runtime": dict_search_details.get("runtime"),
                    "status": dict_search_details.get("status"),
                    "backdrops": dict_search_details.get("backdrops"),
                    "posters": dict_search_details.get("posters"),
                    "providers": dict_search_details.get("providers"),
                    "watchStatus": None,
                    "rating": None,
                    "favorite": None
                }

            elif dict_search_details.get("media_type") == "tv":
                dict = {
                    "media_type": dict_search_details.get("media_type"),
                    "code": dict_search_details.get("code"),
                    "name": dict_search_details.get("name"),
                    "genres": dict_search_details.get("genres"),
                    "overview": dict_search_details.get("overview"),
                    "popularity": dict_search_details.get("popularity"),
                    "voteAverage": dict_search_details.get("vote_average"),
                    "firstAirDate": dict_search_details.get("first_air_date"),
                    "lastAirDate": dict_search_details.get("last_air_date"),
                    "status": dict_search_details.get("status"),
                    "backdrops": dict_search_details.get("backdrops"),
                    "posters": dict_search_details.get("posters"),
                    "providers": dict_search_details.get("providers"),
                    "watchStatus": None,
                    "rating": None,
                    "favorite": None
                }
            array.append(dict)
    return array
