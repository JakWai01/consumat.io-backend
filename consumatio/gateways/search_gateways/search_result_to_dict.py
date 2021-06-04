from consumatio.entities.movie import Movie
from consumatio.entities.tv import TV
from consumatio.external.db.models import *


def search_result_to_dict(data: dict, external_id: str) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
    :param external_id: <str> External representation of the user
    :return: <dict> Internal representation
    """
    result_list = []
    if "results" not in data:
        return result_list
    elif len(data["results"]) == 0:
        return result_list
    else:
        results = data["results"]

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
                    "runtime": None,
                    "rating_count": result.get("vote_count")
                }

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
                    "rating_count": result.get("vote_count")
                }
            else:
                continue
            result_list.append(dict)
        return {"total_pages": data["total_pages"], "results": result_list}
