import requests
from consumatio.gateways.movie_gateways.movie_details_to_dict import *
from consumatio.gateways.movie_gateways.movie_providers_to_dict import *
from consumatio.gateways.movie_gateways.movie_images_to_dict import *
from consumatio.gateways.movie_gateways.movie_credits_to_dict import *
from consumatio.gateways.tv_gateways.tv_credits_to_dict import *
from consumatio.gateways.tv_gateways.tv_details_to_dict import *
from consumatio.gateways.tv_gateways.tv_providers_to_dict import *
from consumatio.gateways.tv_gateways.tv_images_to_dict import *
from consumatio.gateways.season_gateways.season_details_to_dict import *
from consumatio.gateways.season_gateways.season_images_to_dict import *
from consumatio.gateways.episode_gateways.episode_details_to_dict import *
from consumatio.gateways.episode_gateways.episode_images_to_dict import *
from consumatio.gateways.search_gateways.search_result_to_dict import *
from consumatio.gateways.popular_gateways.popular_tv_to_dict import *
from consumatio.gateways.popular_gateways.popular_movies_to_dict import *
from consumatio.external.db import Database
from consumatio.external.logger import get_logger_instance
import json

logger = get_logger_instance()


class Tmdb():
    def __init__(self: object, tmdb_key: str):
        self.db = Database()
        self.api_key = tmdb_key

    def get_movie_details(self: object, movie_id: int) -> dict:
        """
        Fetch tmdb movie details endpoint
        :param movie_id: <int> Id of the movie to fetch details for
        :return: <dict> Movie details
        """
        logger.info("Request:'movie_details' transmitted to databse")
        query = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}&language=en-US'
        data = self.get_data(query, self.db)
        return movie_details_to_dict(data)

    def get_movie_providers(self: object, movie_id: int, country: str) -> dict:
        """
        Fetch tmdb movie providers endpoint
        :param movie_id: <int> Id of the movie to fetch details for
        :param country: <str> Country abbreviations to fetch providers for (e.g. "DE" -> Germany)
        :return: <dict> Movie providers
        """
        logger.info("Request:'movie_providers' transmitted to databse")
        query = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_providers_to_dict(data, country)

    def get_movie_images(self: object, movie_id: int) -> dict:
        """
        Fetch tmdb movie images endpoint
        :param movie_id: <int> Id of the movie to fetch providers images for
        :return: <dict> Movie images
        """
        logger.info("Request:'movie_images' transmitted to databse")
        query = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_images_to_dict(data)

    def get_movie_credits(self: object, movie_id: int) -> dict:
        """
        Fetch tmdb movie credits endpoint
        :param movie_id: <int> Id of the movie to fetch credits for
        :return: <dict> Movie credits
        """
        logger.info("Request:'movie_credits' transmitted to databse")
        query = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_credits_to_dict(data)

    def get_tv_details(self: object, tv_id: int) -> dict:
        """
        Fetch tmdb tv details endpoint
        :param tv_id: <int> Id of the tv show to fetch details for
        :return: <dict> TV show details
        """
        logger.info("Request:'tv_details' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}?api_key={self.api_key}&language=en-US'
        data = self.get_data(query, self.db)
        return tv_details_to_dict(data)

    def get_tv_providers(self: object, tv_id: int, country: str) -> dict:
        """
        Fetch tmdb tv providers endpoint
        :param tv_id: <int> Id of the tv show to fetch providers for
        :param country: <str> Country abbreviation to fetch providers for (e.g. "DE" -> Germany)
        :return: <dict> TV show providers
        """
        logger.info("Request:'tv_providers' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/watch/providers?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_providers_to_dict(data, country)

    def get_tv_images(self: object, tv_id: int) -> dict:
        """
        Fetch tmdb tv images endpoint
        :param tv_id: <int> Id of the tv show to fetch images for
        :return: <dict> TV show images
        """
        logger.info("Request:'tv_images' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_images_to_dict(data)

    def get_tv_credits(self: object, tv_id: int) -> dict:
        """
        Fetch tmdb tv credits endpoint
        :param tv_id: <int> Id of the tv show to fetch credits for
        :return: <dict> TV show credits 
        """
        logger.info("Request:'tv_credits' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/credits?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_credits_to_dict(data)

    def get_season_details(self: object, tv_id: int,
                           season_number: int) -> dict:
        """
        Fetch tmdb season details endpoint
        :param tv_id: <int> Id of the tv show to fetch season details for
        :param season_number: <int> Number of the season to get details for
        :return: <dict> Season details
        """
        logger.info("Request:'season_details' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return season_details_to_dict(data, tv_id)

    def get_season_images(self: object, tv_id: int,
                          season_number: int) -> dict:
        """
        Fetch tmdb season images endpoint
        :param tv_id: <int> Id of the tv show to fetch season images for
        :param season_number: <int> Number of the season to get images for
        :return: <dict> Season images
        """
        logger.info("Request:'season_images' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return season_images_to_dict(data)

    def get_episode_details(self: object, tv_id: int, season_number: int,
                            episode_number: int) -> dict:
        """
        Fetch tmdb episode details endpoint
        :param tv_id: <int> Id of the tv show to fetch episode details for
        :param season_number: <int> Number of the season which contains the searched episode
        :param episode_number: <int> Number of the searched episode in the corresponding season
        :return: <dict> Episode details
        """
        logger.info("Request:'episode_details' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return episode_details_to_dict(data)

    def get_episode_images(self: object, tv_id: dict, season_number: int,
                           episode_number: int) -> dict:
        """
        Fetch tmdb episode images endpoint
        :param tv_id: <int> Id of the tv show to fetch episode images for
        :param season_number: <int> Number of the season which contains the searched episode
        :param episode_number: <int> Number of the searched episode in the corresponding season
        :return: <dict> Episode images 
        """
        logger.info("Request:'episode_images' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return episode_images_to_dict(data)

    def get_search(self: object, keyword: str) -> dict:
        """
        Fetch tmdb search endpoint
        :param keyword: <str> Search string
        :return: <dict> Search results
        """
        logger.info("Request:'search' transmitted to databse")
        query = f'https://api.themoviedb.org/3/search/multi?api_key={self.api_key}&language=en-US&query={keyword}&page=1&include_adult=false'
        data = self.get_data(query, self.db)
        return search_result_to_dict(data)

    def get_popular_movies(self: object, country: str) -> dict:
        """
        Fetch tmdb popular movies endpoint
        :param country: <str> country ISO 3166-1 code (must be uppercase) to get region specific results 
        :return: <dict> movie results
        """
        logger.info("Request:'popular_movies' transmitted to databse")
        query = f'https://api.themoviedb.org/3/movie/popular?api_key={self.api_key}&language=en-US&region={country}&page=1&include_adult=false'
        data = self.get_data(query, self.db)
        return popular_movies_to_dict(data)

    def get_popular_tv(self: object) -> dict:
        """
        Fetch tmdb popular tv shows endpoint
        :return: <dict> tv results
        """
        logger.info("Request:'popular_tv' transmitted to databse")
        query = f'https://api.themoviedb.org/3/tv/popular?api_key={self.api_key}&language=en-US&page=1&include_adult=false'
        data = self.get_data(query, self.db)
        return popular_tv_to_dict(data)

    def get_data(self: object, query: str, db: object) -> dict:
        """
        Check if data is cached and get the data then either from the cache or by making a new API request.
        :param query: <str> API query
        :param db: <object> Database object
        :return: <dict> Return response of the query
        """
        if (db.is_cached(query)):
            data = json.loads(db.get_from_cache(query))
        else:
            data = requests.get(query).json()
            db.cache(query, json.dumps(data))
        return data
