def movie_credits_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    cast = data["cast"]
    crew = data["crew"]
    cast_list = []
    directors_list = []

    for castmember in cast:
        member = {
            "code": castmember.get("id"),
            "name": castmember.get("name"),
            "role": castmember.get("character"),
            "image_path": castmember.get("profile_path"),
            "job": castmember.get("known_for_department")
        }

        cast_list.append(member)

    for crewmember in crew:
        if crewmember.get("job") == "Director":
            director = {
                "code": castmember.get("id"),
                "name": crewmember.get("name"),
                "image_path": crewmember.get("profile_path")
            }

            directors_list.append(director)

    dict = {"cast": cast_list, "directors": directors_list}

    return dict