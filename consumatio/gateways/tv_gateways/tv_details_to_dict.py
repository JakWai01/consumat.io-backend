def tv_details_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    genre_list = []
    created_by_list = []

    for index in range(len(data["genres"])):
        genre = {"name": data["genres"][index].get("name")}
        genre_list.append(genre)

    for creator in data["created_by"]:
        creator_dict = {
            "name": creator["name"],
            "image_path": creator["profile_path"]
        }
        created_by_list.append(creator_dict)

    dict = {
        "code": data["id"],
        "title": data["name"],
        "genres": genre_list,
        "overview": data["overview"],
        "popularity": data["popularity"],
        "rating_average": data["vote_average"],
        "rating_count": data["vote_count"],
        "first_air_date": data["first_air_date"],
        "last_air_date": data["last_air_date"],
        "status": data["status"],
        "creators": created_by_list,
        "number_of_episodes": data["number_of_episodes"],
        "number_of_seasons": data["number_of_seasons"],
        "backdrop_path": data["backdrop_path"],
        "poster_path": data["poster_path"],
        "runtime": data["episode_run_time"][0]
    }

    return dict