import dataclasses

@dataclasses.dataclass
class Episode():
    id: int 
    season_number: int 
    episode_number: int
    name: str
    overview: str
    vote_average: float
    air_date: str
    stills: dict
    
    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)