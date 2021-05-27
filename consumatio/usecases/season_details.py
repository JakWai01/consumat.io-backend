from consumatio.entities.season import Season
from consumatio.external.models import *
from sqlalchemy import text


def get_season_details(external_id: str, tmdb: object, code: int,
                       season_number: int) -> dict:
    """
    Make all relevant API requests for this usecase (details, images) and assemble them into a dictionary
    :param tmdb: <object> Tmdb object
    :param code: <int> Id of the tv_show to get season details for
    :param season_number: <int> Number of season to get details for
    :return: <dict> Season details
    """
    dict_season_details = tmdb.get_season_details(code, season_number)

    result = MediaData.query.from_statement(
        text(
            "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'Season' AND user_data.external_id_content = :user_value AND media_data.media_id_content=:code_data;"
        )).params(user_value=external_id,
                  code_data=dict_season_details.get("code")).first()

    favorite = None
    number_of_watched_episodes = None
    if result != None:
        number_of_watched_episodes = result.number_of_watched_episodes
        favorite = result.favorite_content

    dict = {
        "code": dict_season_details.get("code"),
        "tv_code": code,
        "season_number": dict_season_details.get("season_number"),
        "title": dict_season_details.get("title"),
        "overview": dict_season_details.get("overview"),
        "poster_path": dict_season_details.get("poster_path"),
        "favorite": favorite,
        "number_of_episodes": dict_season_details.get("number_of_episodes"),
        "air_date": dict_season_details.get("air_date"),
        "number_of_watched_episodes": number_of_watched_episodes
    }

    season = Season.from_dict(dict)

    return season.to_dict()
