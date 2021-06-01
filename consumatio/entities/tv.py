import dataclasses
from consumatio.entities.entity import Entity


@dataclasses.dataclass
class TV(Entity):
    code: int
    title: str
    genres: list
    overview: str
    popularity: float
    rating_average: float
    rating_count: int
    first_air_date: str
    last_air_date: str
    status: str
    backdrop_path: str
    poster_path: str
    providers: list
    cast: list
    creators: list
    number_of_episodes: int
    number_of_seasons: int
    tmdb_url: str
    watch_status: str
    rating_user: int
    favorite: bool
    runtime: int

    @classmethod
    def from_dict(cls: object, dict: dict) -> object:
        """
        Create TV object from dictionary
        :param dict: <dict> Dictionary containing all the required variables
        :return: <object> TV object
        """
        return cls(**dict)

    def to_dict(self: object) -> dict:
        """
        Convert TV object to dictionary
        :return: <dict> Dictionary containing all the variables from the dataclass object
        """
        return dataclasses.asdict(self)