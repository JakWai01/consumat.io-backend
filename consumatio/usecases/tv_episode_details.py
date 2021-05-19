class TVEpisodeDetails:
    def get_tv_episode_details(self, tmdb, code, season_number):
        season_details = tmdb.get_season_details(code, season_number)

        number_of_episodes = season_details.get("number_of_episodes")

        result = []
        for i in range(1, number_of_episodes + 1):
            episode = tmdb.get_episode_details(code, season_number, i)
            result.append(episode)

        return result