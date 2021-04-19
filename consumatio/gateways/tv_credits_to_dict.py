def tv_credits_to_dict(data):
    cast = data["cast"]
    cast_list = []

    for castmember in cast: 
        member = []
        member.append(castmember.get("name"))
        member.append(castmember.get("character"))
        member.append(castmember.get("profile_path"))
        member.append(castmember.get("known_for_department"))

        cast_list.append(member)

    dict = {
        "cast": cast_list
    }

    return dict