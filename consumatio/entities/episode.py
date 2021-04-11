import dataclasses


@dataclasses.dataclass
class Episode():
    code: int
    title: str
    episode_number: int
    season_number: int
    overview: str
    release_date: str
    vote_average: float
    vote_count: int
    stills: dict

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)
