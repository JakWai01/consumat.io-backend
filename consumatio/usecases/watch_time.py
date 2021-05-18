from consumatio.external.models import *
from sqlalchemy import text
from consumatio.external.exceptions.invalid_parameter import *


class WatchTime:
    def get_watch_time(self: object, tmdb: object, user: str,
                       type: str) -> int:
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
            results = MediaData.query.from_statement(
                text(
                    "SELECT * FROM media_data, user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'Episode' AND user_data.external_id_content = :user AND media_data.watch_status_content = 'Finished';"
                )).params(user=user, type=type).all()

            for result in results:
                data = tmdb.get_tv_details(result.media_id_content)

                runtime += data.get("runtime")
        else:
            raise InvalidParameter(
                "The watchStatus: {} is invalid -> valide arguments:{} ".
                format(type, ["Movie", "TV"]))

        return runtime