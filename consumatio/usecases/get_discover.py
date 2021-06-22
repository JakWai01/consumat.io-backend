from consumatio.usecases.get_popular import get_popular
from consumatio.external.db.models import MediaData, User
import datetime


def get_discover(external_id: str, tmdb: object, type: str, person: int,
                 similar_to: int, page: int, db: object) -> dict:
    """
    Get list of recommended media based on user ratings/favorites (popular as fallback)
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object 
    :param type: <str> Type of the media to query
    :param person: <int> TMDB code of a person to get media w/ them (e.g. actor or director)
    :param similar_to: <int> TMDB code of a movie/tv show to get similar media
    :param page: <int> Search page (minimum:1 maximum:1000)
    :param db: <object> Database object
    :return: <dict> Result dictionary 
    """
    results = []
    total_pages = 0

    media = db.session.query(MediaData).join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == type, User.external_id_content ==
        external_id).filter((MediaData.rating_content != None)
                            | (MediaData.favorite_content == True)).order_by(
                                MediaData.created_on.desc()).all()

    watched = db.session.query(MediaData).join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.watch_status_content == "Finished",
        MediaData.media_type_content == type,
        User.external_id_content == external_id).all()

    if person is None and similar_to is None:
        if len(media) > 0:
            # request only for the first 8 items
            results.extend(get_recommended(media[:8], external_id, tmdb, type))

    elif person is None and similar_to is not None:
        return get_similar(similar_to, external_id, tmdb, type, page)

    elif type == "Movie" and person is not None and similar_to is None:
        return tmdb.get_movies_with(external_id, person, page)

    if len(results) == 0:
        return get_popular(external_id, tmdb, type, page, db)

    else:
        for result in results:
            # remove already watched items from results
            if result.get("code") in [i.media_id_content for i in watched]:
                results.remove(result)

        results = list(divide_chunks(results, 20))
        total_pages = len(results)

        return {"total_pages": total_pages, "results": results[page - 1]}


def get_recommended(list: list, external_id: str, tmdb: object,
                    type: str) -> list:
    """
    Handle the 'logic' to find recommended media based on user ratings
    :param list: <list> List of codes to query TMDB API with
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object 
    :param type: <str> Type of the media to query
    :return: <list> List of TV/Movie recommendations
    """
    results = []

    # list comprising only of user ratings to calculate average
    user_ratings = [
        i.rating_content for i in list if i.rating_content is not None
    ]

    rating_avg = sum(user_ratings) / len(user_ratings)

    # set every rating thats null to 0 or 10 if favorite
    for media in list:
        if media.rating_content is None or media.favorite_content:
            media.rating_content = 10 if media.favorite_content else 0

    for media in list:
        code = media.media_id_content
        rating = media.rating_content

        if time_delta(media.created_on).days <= 14 and rating >= rating_avg:
            similar = get_similar(code, external_id, tmdb, type)
            results.extend(similar.get("results"))

    return results


def get_similar(code: int,
                external_id: str,
                tmdb: object,
                type: str,
                page=1) -> dict:
    """
    Get similar media like the one provided
    :param code: <int> Id of TV or Movie
    :param external_id: <str> External ID of the user provided by OAuth
    :param tmdb: <object> Tmdb object
    :param type: <str> Type of the Media ("Movie" or "TV")
    :param page: <int> How many pages should be displayed
    :return: <dict> Recommended Media
    """
    similar_media = {}

    if type == "Movie":
        similar_media = tmdb.get_recommended_movies(external_id, code, page)
    elif type == "TV":
        similar_media = tmdb.get_recommended_tv(external_id, code, page)

    return similar_media


def divide_chunks(list: list, n: int):
    """
    Divide list in equally sized parts
    :param list: <list> Any list
    :param n: <int> Size of the chunks
    """
    for i in range(0, len(list), n):
        yield list[i:i + n]


def time_delta(date_added: datetime.datetime) -> datetime.timedelta:
    """
    Calculate the time difference for any given time and now
    :param date_added: <datetime> Datetime object
    :param n: <int> Size of the chunks
    :return: <timedelta> Timedelta object
    """
    today = datetime.datetime.now().date()
    delta = today - date_added.date()

    return delta
