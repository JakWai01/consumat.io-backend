import dataclasses
from consumatio.entities.entity import Entity


@dataclasses.dataclass
class Episode(Entity):
    code: int
    title: str
    episode_number: int
    season_number: int
    overview: str
    air_date: str
    rating_average: float
    still_path: str
    rating_user: float
    favorite: bool

    @classmethod
    def from_dict(cls: object, dict: dict) -> object:
        """
        Create Episode object from dictionary
        :param dict: <dict> Dictionary containing all the required variables
        :return: <object> Episode object
        """
        return cls(**dict)

    def to_dict(self: object) -> dict:
        """
        Convert Episode object to dictionary
        :return: <dict> Dictionary containing all the variables from the dataclass object
        """
        return dataclasses.asdict(self)
