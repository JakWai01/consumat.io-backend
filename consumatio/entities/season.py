import dataclasses


@dataclasses.dataclass
class Season():
    code: int
    tv_code: int
    season_number: int
    name: str
    overview: str
    posters: dict
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)