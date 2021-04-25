from consumatio.entities.episode import Episode


class EpisodeDetails:
    def get_episode_details(self, tmdb, code, season_number, episode_number):
        dict_episode_details = tmdb.get_episode_details(
            code, season_number, episode_number)
        dict_episode_images = tmdb.get_episode_images(code, season_number,
                                                      episode_number)

        dict = {
            "code": dict_episode_details.get("code"),
            "name": dict_episode_details.get("name"),
            "episodeNumber": dict_episode_details.get("episode_number"),
            "seasonNumber": season_number,
            "overview": dict_episode_details.get("overview"),
            "airDate": dict_episode_details.get("air_date"),
            "voteAverage": dict_episode_details.get("vote_average"),
            "still": dict_episode_images.get("still"),
            "watchStatus": None,
            "rating": None,
            "favorite": None,
        }

        return dict