from consumatio.entities.movie import Movie
from consumatio.external.db.models import *
from sqlalchemy import text


def popular_movies_to_dict(data: dict, external_id: str) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    result_list = []
    result_dict = {"results": result_list, "total_pages": data["total_pages"]}
    if "results" not in data:
        return result_dict
    elif len(data["results"]) == 0:
        return result_dict
    else:
        results = data["results"]
        for result in results:

            query = MediaData.query.join(User).filter(
                User.user_id_content == MediaData.user_id_content_media_data,
                MediaData.media_type_content == "Movie",
                User.external_id_content == external_id,
                MediaData.media_id_content == result.get("id")).first()

            rating = None
            watch_status = None
            if query != None:
                rating = query.rating_content
                watch_status = query.watch_status_content
            dict = {
                "code": result.get("id"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("vote_average"),
                "rating_count": result.get("vote_count"),
                "release_date": result.get("release_date"),
                "runtime": None,
                "status": None,
                "backdrop_path": result.get("backdrop_path"),
                "poster_path": result.get("poster_path"),
                "providers": None,
                "cast": None,
                "directors": None,
                "tmdb_url":
                f'https://www.themoviedb.org/movie/{result.get("id")}',
                "watch_status": watch_status,
                "rating_user": rating,
                "favorite": None
            }

            movie = Movie.from_dict(dict)

            dict = movie.to_dict()

            dict["__typename"] = "Movie"

            result_list.append(dict)
        return result_dict
