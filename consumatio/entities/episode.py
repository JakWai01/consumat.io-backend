import dataclasses
from consumatio.entities.entity import Entity


@dataclasses.dataclass
class Episode(Entity):
    code: int
    name: str
    episode_number: int
    season_number: int
    overview: str
    air_date: str
    vote_average: float
    still: str
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self: object, dict: dict) -> object:
        """
        Create Episode object from dictionary
        :param dict: <dict> Dictionary containing all the required variables
        :return: <object> Episode object
        """
        return self(**dict)

    def to_dict(self: object) -> dict:
        """
        Convert Episode object to dictionary
        :return: <dict> Dictionary containing all the variables from the dataclass object
        """
        return dataclasses.asdict(self)
