def tv_credits_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    cast = data["cast"]
    cast_list = []

    for castmember in cast:
        member = {
            "code": castmember.get("id"),
            "name": castmember.get("name"),
            "role": castmember.get("character"),
            "image_path": castmember.get("profile_path"),
            "job": castmember.get("known_for_department")
        }

        cast_list.append(member)

    dict = {"cast": cast_list}

    return dict