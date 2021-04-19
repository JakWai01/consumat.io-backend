def movie_images_to_dict(data):
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

    dict = {
        "backdrops": str(backdrop_list[0].get("file_path")),
        "posters": str(poster_list[0].get("file_path"))
    }

    return dict