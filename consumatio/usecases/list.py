from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.external.models import *
from sqlalchemy import text


def get_list(tmdb: object, external_id: str, type: str, watchStatus: str,
             favorite: bool):
    watch_list = []

    query = "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data"
    results = []

    if watchStatus == "any" and favorite:
        query += " AND media_data.favorite_content = :favorite AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
        results = MediaData.query.from_statement(text(query)).params(
            favorite=favorite, type=type, user=external_id).all()
    elif watchStatus == "any":
        query += " AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
        results = MediaData.query.from_statement(text(query)).params(
            type=type, user=external_id).all()
    elif favorite:
        query += " AND media_data.watch_status_content = :watch_status AND media_data.favorite_content = :favorite AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
        results = MediaData.query.from_statement(text(query)).params(
            watch_status=watchStatus,
            favorite=favorite,
            type=type,
            user=external_id).all()
    else:
        query += " AND media_data.watch_status_content = :watch_status AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
        results = MediaData.query.from_statement(text(query)).params(
            watch_status=watchStatus, type=type, user=external_id).all()

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
