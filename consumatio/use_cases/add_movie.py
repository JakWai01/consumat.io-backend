from consumatio.entities.movie import Movie
from consumatio.external.database import Database
import uuid

def add_movie(repo, dict):
    repo.add_movie(Movie.from_dict(dict).to_dict())

repo = Database()

#add_movie(repo=repo, dict=Movie.from_dict(
#    {
#    "code": uuid.uuid4(),
#    "title": "The Matrix",
#    "year": 1999,
#    "regisseur": "The Wichowskis",
#    "rating": 8.7
#    }
#).to_dict())