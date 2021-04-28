from consumatio.entities.episode import Episode


class EpisodeDetails:
    def get_episode_details(self: object, tmdb: object, code: int, season_number: int, episode_number: int) -> dict:
        """
        Make all relevant API requests for this usecase (details, images) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param code: <int> Id of the tv show to get data for
        :param season_number: <int> Number of the season which includes the episode
        :param episode_number: <int> Number of the episode in the corresponding season
        :return: <dict> Episode details
        """
        dict_episode_details = tmdb.get_episode_details(
            code, season_number, episode_number)
        dict_episode_images = tmdb.get_episode_images(code, season_number,
                                                      episode_number)

        dict = {
            "code": dict_episode_details.get("code"),
            "title": dict_episode_details.get("name"),
            "episodeNumber": dict_episode_details.get("episode_number"),
            "seasonNumber": season_number,
            "overview": dict_episode_details.get("overview"),
            "airDate": dict_episode_details.get("air_date"),
            "ratingAverage": dict_episode_details.get("vote_average"),
            "stillPath": dict_episode_images.get("still"),
            "watchStatus": None,
            "ratingUser": None,
            "favorite": None,
        }

        return dict