import uuid
from consumatio.entities.movie import Movie


def test_room():
    code = uuid.uuid4()
    movie = Movie(
        code=code,
        title="The Matrix",
        year=1999, 
        regisseur="The Wachowskis",
        rating=8.7
        )

    assert movie.code == code
    assert movie.title == "The Matrix"
    assert movie.year == 1999
    assert movie.regisseur == "The Wachowskis"
    assert movie.rating == 8.7


def test_room_model_comparison():
    dict = {
        "code": uuid.uuid4(),
        "title": "The Matrix",
        "year": 1999,
        "regisseur": "The Wachowskis",
        "rating": 8.7
    }

    movie1 = Movie.from_dict(dict)
    movie2 = Movie.from_dict(dict)

    assert movie1 == movie2
