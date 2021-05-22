from consumatio.entities.movie import Movie
from consumatio.entities.tv import TV
from consumatio.external.models import *
from sqlalchemy import text


def search_result_to_dict(data: dict, user: str) -> dict:
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
            if result.get("media_type") == "tv":

                query = MediaData.query.from_statement(
                    text(
                        "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'TV' AND user_data.external_id_content = :user_value AND media_data.media_id_content=:code_data;"
                    )).params(user_value=user,
                              code_data=result.get("id")).first()

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
                    "favorite": None,
                    "runtime": None
                }

                tv = TV.from_dict(dict)

                dict = tv.to_dict()

                dict["__typename"] = "TV"
            elif result.get("media_type") == "movie":
                query = MediaData.query.from_statement(
                    text(
                        "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'Movie' AND user_data.external_id_content = :user_value AND media_data.media_id_content=:code_data;"
                    )).params(user_value=user,
                              code_data=result.get("id")).first()

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
            else:
                continue
            result_list.append(dict)
        return result_dict
