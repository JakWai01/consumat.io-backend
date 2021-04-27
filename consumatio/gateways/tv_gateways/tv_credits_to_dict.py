def tv_credits_to_dict(data):
    cast = data["cast"]
    cast_list = []

    for castmember in cast:
        member = {
            "name": castmember.get("name"),
            "role": castmember.get("character"),
            "imagePath": castmember.get("profile_path"),
            "job": castmember.get("known_for_department")
        }

        cast_list.append(member)

    dict = {"cast": cast_list}

    return dict