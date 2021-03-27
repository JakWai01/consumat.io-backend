import sqlite3
import uuid

#con = sqlite3.connect('data.db')

#cur = con.cursor()

# Create Table (only first time)
# cur.execute('''CREATE TABLE movies(code text, title text, year real, regisseur text, rating real)''')

#con.commit()

#con.close()

def add_movie(dict):
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    code = dict.get('code')
    title = dict.get('title')
    year = dict.get('year')
    regisseur = dict.get('regisseur')
    rating = dict.get('rating')

    values = [(str(code), title, year, regisseur, rating)]

    cur.executemany('INSERT INTO movies VALUES (?, ?, ?, ?, ?)', values)
    

    cur.execute('SELECT * FROM movies')
    print(cur.fetchone())
    
    con.commit()
    con.close()


add_movie({
    "code": uuid.uuid4(),
    "title": "The Matrix",
    "year": 1999,
    "regisseur": "The Wichowskis",
    "rating": 8.7
})