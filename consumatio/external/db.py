import sqlite3
import datetime
from consumatio.external.models import *


class Database():
    def __init__(self, db):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        db = db

        cur.execute(
            '''CREATE TABLE IF NOT EXISTS cache(query text UNIQUE, body text, last_changed date)'''
        )

        con.commit()
        con.close()

    def cache(self: object, query: str, body: str) -> None:
        """
        Cache the provided query and the respective result in the database.
        :param query: <str> Tmdb query string
        :param body: <str> Response of the query 
        """
        cache = Cache(query, body)
        db.session.add(cache)
        db.session.commit()

    def is_cached(self: object, query: str) -> bool:
        """
        Checks if a query is cached in the database.
        :param query: <str> Tmdb query string
        :return: <bool> Returns true if the query is cached, else false 
        """
        cached = Cache.query.filter_by(query_content=query).first()

        if cached == None:
            return False
        elif (cached.last_changed - datetime.datetime.now()).days >= 10:
            db.session.delete(cached)

            return False
        else:
            return True

    def get_from_cache(self: object, query: str) -> str:
        """
        Get body of a query out of the database if the query was cached.
        :param query: <str> tmdb query string
        :return: <str> body of query
        """
        return Cache.query.filter_by(query_content=query).first().body_content
