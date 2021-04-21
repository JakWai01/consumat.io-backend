import requests
from consumatio.gateways.movie_details_to_dict import *
from consumatio.gateways.movie_providers_to_dict import *
from consumatio.gateways.movie_images_to_dict import *
from consumatio.gateways.movie_credits_to_dict import *
from consumatio.gateways.tv_credits_to_dict import *
from consumatio.gateways.tv_details_to_dict import *
from consumatio.gateways.tv_providers_to_dict import *
from consumatio.gateways.tv_images_to_dict import *
from consumatio.gateways.season_details_to_dict import *
from consumatio.gateways.season_images_to_dict import *
from consumatio.gateways.episode_details_to_dict import *
from consumatio.gateways.episode_images_to_dict import *
from consumatio.gateways.search_result_to_dict import *
from consumatio.external.db import Database
import json


class Tmdb():

    def __init__(self, tmdb_key: str):
        self.db = Database()
        self.api_key = tmdb_key

    def get_movie_details(self, movie_id):
        query = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}&language=en-US'
        data = self.get_data(query, self.db)
        return movie_details_to_dict(data)

    def get_movie_providers(self, movie_id, country):
        query = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        # data = data['results'][country]
        return movie_providers_to_dict(data, country)

    def get_movie_images(self, movie_id):
        query = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_images_to_dict(data)

    def get_movie_credits(self, movie_id):
        query = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return movie_credits_to_dict(data)

    def get_tv_details(self, tv_id):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}?api_key={self.api_key}&language=en-US'
        data = self.get_data(query, self.db)
        return tv_details_to_dict(data)

    def get_tv_providers(self, tv_id, country):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/watch/providers?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        # data = data['results'][country]
        return tv_providers_to_dict(data, country)

    def get_tv_images(self, tv_id):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_images_to_dict(data)

    def get_tv_credits(self, tv_id):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/credits?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return tv_credits_to_dict(data)

    def get_season_details(self, tv_id, season_number):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return season_details_to_dict(data, tv_id)

    def get_season_images(self, tv_id, season_number):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return season_images_to_dict(data)

    def get_episode_details(self, tv_id, season_number, episode_number):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return episode_details_to_dict(data)

    def get_episode_images(self, tv_id, season_number, episode_number):
        query = f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images?api_key={self.api_key}'
        data = self.get_data(query, self.db)
        return episode_images_to_dict(data)

    def get_search(self, str):
        query = f'https://api.themoviedb.org/3/search/multi?api_key={self.api_key}&language=en-US&query={str}&page=1&include_adult=false'
        data = self.get_data(query, self.db)
        return search_result_to_dict(data)

    def get_data(self, query, db):
        if (db.is_cached(query)):
            data = json.loads(db.get_from_cache(query))
        else:
            data = requests.get(query).json()
            db.cache(query, json.dumps(data))
        return data
