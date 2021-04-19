
def search_result_to_dict(data):

    # TODO @Danny: check if enumeration of api-data works
    array = []
    for idx, element in enumerate(data):
        if idx == 0:
            continue
        for values in element:
            if values.media_type == "movie":
                dict = {
                    "media_type": data["media_type"],
                    "code": data["id"],
                    "title": data["title"],
                    "genres": data["genres"],
                    "overview": data["overview"],
                    "popularity": data["popularity"],
                    "voteAverage": data["vote_average"],
                    "releaseDate": data["release_date"],
                    "runtime": data["runtime"],
                    "status": data["status"],
                    "backdrops": data["backdrops"],
                    "posters": data["posters"],
                    "providers": data["providers"],
                    "watchStatus": None,
                    "rating": None,
                    "favorite": None
                }

            elif values.media_type == "movie":
                dict = {
                    "code": data["id"],
                    "name": data["name"],
                    "genres": data["genres"],
                    "overview": data["overview"],
                    "popularity": data["popularity"],
                    "voteAverage": data["vote_average"],
                    "firstAirDate": data["first_air_date"],
                    "lastAirDate": data["last_air_date"],
                    "status": data["status"],
                    "backdrops": data["backdrops"],
                    "posters": data["posters"],
                    "providers": data["providers"],
                    "watchStatus": None,
                    "rating": None,
                    "favorite": None
                }
            array.append(dict)
    return array
