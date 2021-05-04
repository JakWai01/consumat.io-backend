def movie_details_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
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
        "rating_average": data["vote_average"],
        "release_date": data["release_date"],
        "runtime": data["runtime"],
        "status": data["status"],
        "backdrop_path": data["backdrop_path"],
        "poster_path": data["poster_path"],
    }

    return dict
