from consumatio.external.db.models import MediaData, User
from consumatio.entities.tv import TV
from consumatio.entities.movie import Movie


def get_search(external_id: str, tmdb: object, keyword: str, page: int,
               db: object) -> dict:
    """
    Assemble search results
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param keyword: <str> Search string
    :param page: <int> Search page (minimum:1 maximum:1000)
    :param db: <object> Database object
    :return: <dict> Search details
    """
    dict_search_details = tmdb.get_search_result(external_id, keyword, page)

    results = dict_search_details["results"]
    result_list = []
    for result in results:
        if "first_air_date" in result:
            # TV
            dict = {}

            query = db.session.query(MediaData).join(User).filter(
                User.user_id_content == MediaData.user_id_content_media_data,
                MediaData.media_type_content == 'TV',
                User.external_id_content == external_id,
                MediaData.media_id_content == result.get("code")).first()

            rating = None
            watch_status = None
            favorite = False
            if query != None:
                rating = query.rating_content
                watch_status = query.watch_status_content
                favorite = query.favorite_content

            dict = {
                "code": result.get("code"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("rating_average"),
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
                f'https://www.themoviedb.org/tv/{result.get("code")}',
                "watch_status": watch_status,
                "rating_user": rating,
                "favorite": favorite,
                "runtime": None,
                "rating_count": result.get("rating_count")
            }

            tv = TV.from_dict(dict)
            dict = tv.to_dict()

            dict["__typename"] = "TV"
        else:
            # Movie
            dict = {}

            query = db.session.query(MediaData).join(User).filter(
                User.user_id_content == MediaData.user_id_content_media_data,
                MediaData.media_type_content == 'Movie',
                User.external_id_content == external_id,
                MediaData.media_id_content == result.get("code")).first()

            rating = None
            watch_status = None
            favorite = False
            if query != None:
                rating = query.rating_content
                watch_status = query.watch_status_content
                favorite = query.favorite_content

            dict = {
                "code": result.get("code"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("rating_average"),
                "release_date": result.get("release_date"),
                "runtime": None,
                "status": None,
                "backdrop_path": result.get("backdrop_path"),
                "poster_path": result.get("poster_path"),
                "providers": None,
                "cast": None,
                "directors": None,
                "tmdb_url":
                f'https://www.themoviedb.org/movie/{result.get("code")}',
                "watch_status": watch_status,
                "rating_user": rating,
                "favorite": favorite,
                "rating_count": result.get("rating_count")
            }

            movie = Movie.from_dict(dict)

            dict = movie.to_dict()

            dict["__typename"] = "Movie"

        result_list.append(dict)

    dict = {
        "total_pages": dict_search_details["total_pages"],
        "results": result_list
    }

    return dict
