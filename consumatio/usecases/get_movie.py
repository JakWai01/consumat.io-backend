from consumatio.constants import TMDB_FRONTEND_PREFIX
from consumatio.entities.movie import Movie
from consumatio.external.db.models import MediaData, User


def get_movie(external_id: str, tmdb: object, code: int, db: object) -> dict:
    """
    Make all relevant API requests (details, providers, credits) and assemble a Movie
    :param external_id: <str> External ID provided by OAuth
    :param tmdb: <object> Tmdb object
    :param code: <int> Id of the movie to get data for
    :param db: <object> Database object
    :return: <dict> Movie details
    """
    dict_movie_details = tmdb.get_movie_details(external_id, code)
    dict_movie_providers = tmdb.get_movie_providers(external_id, code)
    dict_movie_credits = tmdb.get_movie_credits(code)

    result = db.session.query(MediaData).join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == 'Movie',
        User.external_id_content == external_id,
        MediaData.media_id_content == code).first()

    favorite = False
    rating = None
    watch_status = None
    if result != None:
        favorite = result.favorite_content
        rating = result.rating_content
        watch_status = result.watch_status_content

    dict = {
        "code": dict_movie_details.get("code"),
        "title": dict_movie_details.get("title"),
        "genres": dict_movie_details.get("genres"),
        "overview": dict_movie_details.get("overview"),
        "popularity": dict_movie_details.get("popularity"),
        "rating_average": dict_movie_details.get("rating_average"),
        "rating_count": dict_movie_details.get("rating_count"),
        "release_date": dict_movie_details.get("release_date"),
        "runtime": dict_movie_details.get("runtime"),
        "status": dict_movie_details.get("status"),
        "backdrop_path": dict_movie_details.get("backdrop_path"),
        "poster_path": dict_movie_details.get("poster_path"),
        "providers": dict_movie_providers.get("providers"),
        "cast": dict_movie_credits.get("cast"),
        "directors": dict_movie_credits.get("directors"),
        "tmdb_url":
        f'{TMDB_FRONTEND_PREFIX}/movie/{dict_movie_details.get("code")}',
        "watch_status": watch_status,
        "rating_user": rating,
        "favorite": favorite
    }

    movie = Movie.from_dict(dict)

    return movie.to_dict()
