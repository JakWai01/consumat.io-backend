def tv_details_to_dict(data):
    dict = {
        "code": data["id"],
        "name": data["original_name"],
        "genres": data["genres"],
        "overview": data["overview"],
        "popularity": data["popularity"],
        "vote_average": data["vote_average"],
        "first_air_date": data["first_air_date"],
        "last_air_date": data["last_air_date"],
        "status": data["status"]
    }

    return dict