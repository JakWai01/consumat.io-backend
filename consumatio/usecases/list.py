from consumatio.usecases.movie_details import MovieDetails
from consumatio.usecases.tv_details import TVDetails


class List:
    def get_list(tmdb: object, user: str, type: str, watchStatus: str):
        watch_list = []
        results = query where user == user and watch_status == watch_status and type == type

        for result in results:
            if type == "Movie":
                movie_details = MovieDetails()
                watch_list.append(movie_details.get_movie_details(tmdb, result.code, "DE"))
            elif type == "TV":
                tv_details = TVDetails()
                watch_list.append(tv_details.get_tv_details(tmdb, result.code, "DE"))

        return watch_list