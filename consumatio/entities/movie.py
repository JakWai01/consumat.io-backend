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
    def from_dict(self: object, dict: dict) -> object:
        """
        Create Movie object from dictionary
        :param dict: <dict> Dictionary containing all the required variables
        :return: <object> Movie object
        """
        return self(**dict)

    def to_dict(self: object) -> dict:
        """
        Convert Movie object to dictionary
        :return: <dict> Dictionary containing all the variables from the dataclass object
        """
        return dataclasses.asdict(self)