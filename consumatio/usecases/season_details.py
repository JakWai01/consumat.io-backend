from consumatio.entities.season import Season

def season_details(tmdb, code, season_number):
    dict_season_details = tmdb.get_season_details(code, season_number)
    dict_season_images = tmdb.get_season_images(code, season_number)

    dict = {
        "code": dict_season_details.get("code"),
        "tvCode": code,
        "seasonNumber": dict_season_details.get("season_number"), 
        "name": dict_season_details.get("name"),
        "overview": dict_season_details.get("overview"),
        "poster": dict_season_images.get("poster"),
        "watchStatus": None,
        "rating": None,
        "favorite": None
    }

    return dict 