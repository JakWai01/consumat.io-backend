from consumatio.entities.episode import Episode
from consumatio.external.models import *
from sqlalchemy import text


def get_episode_details(external_id: str, tmdb: object, code: int,
                        season_number: int, episode_number: int) -> dict:
    """
    Make all relevant API requests for this usecase (details, images) and assemble them into a dictionary
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param code: <int> Id of the tv show to get data for
    :param season_number: <int> Number of the season which includes the episode
    :param episode_number: <int> Number of the episode in the corresponding season
    :return: <dict> Episode details
    """
    dict_episode_details = tmdb.get_episode_details(code, season_number,
                                                    episode_number)

    result = MediaData.query.from_statement(
        text(
            "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'Episode' AND user_data.external_id_content = :user_value AND media_data.media_id_content=:code_data;"
        )).params(user_value=external_id,
                  code_data=dict_episode_details.get("code")).first()

    favorite = None
    rating = None
    if result != None:
        rating = result.rating_content
        favorite = result.favorite_content

    dict = {
        "code": dict_episode_details.get("code"),
        "title": dict_episode_details.get("title"),
        "episode_number": dict_episode_details.get("episode_number"),
        "season_number": season_number,
        "overview": dict_episode_details.get("overview"),
        "air_date": dict_episode_details.get("air_date"),
        "rating_average": dict_episode_details.get("rating_average"),
        "still_path": dict_episode_details.get("still_path"),
        "rating_user": rating,
        "favorite": favorite,
    }

    episode = Episode.from_dict(dict)

    return episode.to_dict()