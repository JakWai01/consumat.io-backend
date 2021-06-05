from consumatio.external.db.models import *


def popular_movies_to_dict(data: dict) -> dict:
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
                "title": result.get("title"),
                "genres": None,
                "overview": result.get("overview"),
                "popularity": result.get("popularity"),
                "rating_average": result.get("vote_average"),
                "rating_count": result.get("vote_count"),
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
            }

            result_list.append(dict)

        return {"total_pages": data["total_pages"], "results": result_list}
