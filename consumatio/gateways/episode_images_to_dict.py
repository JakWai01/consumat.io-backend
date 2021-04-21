def episode_images_to_dict(data):

    if "stills" not in data:
        return {
         "stills": None   
        }

    stills = data['stills']

    if len(data['stills']) == 0:
        return {
            "stills": None
        }
    
    dict = {
        "stills": str(stills[0].get("file_path"))
    }

    return dict