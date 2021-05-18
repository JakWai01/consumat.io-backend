from consumatio.external.models import *
from sqlalchemy import text


class WatchTime:
    def get_watch_time(self, tmdb, user, type):
        runtime = 0
        if type == "Movie":
            results = MediaData.query.from_statement(
                text(
                    "SELECT * FROM media_data, user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = :type AND user_data.external_id_content = :user AND media_data.watch_status_content = 'Finished';"
                )).params(user=user, type=type).all()

            for result in results:
                data = tmdb.get_movie_details(result.media_id_content)

                runtime += data.get("runtime")

        if type == "TV":
            pass

        return runtime