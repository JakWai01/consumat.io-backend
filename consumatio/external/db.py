import sqlite3
import datetime

class Database():
    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS cache(query text UNIQUE, body text, last_changed date)''')

    def cache(self, query, body):
        self.cur.execute('''INSERT INTO CACHE VALUES (:query, :body, :last_changed)''', {"query": query, "body": body, "last_changed": datetime.date.today()})

    def is_cached(self, query):
        self.cur.execute('SELECT * FROM cache WHERE query=:query', {"query": query})

        result = self.cur.fetchall()

        if len(result) != 0 and datetime.date.today() - datetime.timedelta(days = 10) < datetime.datetime.strptime(result[0][2], '%Y-%m-%d').date():
            return True
        else:
            if len(result) != 0 and datetime.date.today() - datetime.timedelta(days = 10) > datetime.datetime.strptime(result[0][2], '%Y-%m-%d').date():
                self.cur.execute('''DELETE FROM cache WHERE query=:query''', {"query": query})

            return False

    def get_from_cache(self, query):
        self.cur.execute('SELECT body from cache WHERE query=:query', {"query": query})

        result = self.cur.fetchall()

        return result[0][0]