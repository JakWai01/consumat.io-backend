from consumatio.external.models import *
from sqlalchemy import text


class WatchCount:
    def get_watch_count(self: object, tmdb: object, user: str,
                        type: str) -> int:
        """
        Get count of watched media of a certain type (e.g. "Movie", "Season" or "Drama")
        :param tmdb: <object> TMDB object to make API requests
        :param user: <str> External id of the user
        :param type: <str> Type of the media to get count for (e.g. "Movie", "Season" or "Drama")
        :return: <int> Count of media watched
        """
        count = 0
        if type in "MovieEpisodeTVSeason":
            results = MediaData.query.from_statement(
                text(
                    "SELECT * FROM media_data, user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = :type AND user_data.external_id_content = :user AND media_data.watch_status_content = 'Finished';"
                )).params(user=user, type=type).all()

            for i in range(len(results)):
                count += 1
        else:
            results = MediaData.query.from_statement(
                text(
                    "SELECT * FROM media_data, user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND user_data.external_id_content = :user AND media_data.watch_status_content = 'Finished';"
                )).params(user=user, type=type).all()

            for result in results:
                if result.media_type_content == "Movie":
                    data = tmdb.get_movie_details(result.media_id_content)

                    for genre in data.get("genres"):
                        if genre.get("name") == type:
                            count += 1

                if result.media_type_content == "TV":
                    data = tmdb.get_tv_details(result.media_id_content)

                    for genre in data.get("genres"):
                        if genre.get("name") == type:
                            count += 1

        return count
