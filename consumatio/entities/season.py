import dataclasses
from consumatio.entities.entity import Entity

@dataclasses.dataclass
class Season(Entity):
    code: int
    tv_code: int
    season_number: int
    name: str
    overview: str
    poster: str
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)