def tv_images_to_dict(data):
    dict = {
        "backdrops": str(data['backdrops']),
        "posters": str(data['posters'])
    }

    return dict