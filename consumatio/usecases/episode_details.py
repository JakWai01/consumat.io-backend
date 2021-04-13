from consumatio.entities.episode import Episode

def episode_details(tmdb, code, season_number, episode_number):
    dict_episode_details = tmdb.get_episode_details(code, season_number, episode_number)
    dict_episode_images = tmdb.get_episode_images(code, season_number, episode_number)

    dict = {
        "code": dict_episode_details.get("code"),
        "name": dict_episode_details.get("name"), 
        "episode_number": dict_episode_details.get("episode_number"),
        "season_number": season_number,
        "overview": dict_episode_details.get("overview"),
        "air_date": dict_episode_details.get("air_date"),
        "vote_average": dict_episode_details.get("vote_average"),
        "stills": dict_episode_images.get("stills"),
        "watch_status": None,
        "rating": None,
        "favorite": None,
    }

    episode = Episode.from_dict(dict)

    return episode.to_dict()