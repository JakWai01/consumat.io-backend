from consumatio.usecases.get_movie import *
from consumatio.usecases.get_tv import *
from consumatio.external.models import *
from sqlalchemy import text


def get_list(tmdb: object, external_id: str, type: str, watchStatus: str,
             favorite: bool):
    watch_list = []
    results = []

    if watchStatus == None and favorite != None:
        results = MediaData.query.join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.favorite_content == favorite,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    elif watchStatus == None and favorite == None:
        results = MediaData.query.join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    elif watchStatus != None and favorite != None:
        results = MediaData.query.join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.watch_status_content == watchStatus,
            MediaData.favorite_content == favorite,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    else:
        results = MediaData.query.join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.watch_status_content == watchStatus,
            MediaData.media_type_content == type,
            User.external_id_content == external_id).all()
    for result in results:
        if type == "Movie":
            dict = get_movie(external_id, tmdb, result.media_id_content, "DE")
            dict["__typename"] = "Movie"
            watch_list.append(dict)
        elif type == "TV":
            dict = get_tv(external_id, tmdb, result.media_id_content, "DE")
            dict["__typename"] = "TV"
            watch_list.append(dict)

    return watch_list
