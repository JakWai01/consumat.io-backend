from consumatio.entities.movie import Movie


class MovieDetails:
    def get_movie_details(self: object, tmdb: object, code: int, country: str) -> dict:
        """
        Make all relevant API requests for this usecase (details, images, providers, credits) and assemble them into a dictionary
        :param tmdb: <object> Tmdb object
        :param code: <int> Id of the movie to get data for
        :country: <str> Country abbreveation of the country to get providers for (e.g. "DE" -> Germany)
        :return: <dict> Movie details
        """
        dict_movie_details = tmdb.get_movie_details(code)
        dict_movie_images = tmdb.get_movie_images(code)
        dict_movie_providers = tmdb.get_movie_providers(code, country)
        dict_movie_credits = tmdb.get_movie_credits(code)

        dict = {
            "code": dict_movie_details.get("code"),
            "title": dict_movie_details.get("title"),
            "genres": dict_movie_details.get("genres"),
            "overview": dict_movie_details.get("overview"),
            "popularity": dict_movie_details.get("popularity"),
            "ratingAverage": dict_movie_details.get("vote_average"),
            "releaseDate": dict_movie_details.get("release_date"),
            "runtime": dict_movie_details.get("runtime"),
            "status": dict_movie_details.get("status"),
            "backdropPath": dict_movie_images.get("backdrop"),
            "posterPath": dict_movie_images.get("poster"),
            "providers": dict_movie_providers.get("providers"),
            "cast": dict_movie_credits.get("cast"),
            "directors": dict_movie_credits.get("directors"),
            "tmdbUrl":
            f'https://www.themoviedb.org/movie/{dict_movie_details.get("code")}',
            "watchStatus": None,
            "ratingUser": None,
            "favorite": None
        }

        return dict