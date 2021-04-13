def season_details_to_dict(data, tv_id):

    dict = {
        "code": data["id"],
        "tv_code": tv_id,
        "season_number": data["season_number"],
        "name": data["name"],
        "overview": data["overview"]
    }

    print(data["id"])

    return dict