from consumatio.entities.movie import Movie


def popular_movies_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :return: <dict> Internal representation
    """
    if "results" not in data:
        return []
    elif len(data["results"]) == 0:
        return []
    else:
        results = data["results"]
        result_list = []

        for result in results:
            dict = {
                "code": result.get("id"),
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("vote_average"),
                "release_date": result.get("release_date"),
                "runtime": None,
                "status": None,
                "backdrop_path": result.get("backdrop_path"),
                "poster_path": result.get("poster_path"),
                "providers": None,
                "cast": None,
                "directors": None,
                "tmdb_url":
                f'https://www.themoviedb.org/movie/{result.get("id")}',
                "watch_status": None,
                "rating_user": None,
                "favorite": None
            }

            movie = Movie.from_dict(dict)

            dict = movie.to_dict()

            dict["__typename"] = "Movie"

            result_list.append(dict)
        return result_list
