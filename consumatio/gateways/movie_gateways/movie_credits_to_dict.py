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
            "name": castmember.get("name"),
            "role": castmember.get("character"),
            "imagePath": castmember.get("profile_path"),
            "job": castmember.get("known_for_department")
        }

        cast_list.append(member)

    for crewmember in crew:
        director = {
            "name": crewmember.get("name"),
            "imagePath": crewmember.get("profile_path")
        }

        if crewmember.get("job") == "Director":
            directors_list.append(director)

    dict = {"cast": cast_list, "directors": directors_list}

    return dict