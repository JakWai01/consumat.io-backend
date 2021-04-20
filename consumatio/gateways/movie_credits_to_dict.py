def movie_credits_to_dict(data):
    cast = data["cast"]
    crew = data["crew"]
    cast_list = []
    directors_list = []

    for castmember in cast:
        member = {
            "name": castmember.get("name"),
            "role": castmember.get("character"),
            "image": castmember.get("profile_path"),
            "job": castmember.get("known_for_department")
        } 
        
        cast_list.append(member)

    for crewmember in crew:
        director = {
            "name": crewmember.get("name"),
            "image": crewmember.get("profile_path")
        }

        if crewmember.get("job") == "Director":
            directors_list.append(director)

    dict = {
        "cast": cast_list,
        "directors": directors_list
    }

    return dict