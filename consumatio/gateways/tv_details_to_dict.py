def tv_details_to_dict(data):
    genre_list = []

    for index in range(len(data["genres"])):
        genre_list.append(data["genres"][index].get("name"))

    dict = {
        "code": data["id"],
        "name": data["original_name"],
        "genres": genre_list,
        "overview": data["overview"],
        "popularity": data["popularity"],
        "vote_average": data["vote_average"],
        "first_air_date": data["first_air_date"],
        "last_air_date": data["last_air_date"],
        "status": data["status"]
    }

    return dict