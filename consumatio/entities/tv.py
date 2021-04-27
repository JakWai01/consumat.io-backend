import dataclasses
from consumatio.entities.entity import Entity


@dataclasses.dataclass
class TV(Entity):
    code: int
    name: str
    genres: list
    overview: str
    popularity: float
    vote_average: float
    first_air_date: str
    last_air_date: str
    status: str
    backdrop: str
    poster: str
    providers: list
    creators: list
    cast: list
    number_of_episodes: int
    number_of_seasons: int
    tmdb: str
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self: object, dict: dict) -> object:
        """
        Create TV object from dictionary
        :param dict: <dict> Dictionary containing all the required variables
        :return: <object> TV object
        """
        return self(**dict)

    def to_dict(self: object) -> dict:
        """
        Convert TV object to dictionary
        :return: <dict> Dictionary containing all the variables from the dataclass object
        """
        return dataclasses.asdict(self)