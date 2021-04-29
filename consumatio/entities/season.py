import dataclasses
from consumatio.entities.entity import Entity


@dataclasses.dataclass
class Season(Entity):
    code: int
    tv_code: int
    season_number: int
    title: str
    overview: str
    poster_path: str
    watch_status: str
    rating_user: float
    favorite: bool

    @classmethod
    def from_dict(self: object, dict: dict) -> object:
        """
        Create Season object from dictionary
        :param dict: <dict> Dictionary containing all the required variables
        :return: <object> Season object
        """
        return self(**dict)

    def to_dict(self: object) -> dict:
        """
        Convert Season object to dictionary
        :return: <dict> Dictionary containing all the variables from the dataclass object
        """
        return dataclasses.asdict(self)