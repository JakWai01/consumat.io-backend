def episode_images_to_dict(data):
    stills = data['stills']

    dict = {
        "stills": str(stills[0].get("file_path"))
    }
    return dict