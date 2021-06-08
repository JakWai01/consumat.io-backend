from consumatio.entities.tv import TV
from consumatio.external.db.models import *


def get_tv(external_id: str, tmdb: object, code: int) -> dict:
    """
    Make all relevant API requests for this usecase (details, images, providers, credits) and assemble a TV 
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param code: <int> Id of the tv show to get data for
    :return: <dict> TV details
    """
    dict_tv_details = tmdb.get_tv_details(external_id, code)
    dict_tv_providers = tmdb.get_tv_providers(external_id, code)
    dict_tv_credits = tmdb.get_tv_credits(code)

    result = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == 'TV',
        User.external_id_content == external_id,
        MediaData.media_id_content == code).first()

    rating = None
    watch_status = None
    favorite = None
    if result != None:
        rating = result.rating_content
        watch_status = result.watch_status_content
        favorite = result.favorite_content

    dict = {
        "code": dict_tv_details.get("code"),
        "title": dict_tv_details.get("title"),
        "genres": dict_tv_details.get("genres"),
        "overview": dict_tv_details.get("overview"),
        "popularity": dict_tv_details.get("popularity"),
        "rating_average": dict_tv_details.get("rating_average"),
        "rating_count": dict_tv_details.get("rating_count"),
        "first_air_date": dict_tv_details.get("first_air_date"),
        "last_air_date": dict_tv_details.get("last_air_date"),
        "status": dict_tv_details.get("status"),
        "backdrop_path": dict_tv_details.get("backdrop_path"),
        "poster_path": dict_tv_details.get("poster_path"),
        "providers": dict_tv_providers.get("providers"),
        "cast": dict_tv_credits.get("cast"),
        "creators": dict_tv_details.get("creators"),
        "number_of_episodes": dict_tv_details.get("number_of_episodes"),
        "number_of_seasons": dict_tv_details.get("number_of_seasons"),
        "tmdb_url":
        f'https://www.themoviedb.org/tv/{dict_tv_details.get("code")}',
        "watch_status": watch_status,
        "rating_user": rating,
        "favorite": favorite,
        "runtime": dict_tv_details.get("runtime"),
        "rating_count": dict_tv_details.get("vote_count")
    }

    tv = TV.from_dict(dict)

    return tv.to_dict()
