from consumatio.external.exceptions.invalid_parameter import InvalidParameter
from consumatio.external.models import *


def get_watch_count(tmdb: object, external_id: str, type: str) -> int:
    """
    Get count of watched media of a certain type (e.g. "Movie", "Season" or "Drama")
    :param tmdb: <object> TMDB object to make API requests
    :param user: <str> External id of the user
    :param type: <str> Type of the media to get count for (e.g. "Movie", "Season" or "Drama")
    :return: <int> Count of media watched
    """
    count = 0
    # Same problem right here
    if type in "MovieTV":
        results = MediaData.query.join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            MediaData.media_type_content == type,
            User.external_id_content == external_id,
            MediaData.watch_status_content == 'Finished').all()

        count = len(results)
    elif type in "SeasonEpisode":
        raise InvalidParameter("Can't query watchCount for", type)
    else:
        results = MediaData.query.join(User).filter(
            User.user_id_content == MediaData.user_id_content_media_data,
            User.external_id_content == external_id,
            MediaData.watch_status_content == 'Finished').all()

        for result in results:
            if result.media_type_content == "Movie":
                data = tmdb.get_movie_details(result.media_id_content)

            if result.media_type_content == "TV":
                data = tmdb.get_tv_details(result.media_id_content)

            for genre in data.get("genres"):
                if genre.get("name") == type:
                    count += 1

    return count
