def episode_images_to_dict(data):

    if "stills" not in data:
        return {
         "still": None   
        }

    stills = data['stills']

    if len(data['stills']) == 0:
        return {
            "still": None
        }
    
    dict = {
        "still": str(stills[0].get("file_path"))
    }

    return dict