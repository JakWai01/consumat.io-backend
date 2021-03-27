from ..entities.movie import Movie

def add_movie(repo, dict):
    repo.add(Movie.from_dict(dict).to_dict())