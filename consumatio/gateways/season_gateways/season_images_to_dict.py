def season_images_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """

    posters = data['posters']
    poster_list = []

    for poster in posters:
        if poster.get("iso_639_1") == "en" or poster.get("iso_639_1") == None:
            poster_list.append(poster)

    poster = None

    if len(poster_list) != 0:
        poster = str(poster_list[0].get("file_path"))

    dict = {"poster": poster}

    return dict