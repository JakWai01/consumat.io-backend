import dataclasses

@dataclasses.dataclass
class Episode():
    code: int
    name: str
    episode_number: int
    season_number: int
    overview: str
    air_date: str
    vote_average: float
    stills: list
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)
