def movie_credits_to_dict(data):
    cast = data["cast"]
    crew = data["crew"]
    cast_list = []
    directors_list = []

    for castmember in cast:
        member = []
        member.append(castmember.get("name"))
        member.append(castmember.get("character"))
        member.append(castmember.get("profile_path"))
        member.append(castmember.get("known_for_department"))

        cast_list.append(member)

    for crewmember in crew:
        director = []

        if crewmember.get("job") == "Director":
            director.append(crewmember.get("name"))
            director.append(crewmember.get("profile_path"))

            directors_list.append(director)

    dict = {
        "cast": cast_list,
        "directors": directors_list
    }

    return dict