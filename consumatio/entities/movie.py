import dataclasses
from consumatio.entities.entity import Entity


@dataclasses.dataclass
class Movie(Entity):
    code: int
    title: str
    genres: list
    overview: str
    popularity: float
    vote_average: float
    release_date: str
    runtime: int
    status: str
    backdrop: str
    poster: str
    providers: list
    cast: list
    directors: list
    tmdb: str
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)