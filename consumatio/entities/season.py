import dataclasses

@dataclasses.dataclass
class Season():
    id: int
    tv_id: int
    season_number: int
    name: str
    overview: str
    # images endpoint
    posters: dict 
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self,dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)