def movie_images_to_dict(data):
    dict = {
        "backdrops": data['backdrops'],
        "posters": data['posters']
    }

    return dict