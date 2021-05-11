import datetime
from consumatio.external.models import *
from consumatio.external.logger import get_logger_instance

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
        db.session.add(cache)
        db.session.commit()

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
            
            db.session.delete(cached)
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
