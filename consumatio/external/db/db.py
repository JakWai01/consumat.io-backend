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
        :param query: <str> Request to store in cache
        :param body: <str> Response of the query to store
        :return: None
        """
        cache = Cache(query, body)
        self.db.session.add(cache)
        self.db.session.commit()

        logger.info("Query was saved in the database")

    def is_cached(self: object, query: str) -> bool:
        """
        Checks if a query is cached in the database.
        :param query: <str> Tmdb query string
        :return: <bool> Returns true if the query is cached, else false 
        """
        cached = Cache.query.filter_by(query_content=query).first()

        if cached == None:
            logger.info("Query doesn't exist in the database")

            return False
        elif cached.last_changed < datetime.datetime.now(
        ) - datetime.timedelta(days=10):
            logger.info("Query is stale")

            self.db.session.delete(cached)
            db.session.commit()
            return False
        else:
            logger.info("Query exists in the database")
            return True

    def get_from_cache(self: object, query: str) -> str:
        """
        Get cached body of a query.
        :param query: <str> TMDB query string
        :return: <str> Body of the query
        """
        logger.info("Query was loaded from the database")

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
            logger.info("User doesn't exist in the database")
            return False
        else:
            logger.info("User exists in the database")
            return True

    def get_user_id(self: object, external_id: str) -> int:
        """
        Get the internal user id to the corresponding external id
        :param external_id: <str> External id provided by OAuth
        :return: <int> Internal user id of a user
        """
        logger.info("user_id was loaded from the database")
        user = User.query.filter_by(external_id_content=external_id).first()
        return user.user_id_content

    def get_user(self: object, external_id: str) -> object:
        """
        Get the user to the corresponding external id
        :param external_id: <str> External id provided by OAuth
        :return: <object> Returns requested user object
        """
        if not self.user_exists(external_id):
            self.user(external_id)

        logger.info("user was loaded from the database")
        return User.query.filter_by(external_id_content=external_id).first()

    def user_country(self: object, external_id: str, country: str) -> None:
        """
        Modify specified user's preferred language.
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
        Modify specified user's preferred language.
        :param external_id: <str> External id provided by OAuth
        :param language: <str> RFC 5646 BCP language tag (e.g. 'de-DE' or 'en-US')
        :return: None
        """
        user = User.query.filter_by(user_id_content=external_id).first()
        user.language = language
        self.db.session.commit()
        logger.info(f"user language changed to: {language}")

    def media_data_exists(self: object, user_id: int, type: str,
                          code: int) -> bool:
        """
        Check if media data exists.
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media to check for existence ("Movie", "TV", "Season", "Episode")
        :param code: <int> Id of the media to check
        :return: <bool> True if media data exists, False if not
        """
        self.check_all_media_types(type)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=type,
            media_id_content=code).first()
        if media_data is None:
            logger.info("media_data entry doesn't exist in database")
            return False
        else:
            logger.info("media_data entry exists in database")
            return True

    def media_data(self: object, user_id: int, type: str, code: int,
                   tv_code: int) -> None:
        """
        Add media data to database
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media to check for existence ("Movie", "TV", "Season", "Episode")
        :param code: <int> Id of the media to set
        :return: None
        """
        self.check_all_media_types(type)
        number_of_watched_episodes = None
        if type == "Season":
            number_of_watched_episodes = 0
        media_data = MediaData(None, None, code, type, user_id,
                               number_of_watched_episodes, tv_code)
        self.db.session.add(media_data)
        self.db.session.commit()

        logger.info("media_data successfully entered into the database")

    def get_media_data_id(self: object, user_id: int, type: str,
                          code: int) -> int:
        """
        Get id of media data
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media to check for existence ("Movie", "TV", "Season", "Episode")
        :param code: <int> Id of the media to get
        :return: <int> Internal id of the media
        """
        self.check_all_media_types(type)
        media_data = MediaData.query.filter_by(user_data_id_content=user_id,
                                               media_type_content=type,
                                               media_id_content=code).first()
        logger.info("media_data_id was loaded from the database")
        return media_data.user_data_id_content

    def rating_exists(self: object, user_id: int, type: str,
                      code: int) -> bool:
        """
        Check if rating exists for a certain media
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media to check for existence of a rating ("Movie", "TV", "Season", "Episode")
        :param code: <int> Id of the media to check existence of a rating for
        :return: <bool> True if rating exists, False if not
        """
        self.check_all_media_types(type)
        media_data = MediaData.query.filter_by(user_data_id_content=user_id,
                                               media_type_content=type,
                                               media_id_content=code).first()
        rating = media_data.rating_content
        if rating is None:
            logger.info("rating doesn't exist in the database")
            return False
        else:
            logger.info("rating exists in the database")
            return True

    def rating(self: object, user_id: int, type: str, code: int,
               rating: int) -> None:
        """
        Add rating for a certain media to the database
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media to set rating for ("Movie", "TV")
        :param code: <int> Id of the media to set rating for
        :param rating: <int> Rating to add to the database
        :return: None
        """
        self.check_all_media_types(type)
        self.check_rating_value(rating, type)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=type,
            media_id_content=code).first()
        media_data.rating_content = rating
        self.db.session.commit()
        logger.info("rating successfully entered into the database")

    def number_of_watched_episodes(self: object, user_id: int, code: int,
                                   number_of_watched_episodes: int) -> None:
        """
        Get the number of watched episodes
        :param user_id: <int> User id of a user
        :param code: <int> Id of the media
        :param number_of_watched_episodes: <int> Get number of watched episodes
        :return: None
        """
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content="Season",
            media_id_content=code).first()
        media_data.number_of_watched_episodes = number_of_watched_episodes
        self.db.session.commit()
        logger.info(
            "number_of_watched_episodes successfully entered into the database"
        )

    def watch_status_exists(self: object, user_id: int, type: str,
                            code: int) -> bool:
        """
        Check if watch status exists for a certain production
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media ("Movie", "TV", "Season", "Episode")
        :param code: <int> Id of the media to check watch status for
        :return: <bool> True of watch status exists, False if not
        """
        self.check_root_media_type(type)
        media_data = MediaData.query.filter_by(user_data_id_content=user_id,
                                               media_type_content=type,
                                               media_id_content=code).first()
        watch_status = media_data.watch_status_content
        if watch_status is None:
            logger.info("watch_status doesnt exist in database")
            return False
        else:
            logger.info("watch_status exists in database")
            return True

    def watch_status(self: object, user_id: int, type: str, code: int,
                     watch_status: str) -> None:
        """
        Add watch status for a certain production to the database
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media to set watch_status for
        :param code: <int> Id of the media to check watch status for
        :param watch_status: <str> Watch status to add to the database
        :return: None
        """
        self.check_watch_status(watch_status)
        self.check_root_media_type(type)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=type,
            media_id_content=code).first()
        media_data.watch_status_content = watch_status
        self.db.session.commit()
        logger.info("watchStatus succesful entered into the database")

    def favorite(self: object, user_id: int, type: str, code: int,
                 favorite: bool) -> None:
        """
        Add favorite for a certain production into the database
        :param user_id: <int> User id of a user
        :param type: <str> Type of the media ("Movie", "TV", "Season", "Episode")
        :param code: <int> Id of the media to check watch status for
        :param favorite: <bool> True if media is favorite, False if not
        :return: None
        """
        self.check_all_media_types(type)
        media_data = MediaData.query.filter_by(
            user_id_content_media_data=user_id,
            media_type_content=type,
            media_id_content=code).first()
        media_data.favorite_content = favorite
        self.db.session.commit()
        logger.info("favorite succesful entered into the database")

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
                "The watchStatus: {} is invalid -> valid arguments:{} ".format(
                    watch_status, valid_watch_status))

    def check_all_media_types(self: object, type: str) -> None:
        """
        Check if type has valid values
        :type: <str> Media type of a certain media
        :return: None
        """
        valid_types = ["TV", "Movie", "Episode", "Season"]
        if type not in valid_types:
            raise InvalidParameter(
                "The type: {} is invalid -> valid arguments:{} ".format(
                    type, valid_types))

    def check_root_media_type(self: object, type: str) -> None:
        """
        Check if media has valid values concerning the watch status and rating mutation
        :param type: <str> Media type of a certain media
        :return: None
        """
        valid_types = ["TV", "Movie"]
        if type not in valid_types:
            raise InvalidParameter(
                "The type: {} is invalid -> valid arguments:{} ".format(
                    type, valid_types))

    def check_rating_value(self: object, rating: int, type: str) -> None:
        """
        Check if rating has valid value concerning the watch rating mutation
        :param rating: <int> Rating value
        :param type: <str> Media type of a certain media
        :return: None
        """
        lower_bound = 0
        upper_bound = 10
        valid_types = ["TV", "Movie"]

        if rating is not None and (rating < lower_bound or rating > upper_bound
                                   ) or type not in valid_types:
            raise InvalidParameter(
                "Please make sure your rating is in range: {}-{} and you only rate types {}"
                .format(lower_bound, upper_bound, valid_types))
