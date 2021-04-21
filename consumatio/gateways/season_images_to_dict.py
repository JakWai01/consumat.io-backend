def season_images_to_dict(data):
    posters = data['posters']
    poster_list = []

    for poster in posters:
        if poster.get("iso_639_1") == "en":
            poster_list.append(poster)

    poster = None

    if len(poster_list) != 0:
        poster =  str(poster_list[0].get("file_path"))

    dict = {
        "posters": poster
    }

    return dict