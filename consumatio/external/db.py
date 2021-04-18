import sqlite3
import datetime

class Database():

    def cache(self, query, body):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS cache(query text UNIQUE, body text, last_changed date)''')

        cur.execute('''INSERT INTO CACHE VALUES (:query, :body, :last_changed)''', {"query": query, "body": body, "last_changed": datetime.date.today()})

        con.commit()
        con.close()

    def is_cached(self, query):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS cache(query text UNIQUE, body text, last_changed date)''')

        cur.execute('SELECT * FROM cache WHERE query=:query', {"query": query})

        result = cur.fetchall()

        if len(result) != 0 and datetime.date.today() - datetime.timedelta(days = 10) < datetime.datetime.strptime(result[0][2], '%Y-%m-%d').date():
            con.commit()
            con.close()
            return True
        else:
            con.commit()
            con.close()
            return False

    def get_from_cache(self, query):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()

        cur.execute('SELECT body from cache WHERE query=:query', {"query": query})

        result = cur.fetchall()

        return result[0][0]