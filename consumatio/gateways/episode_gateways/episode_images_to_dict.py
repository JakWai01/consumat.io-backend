def episode_images_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    if "stills" not in data:
        return {"still": None}

    stills = data['stills']
    still_list = []

    if len(data['stills']) == 0:
        return {"still": None}

    for still in stills:
        if still.get("iso_639_1") == "en" or still.get("iso_639_1") == None:
            still_list.append(still)

    dict = {"still": str(still_list[0].get("file_path"))}

    return dict