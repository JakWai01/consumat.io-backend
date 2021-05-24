from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.external.models import *
from sqlalchemy import text


def get_list(tmdb: object, external_id: str, type: str,
             watchStatus: str) -> list:
    """
    :param tmdb: <object> TMDB object to make api requests
    :param external_id: <str> External ID provided by OAuth
    :param type: <str> type of media
    :param watchStatus: <str> watchStatus to get list for
    :return: <list> Requested list
    """
    watch_list = []

    results = MediaData.query.from_statement(
        text(
            "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.watch_status_content = :watch_status AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
        )).params(watch_status=watchStatus, type=type, user=external_id).all()

    for result in results:
        if type == "Movie":
            dict = get_movie_details(external_id, tmdb,
                                     result.media_id_content, "DE")
            dict["__typename"] = "Movie"
            watch_list.append(dict)
        elif type == "TV":
            dict = get_tv_details(external_id, tmdb, result.media_id_content,
                                  "DE")
            dict["__typename"] = "TV"
            watch_list.append(dict)

    return watch_list