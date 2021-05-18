import datetime
from consumatio.external.models import *
from consumatio.external.logger import get_logger_instance
from consumatio.external.exceptions.invalid_parameter import InvalidParameter

logger = get_logger_instance()


class Database():
    def __init__(self, db):
        self.db = db

    def cache(self: object, query: str, body: str) -> None:
        """
        Cache the provided query and the respective result in the database.
        :param query: <str> Tmdb query string
        :param body: <str> Response of the query 
        """
        cache = Cache(query, body)
        self.db.session.add(cache)
        self.db.session.commit()

        logger.info("Query was saved in database")

    def is_cached(self: object, query: str) -> bool:
        """
        Checks if a query is cached in the database.
        :param query: <str> Tmdb query string
        :return: <bool> Returns true if the query is cached, else false 
        """
        cached = Cache.query.filter_by(query_content=query).first()

        if cached == None:
            logger.info("Query doesnt exist in database")

            return False
        elif (cached.last_changed - datetime.datetime.now()).days >= 10:
            logger.info("Query is stale")

            self.db.session.delete(cached)
            return False
        else:
            logger.info("Query exists in database")
            return True

    def get_from_cache(self: object, query: str) -> str:
        """
        Get body of a query out of the database if the query was cached.
        :param query: <str> tmdb query string
        :return: <str> body of query
        """
        logger.info("Query was loaded from database")

        return Cache.query.filter_by(query_content=query).first().body_content

# --------------------------------------------------------------------

    def user(self: object, external_id: str) -> None:
        user = User(external_id)
        self.db.session.add(user)
        self.db.session.commit()

    def user_exists(self: object, external_id: str) -> bool:
        user = User.query.filter_by(external_id_content=external_id).first()
        if user is None:
            logger.info("User doesnt exist in database")
            return False
        else:
            logger.info("User exists in database")
            return True

    def get_user_id(self: object, external_id: str) -> int:
        logger.info("user_id was loaded from database")
        user = User.query.filter_by(external_id_content=external_id).first()
        return user.user_id_content

# --------------------------------------------------------------------

    def media_data_exists(self: object, user_id: int, media: str,
                          media_id: int) -> bool:
        self.check_media(media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        if media_data is None:
            logger.info("media_data entry doesnt exist in database")
            return False
        else:
            logger.info("media_data entry exists in database")
            return True

    def media_Data(self: object, user_id: int, media: str,
                   media_id: int) -> None:
        self.check_media(media)
        media_data = MediaData(None, None, media_id, media, user_id)
        self.db.session.add(media_data)
        self.db.session.commit()

    def get_media_data_id(self: object, user_id: int, media: str,
                          media_id: int) -> int:
        self.check_media(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        return media_data.user_data_id

# --------------------------------------------------------------------

    def rating_exists(self: object, user_id: int, media: str,
                      media_id: int) -> bool:
        self.check_media(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        rating = media_data.rating
        if rating is None:
            logger.info("rating doesnt exist in database")
            return False
        else:
            logger.info("rating exists in database")
            return True

    def rating(self: object, user_id: int, media: str, media_id: int,
               rating: float) -> None:
        self.check_media(media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        media_data.rating_content = rating
        self.db.session.commit()
        logger.info("rating succesful entered in database")

# --------------------------------------------------------------------

    def watch_status_exists(self: object, user_id: int, media: str,
                            media_id: int) -> bool:
        self.check_media(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        watch_status = media_data.watch_status
        if watch_status is None:
            logger.info("watch_status doesnt exist in database")
            return False
        else:
            logger.info("watch_status exists in database")
            return True

    def watch_status(self: object, user_id: int, media: str, media_id: int,
                     watch_status: str) -> None:
        self.check_watch_status(watch_status)
        self.check_media(media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        media_data.watch_status_content = watch_status
        self.db.session.commit()
        logger.info("watchStatus succesful entered in database")


# --------------------------------------------------------------------

    def check_watch_status(self: object, watch_status: str) -> None:
        valid_watch_status = [
            "Planning", "Watching", "Dropped", "Finished", None
        ]
        if watch_status not in valid_watch_status:
            raise InvalidParameter(
                "The watchStatus: {} is invalid -> valide arguments:{} ".
                format(watch_status, valid_watch_status))

    def check_media(self: object, media: str) -> None:
        valid_media = ["TV", "Movie", "Episode", "Season"]
        if media not in valid_media:
            raise InvalidParameter(
                "The media: {} is invalid -> valide arguments:{} ".format(
                    media, valid_media))
