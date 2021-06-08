import datetime
from consumatio.external.db.models import *
from consumatio.external.logger import get_logger_instance
from consumatio.exceptions.invalid_parameter import InvalidParameter

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
            logger.info("Query doesn't exist in database")

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

    def user(self: object, external_id: str) -> None:
        """
        Add a new user to the database.
        :param external_id: <str> External id provided by OAuth
        :return: None
        """
        user = User(external_id)
        self.db.session.add(user)
        self.db.session.commit()

    def user_exists(self: object, external_id: str) -> bool:
        """
        Check if a user exists
        :param external_id: <str> External id provided by OAuth
        :return: <bool> True if user exists, False if not
        """
        user = User.query.filter_by(external_id_content=external_id).first()
        if user is None:
            logger.info("User doesn't exist in database")
            return False
        else:
            logger.info("User exists in database")
            return True

    def get_user_id(self: object, external_id: str) -> int:
        """
        Get the internal user id to the corresponding external id
        :param external_id: <str> External id provided by OAuth
        :return: <int> Internal user id of a user
        """
        logger.info("user_id was loaded from database")
        user = User.query.filter_by(external_id_content=external_id).first()
        return user.user_id_content

    def user_country(self: object, external_id: str, country: str) -> None:
        """
        modify users preffered country.
        :param external_id: <str> External id provided by OAuth
        :param country: <str> ISO 3166-1 alpha-2 country code (e.g. 'DE' or 'US')
        :return: None
        """
        user = User.query.filter_by(user_id_content=external_id).first()
        user.country = country
        self.db.session.commit()
        logger.info(f"user country changed to: {country}")

    def user_language(self: object, external_id: str, language: str) -> None:
        """
        modify users preffered language.
        :param external_id: <str> External id provided by OAuth
        :param language: <str> RFC 5646 BCP language tag (e.g. 'de-DE' or 'en-US')
        :return: None
        """
        user = User.query.filter_by(user_id_content=external_id).first()
        user.language = language
        self.db.session.commit()
        logger.info(f"user language changed to: {language}")

    def media_data_exists(self: object, user_id: int, media: str,
                          media_id: int) -> bool:
        """
        Check if media data exists.
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media to check for existence ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to check
        :return: <bool> True if media data exists, False if not
        """
        self.check_all_media_types(media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        if media_data is None:
            logger.info("media_data entry doesn't exist in database")
            return False
        else:
            logger.info("media_data entry exists in database")
            return True

    def media_Data(self: object, user_id: int, media: str, media_id: int,
                   tv_code: int) -> None:
        """
        Add media data to database
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media to check for existence ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to set
        :return: None
        """
        self.check_all_media_types(media)
        media_data = MediaData(None, None, media_id, media, user_id, None,
                               tv_code)
        self.db.session.add(media_data)
        self.db.session.commit()

    def get_media_data_id(self: object, user_id: int, media: str,
                          media_id: int) -> int:
        """
        Get id of media data
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media to check for existence ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to get
        :return: <int> Internal id of the media
        """
        self.check_all_media_types(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        return media_data.user_data_id

    def rating_exists(self: object, user_id: int, media: str,
                      media_id: int) -> bool:
        """
        Check if rating exists for a certain media
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media to check for existence of a rating ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to check existence of a rating for
        :return: <bool> True if rating exists, False if not
        """
        self.check_all_media_types(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        rating = media_data.rating
        if rating is None:
            logger.info("rating doesn't exist in database")
            return False
        else:
            logger.info("rating exists in database")
            return True

    def rating(self: object, user_id: int, media: str, media_id: int,
               rating: float) -> None:
        """
        Add rating for a certain media to the database
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media to set rating for ("Movie", "TV")
        :param media_id: <int> Id of the media to set rating for
        :param rating: <float> Rating to add to the database
        :return: None
        """
        self.check_all_media_types(media)
        self.check_rating_value(rating, media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        media_data.rating_content = rating
        self.db.session.commit()
        logger.info("rating successfully entered into the database")

    def number_of_watched_episodes(self: object, user_id: int, media_id: int,
                                   number_of_watched_episodes: int) -> None:
        """
        Get the number of watched episodes
        :param user_id: <int> User id of a user
        :param media_id: <int> Id of the media
        :param number_of_watched_episodes: <int> Get number of watched episodes
        :return: None
        """
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content="Season",
            media_id_content=media_id).first()
        media_data.number_of_watched_episodes = number_of_watched_episodes
        self.db.session.commit()
        logger.info(
            "number of watched episodes successfully entered into the database"
        )

    def watch_status_exists(self: object, user_id: int, media: str,
                            media_id: int) -> bool:
        """
        Check if watch status exists for a certain media
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to check watch status for
        :return: <bool> True of watch status exists, False if not
        """
        self.check_root_media_type(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        watch_status = media_data.watch_status_content
        if watch_status is None:
            logger.info("watch_status doesnt exist in database")
            return False
        else:
            logger.info("watch_status exists in database")
            return True

    def watch_status(self: object, user_id: int, media: str, media_id: int,
                     watch_status: str) -> None:
        """
        Add watch status for a certain media to the database
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media to set watch_status for
        :param media_id: <int> Id of the media to check watch status for
        :param watch_status: <str> Watch status to add to the database
        :return: None
        """
        self.check_watch_status(watch_status)
        self.check_root_media_type(media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        media_data.watch_status_content = watch_status
        self.db.session.commit()
        logger.info("watchStatus succesful entered in database")

    def favorite_exists(self: object, user_id: int, media: str,
                        media_id: int) -> bool:
        """
        Check if favorite is specified for a certain media
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to check watch status for
        :return: True if favorite exists, False if not
        """
        self.check_all_media_types(media)
        media_data = MediaData.query.filter_by(
            user_id_content=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        favorite = media_data.favorite
        if favorite is None:
            logger.info("favorite doesnt exist in database")
            return False
        else:
            logger.info("favorite exists in database")
            return True

    def favorite(self: object, user_id: int, media: str, media_id: int,
                 favorite: bool) -> None:
        """
        Add favorite for a certain media into the database
        :param user_id: <int> User id of a user
        :param media: <str> Type of the media ("Movie", "TV", "Season", "Episode")
        :param media_id: <int> Id of the media to check watch status for
        :param favorite: <bool> True if media is favorite, False if not
        :return: None
        """
        self.check_all_media_types(media)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=media,
            media_id_content=media_id).first()
        media_data.favorite_content = favorite
        self.db.session.commit()
        logger.info("favorite succesful entered in database")

    def check_watch_status(self: object, watch_status: str) -> None:
        """
        Check if the watch status has valid values
        :param watch_status: <str> Watch status of a certain media
        :return: None
        """
        valid_watch_status = [
            "Planning", "Watching", "Dropped", "Finished", None
        ]
        if watch_status not in valid_watch_status:
            raise InvalidParameter(
                "The watchStatus: {} is invalid -> valide arguments:{} ".
                format(watch_status, valid_watch_status))

    def check_all_media_types(self: object, media: str) -> None:
        """
        Check if media has valid values
        :media: <str> Media type of a certain media
        :return: None
        """
        valid_media = ["TV", "Movie", "Episode", "Season"]
        if media not in valid_media:
            raise InvalidParameter(
                "The media: {} is invalid -> valide arguments:{} ".format(
                    media, valid_media))

    def check_root_media_type(self: object, media: str) -> None:
        """
        Check if media has valid values concerning the watch status and rating mutation
        :param media: <str> Media type of a certain media
        :return: None
        """
        valid_media = ["TV", "Movie"]
        if media not in valid_media:
            raise InvalidParameter(
                "The media: {} is invalid -> valide arguments:{} ".format(
                    media, valid_media))

    def check_rating_value(self: object, rating: int, media: str) -> None:
        """
        Check if rating has valid value concerning the watch rating mutation
        :param media: <int> Rating value
        :return: None
        """
        lower_bound = 0
        upper_bound = 10
        valid_media = ["TV", "Movie"]

        if rating is not None and (rating < lower_bound or rating > upper_bound
                                   ) or media not in valid_media:
            raise InvalidParameter(
                "Please make sure the rating your rating is in range: {}-{} and you only rate {}"
                .format(lower_bound, upper_bound, valid_media))
