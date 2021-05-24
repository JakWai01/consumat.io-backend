from consumatio.usecases.movie_details import MovieDetails
from consumatio.usecases.tv_details import TVDetails
from consumatio.external.models import *
from sqlalchemy import text


class List:
    def get_list(self: object, tmdb: object, database: object, user: str,
                 type: str, watchStatus: str, favorite: bool):
        watch_list = []
        # results = query where user == user and watch_status == watch_status and type == type
        # results = db.session.query().from_statement(
        #     text("SELECT * FROM media_data")).all()

        query = "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.watch_status_content = :watch_status AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
        results = []

        if watchStatus == "any" and favorite:
            query = "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.favorite_content = :favorite AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
            results = MediaData.query.from_statement(text(query)).params(
                favorite=favorite, type=type, user=user).all()
        elif watchStatus == "any":
            query = "SELECT * FROM media_data , user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
            results = MediaData.query.from_statement(text(query)).params(
                type=type, user=user).all()
        else:
            results = MediaData.query.from_statement(text(query)).params(
                watch_status=watchStatus, type=type, user=user).all()

        for result in results:
            if type == "Movie":
                movie_details = MovieDetails()
                dict = movie_details.get_movie_details(user, tmdb,
                                                       result.media_id_content,
                                                       "DE")
                dict["__typename"] = "Movie"
                watch_list.append(dict)
            elif type == "TV":
                tv_details = TVDetails()
                dict = tv_details.get_tv_details(user, tmdb,
                                                 result.media_id_content, "DE")
                dict["__typename"] = "TV"
                watch_list.append(dict)

        return watch_list