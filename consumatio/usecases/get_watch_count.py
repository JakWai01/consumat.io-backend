from consumatio.exceptions.invalid_parameter import InvalidParameter
from consumatio.external.db.models import *


def get_watch_count(tmdb: object, external_id: str, type: str,
                    db: object) -> int:
    """
    Get count of watched media of a certain type or genre (e.g. "Movie", "Season" or "Drama")
    :param tmdb: <object> TMDB object to make API requests
    :param external_id: <str> External id of the user
    :param type: <str> Type of the media to get count for, including genres (e.g. "Movie", "Season" or "Drama")
    :return: <int> Count of media watched
    """
    count = 0
    if type in "MovieTV":
        # results = MediaData.query.join(User).filter(
        #     User.user_id_content == MediaData.user_id_content_media_data,
        #     MediaData.media_type_content == type,
        #     User.external_id_content == external_id,
        #     MediaData.watch_status_content == 'Finished').all()
        results = db.session.query(MediaData).join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.media_type_content == type,
            User.external_id_content == external_id,
            MediaData.watch_status_content == 'Finished').all()

        count = len(results)
    elif type in "SeasonEpisode":
        raise InvalidParameter("Can't query watchCount for", type)
    else:
        # results = MediaData.query.join(User).filter(
        #     User.user_id_content == MediaData.user_id_content_media_data,
        #     User.external_id_content == external_id,
        #     MediaData.watch_status_content == 'Finished').all()
        results = db.session.query(MediaData).join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            User.external_id_content == external_id,
            MediaData.watch_status_content == 'Finished').all()

        for result in results:
            if result.media_type_content == "Movie":
                data = tmdb.get_movie_details(external_id,
                                              result.media_id_content)

            if result.media_type_content == "TV":
                data = tmdb.get_tv_details(external_id,
                                           result.media_id_content)

            for genre in data.get("genres"):
                if genre.get("name") == type:
                    count += 1

    return count
