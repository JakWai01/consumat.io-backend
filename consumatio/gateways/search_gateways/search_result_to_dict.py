from consumatio.entities.movie import Movie
from consumatio.entities.tv import TV


def search_result_to_dict(data: dict) -> dict:
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
            if result.get("media_type") == "tv":
                dict = {
                    "code": result.get("id"),
                    "title": result.get("name"),
                    "genres": None,
                    "overview": result.get("overview"),
                    "popularity": result.get("popularity"),
                    "rating_average": result.get("vote_average"),
                    "first_air_date": result.get("first_air_date"),
                    "last_air_date": None,
                    "status": None,
                    "backdrop_path": result.get("backdrop_path"),
                    "poster_path": result.get("poster_path"),
                    "providers": None,
                    "creators": None,
                    "cast": None,
                    "number_of_episodes": None,
                    "number_of_seasons": None,
                    "tmdb_url":
                    f'https://www.themoviedb.org/tv/{result.get("id")}',
                    "watch_status": None,
                    "rating_user": None,
                    "favorite": None
                }

                tv = TV.from_dict(dict)

                dict = tv.to_dict()

                dict["__typename"] = "TV"
            elif result.get("media_type") == "movie":
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
            else:
                continue
            result_list.append(dict)
        return result_list
