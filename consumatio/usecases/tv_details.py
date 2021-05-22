from consumatio.entities.tv import TV
from consumatio.external.models import *
from sqlalchemy import text


class TVDetails:
    def get_tv_details(self: object, user: str, tmdb: object, code: int,
                       country: str) -> dict:
        """
        Make all relevant API requests for this usecase (details, images, providers, credits) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param code: <int> Id of the tv show to get data for
        :param country: <str> Country abbreveation of the country to get providers for (e.g. "DE" -> Germany)
        :return: <dict> TV details
        """
        dict_tv_details = tmdb.get_tv_details(code)
        dict_tv_providers = tmdb.get_tv_providers(code, country)
        dict_tv_credits = tmdb.get_tv_credits(code)

        result = MediaData.query.from_statement(
            text(
                "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = 'TV' AND user_data.external_id_content = :user_value AND media_data.media_id_content=:code_data;"
            )).params(user_value=user, code_data=code).first()

        rating = None
        watch_status = None
        favorite = None
        if result != None:
            rating = result.rating_content
            watch_status = result.watch_status_content
            favorite = result.favorite_content

        dict = {
            "code": dict_tv_details.get("code"),
            "title": dict_tv_details.get("title"),
            "genres": dict_tv_details.get("genres"),
            "overview": dict_tv_details.get("overview"),
            "popularity": dict_tv_details.get("popularity"),
            "rating_average": dict_tv_details.get("rating_average"),
            "first_air_date": dict_tv_details.get("first_air_date"),
            "last_air_date": dict_tv_details.get("last_air_date"),
            "status": dict_tv_details.get("status"),
            "backdrop_path": dict_tv_details.get("backdrop_path"),
            "poster_path": dict_tv_details.get("poster_path"),
            "providers": dict_tv_providers.get("providers"),
            "cast": dict_tv_credits.get("cast"),
            "creators": dict_tv_details.get("creators"),
            "number_of_episodes": dict_tv_details.get("number_of_episodes"),
            "number_of_seasons": dict_tv_details.get("number_of_seasons"),
            "tmdb_url":
            f'https://www.themoviedb.org/tv/{dict_tv_details.get("code")}',
            "watch_status": watch_status,
            "rating_user": rating,
            "favorite": favorite,
            "runtime": dict_tv_details.get("runtime")
        }

        tv = TV.from_dict(dict)

        return tv.to_dict()
