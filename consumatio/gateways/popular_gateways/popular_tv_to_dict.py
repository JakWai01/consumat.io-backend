from consumatio.entities.tv import TV
from consumatio.external.models import *
from sqlalchemy import text


def popular_tv_to_dict(data: dict, user: str) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    if "results" not in data:
        return []
    elif len(data["results"]) == 0:
        return []
    else:
        results = data["results"]
        result_list = []

        for result in results:
            query = MediaData.query.from_statement(
                text(
                    "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'Movie' AND user_data.external_id_content = :user_value AND media_data.media_id_content=:code_data;"
                )).params(user_value=user, code_data=result.get("id")).first()

            rating = None
            watch_status = None
            if query != None:
                rating = query.rating_content
                watch_status = query.watch_status_content

            dict = {
                "code": result.get("id"),
                "title": result.get("name"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("vote_average"),
                "first_air_date": result.get("first_air_date"),
                "last_air_date": None,
                "status": None,
                "backdrop_path": result.get("backdrop_path"),
                "poster_path": result.get("poster_path"),
                "providers": None,
                "creators": None,
                "cast": None,
                "number_of_episodes": None,
                "number_of_seasons": None,
                "tmdb_url":
                f'https://www.themoviedb.org/tv/{result.get("id")}',
                "watch_status": watch_status,
                "rating_user": rating,
                "favorite": None
            }

            tv = TV.from_dict(dict)

            dict = tv.to_dict()

            dict["__typename"] = "TV"

            result_list.append(dict)
        return result_list
