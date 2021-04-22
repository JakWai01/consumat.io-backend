def movie_details_to_dict(data):
    genre_list = []

    for index in range(len(data["genres"])):
        genre = {"name": data["genres"][index].get("name")}
        genre_list.append(genre)

    dict = {
        "code": data["id"],
        "title": data["original_title"],
        "genres": genre_list,
        "overview": data["overview"],
        "popularity": data["popularity"],
        "vote_average": data["vote_average"],
        "release_date": data["release_date"],
        "runtime": data["runtime"],
        "status": data["status"]
    }

    return dict
