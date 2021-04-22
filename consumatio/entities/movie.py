import dataclasses


@dataclasses.dataclass
class Movie():
    code: int
    title: str
    genres: list
    overview: str
    popularity: float
    vote_average: float
    release_date: str
    runtime: int
    status: str
    backdrops: list
    posters: list
    providers: list
    cast: list
    directors: list
    watch_status: str
    rating: float
    favorite: bool

    @classmethod
    def from_dict(self, dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)