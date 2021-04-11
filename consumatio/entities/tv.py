import dataclasses

@dataclasses.dataclass
class TV():
    id: int 
    name: str
    genres: dict
    overview: str
    popularity: float
    vote_average: float
    first_air_date: str
    last_air_date: int
    status: str
    # Possibility to request different image sizes (not from api)
    backdrop: dict
    posters: dict
    # Possibility to get providers according to provided country
    providers: dict 
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)