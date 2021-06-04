from consumatio.external.db.models import *


def popular_tv_to_dict(data: dict) -> dict:
    """
    Create dictionary for internal representation
    :param data: <dict> API response
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

            dict = {
                "code": result.get("id"),
                "title": result.get("name"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("vote_average"),
                "rating_count": result.get("vote_count"),
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
                "runtime": None
            }

            result_list.append(dict)
        return {"total_pages": data["total_pages"], "results": result_list}
