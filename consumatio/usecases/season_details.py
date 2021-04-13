from consumatio.entities.season import Season

def season_details(tmdb, code, season_number):
    dict_season_details = tmdb.get_season_details(code, season_number)
    dict_season_images = tmdb.get_season_images(code, season_number)

    dict = {
        "code": dict_season_details.get("code"),
        "tv_code": code,
        "season_number": dict_season_details.get("season_number"), 
        "name": dict_season_details.get("name"),
        "overview": dict_season_details.get("overview"),
        "posters": dict_season_images.get("posters"),
        "watch_status": None,
        "rating": None,
        "favorite": None
    }

    season = Season.from_dict(dict)

    return season.to_dict()