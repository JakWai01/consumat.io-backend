from consumatio.entities.tv import TV


def tv_details(tmdb, code, country):
    dict_tv_details = tmdb.get_tv_details(code)
    dict_tv_images = tmdb.get_tv_images(code)
    dict_tv_providers = tmdb.get_tv_providers(code, country)
    dict_tv_credits = tmdb.get_tv_credits(code)

    creators = []
    for index in range(len(dict_tv_details.get("creators"))):
        creator = {
            "name": dict_tv_details.get("creators")[index][0],
            "image": dict_tv_details.get("creators")[index][1]
        }

        creators.append(creator)

    dict = {
        "code": dict_tv_details.get("code"),
        "name": dict_tv_details.get("name"),
        "genres": dict_tv_details.get("genres"),
        "overview": dict_tv_details.get("overview"),
        "popularity": dict_tv_details.get("popularity"),
        "voteAverage": dict_tv_details.get("vote_average"),
        "firstAirDate": dict_tv_details.get("first_air_date"),
        "lastAirDate": dict_tv_details.get("last_air_date"),
        "status": dict_tv_details.get("status"),
        "backdrop": dict_tv_images.get("backdrops"),
        "poster": dict_tv_images.get("posters"),
        "providers": dict_tv_providers.get("providers"),
        "cast": dict_tv_credits.get("cast"),
        "creators": creators,
        "numberOfEpisodes": dict_tv_details.get("number_of_episodes"),
        "numberOfSeasons": dict_tv_details.get("number_of_seasons"),
        "tmdb": f'https://www.themoviedb.org/tv/{dict_tv_details.get("code")}',
        "watchStatus": None,
        "rating": None,
        "favorite": None
    }

    return dict
