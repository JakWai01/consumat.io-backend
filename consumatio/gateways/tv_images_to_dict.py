def tv_images_to_dict(data):
    posters = data['posters']
    backdrops = data['backdrops']
    poster_list = []
    backdrop_list = []

    for poster in posters:
        if poster.get("iso_639_1") == "en":
            poster_list.append(poster)

    for backdrop in backdrops:
        if backdrop.get("iso_639_1") == "en":
            backdrop_list.append(backdrop)

    poster = None

    if len(poster_list) != 0:
        poster = str(poster_list[0].get("file_path"))

    backdrop = None

    if len(backdrop_list) != 0:
        backdrop = str(backdrop_list[0].get("file_path"))

    dict = {"backdrops": backdrop, "posters": poster}

    return dict
