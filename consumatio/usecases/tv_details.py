from consumatio.entities.tv import TV

def tv_details(tmdb, code, country):
    dict_tv_details = tmdb.get_tv_details(code)
    dict_tv_images = tmdb.get_tv_images(code)
    dict_tv_providers = tmdb.get_tv_providers(code, country)

    dict = {
        "code": dict_tv_details.get("code"),
        "name": dict_tv_details.get("name"),
        "genres": dict_tv_details.get("genres"),
        "overview": dict_tv_details.get("overview"),
        "popularity": dict_tv_details.get("popularity"),
        "vote_average": dict_tv_details.get("vote_average"),
        "first_air_date": dict_tv_details.get("first_air_date"),
        "last_air_date": dict_tv_details.get("last_air_date"),
        "status": dict_tv_details.get("status"),
        "backdrops": dict_tv_images.get("backdrops"),
        "posters": dict_tv_images.get("posters"),
        "providers": dict_tv_providers.get("providers"),
        "watch_status": None,
        "rating": None,
        "favorite": None
    }

    tv = TV.from_dict(dict)

    return tv.to_dict()