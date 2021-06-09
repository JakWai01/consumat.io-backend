from consumatio.entities.episode import Episode
from consumatio.external.db.models import *


def get_episode(external_id: str, tmdb: object, code: int, season_number: int,
                episode_number: int, db: object) -> dict:
    """
    Make all relevant API requests (details, images) and assemble an Episode
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param code: <int> Id of the tv show to get data for
    :param season_number: <int> Number of the season which includes the episode
    :param episode_number: <int> Number of the episode in the corresponding season
    :return: <dict> Episode details
    """
    dict_episode_details = tmdb.get_episode_details(external_id, code,
                                                    season_number,
                                                    episode_number)

    # result = MediaData.query.join(User).filter(
    #     User.user_id_content == MediaData.user_id_content_media_data,
    #     MediaData.media_type_content == 'Episode',
    #     User.external_id_content == external_id, MediaData.media_id_content ==
    #     dict_episode_details.get("code")).first()
    result = db.session.query(MediaData).join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == 'Episode',
        User.external_id_content == external_id, MediaData.media_id_content ==
        dict_episode_details.get("code")).first()

    favorite = None
    if result != None:
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
        "favorite": favorite,
    }

    episode = Episode.from_dict(dict)

    return episode.to_dict()