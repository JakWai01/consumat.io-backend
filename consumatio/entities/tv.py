import dataclasses

@dataclasses.dataclass
class TV():
    code: int 
    name: str
    genres: list 
    overview: str
    popularity: float
    vote_average: float
    first_air_date: str
    last_air_date: str
    status: str
    backdrops: list 
    posters: list    
    providers: list 
    creators: list
    cast: list
    number_of_episodes: int
    number_of_seasons: int
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)