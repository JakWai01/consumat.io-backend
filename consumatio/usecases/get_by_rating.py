from consumatio.constants import TMDB_FRONTEND_PREFIX
from consumatio.external.db.models import MediaData, User
from consumatio.entities.movie import Movie
from consumatio.entities.tv import TV
from consumatio.external.db.models import *


def get_by_rating(external_id: str, tmdb: object, type: str, vote_avg: float,
                  vote_count: int, released_from: str, page: int,
                  db: object) -> dict:
    """
    Make all relevant API request for this usecase (items by rating) and assemble them into a dictionary
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param type: <str> Popular item type "movie" or "tv"
    :param vote_avg: <float> filter media with average rating greater than set value
    :param vote_count: <int> minimum number of votes
    :param released_from: <str> search for media released after specified date (YYYY-MM-DD)
    :param page: <int> Search page (minimum:1 maximum:1000)
    :param db: <object> Database object
    :return: <dict> popular media
    """
    dict = {}
    if type == "Movie":
        dict_movie_results = tmdb.get_movies_by_rating(external_id, vote_avg,
                                                       vote_count,
                                                       released_from, page)

        results = dict_movie_results.get("results")
        result_list = []

        for result in results:
            query = db.session.query(MediaData).join(User).filter(
                User.user_id_content == MediaData.user_id_content_media_data,
                MediaData.media_type_content == "Movie",
                User.external_id_content == external_id,
                MediaData.media_id_content == result["code"]).first()

            rating = None
            watch_status = None
            favorite = False

            if query != None:
                rating = query.rating_content
                watch_status = query.watch_status_content
                favorite = query.favorite_content

            result["rating"] = rating
            result["watch_status"] = watch_status
            result["favorite"] = favorite

            dict = {
                "code": result.get("code"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("rating_average"),
                "rating_count": result.get("rating_count"),
                "release_date": result.get("release_date"),
                "runtime": None,
                "status": None,
                "backdrop_path": result.get("backdrop_path"),
                "poster_path": result.get("poster_path"),
                "providers": None,
                "cast": None,
                "directors": None,
                "tmdb_url":
                f'{TMDB_FRONTEND_PREFIX}/movie/{result.get("code")}',
                "watch_status": watch_status,
                "rating_user": rating,
                "favorite": favorite
            }

            movie = Movie.from_dict(dict)
            dict = movie.to_dict()

            dict["__typename"] = "Movie"

            result_list.append(dict)

        dict = {
            "total_pages": dict_movie_results.get("total_pages"),
            "results": result_list
        }

    elif type == "TV":
        dict_tv_results = tmdb.get_tv_by_rating(external_id, vote_avg,
                                                vote_count, released_from,
                                                page)

        results = dict_tv_results.get("results")
        result_list = []

        for result in results:
            query = db.session.query(MediaData).join(User).filter(
                User.user_id_content == MediaData.user_id_content_media_data,
                MediaData.media_type_content == "TV",
                User.external_id_content == external_id,
                MediaData.media_id_content == result["code"]).first()

            rating = None
            watch_status = None
            favorite = False

            if query != None:
                rating = query.rating_content
                watch_status = query.watch_status_content
                favorite = query.favorite_content

            result["rating"] = rating
            result["watch_status"] = watch_status
            result["favorite"] = favorite

            dict = {
                "code": result.get("code"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("rating_average"),
                "rating_count": result.get("rating_count"),
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
                "tmdb_url": f'{TMDB_FRONTEND_PREFIX}/tv/{result.get("code")}',
                "watch_status": watch_status,
                "rating_user": rating,
                "favorite": favorite,
                "runtime": None
            }

            tv = TV.from_dict(dict)
            dict = tv.to_dict()

            dict["__typename"] = "TV"

            result_list.append(dict)

        dict = {
            "total_pages": dict_tv_results.get("total_pages"),
            "results": result_list
        }

    return dict
