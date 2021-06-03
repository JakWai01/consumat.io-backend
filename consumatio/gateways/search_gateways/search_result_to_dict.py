from consumatio.entities.movie import Movie
from consumatio.entities.tv import TV
from consumatio.external.db.models import *


def search_result_to_dict(data: dict, external_id: str) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :param external_id: <str> External representation of the user
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

                query = MediaData.query.join(User).filter(
                    User.user_id_content ==
                    MediaData.user_id_content_media_data,
                    MediaData.media_type_content == 'TV',
                    User.external_id_content == external_id,
                    MediaData.media_id_content == result.get("id")).first()

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
                    "runtime": None,
                    "rating_count": result.get("vote_count")
                }

                tv = TV.from_dict(dict)

                dict = tv.to_dict()

                dict["__typename"] = "TV"
            elif result.get("media_type") == "movie":
                query = MediaData.query.join(User).filter(
                    User.user_id_content ==
                    MediaData.user_id_content_media_data,
                    MediaData.media_type_content == 'Movie',
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
                    "favorite": None,
                    "rating_count": result.get("vote_count")
                }

                movie = Movie.from_dict(dict)

                dict = movie.to_dict()

                dict["__typename"] = "Movie"
            else:
                continue
            result_list.append(dict)
        return result_dict
