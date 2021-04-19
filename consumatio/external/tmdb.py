import requests
from consumatio.gateways.movie_details_to_dict import *
from consumatio.gateways.movie_providers_to_dict import *
from consumatio.gateways.movie_images_to_dict import *
from consumatio.gateways.tv_details_to_dict import *
from consumatio.gateways.tv_providers_to_dict import *
from consumatio.gateways.tv_images_to_dict import *
from consumatio.gateways.season_details_to_dict import *
from consumatio.gateways.season_images_to_dict import *
from consumatio.gateways.episode_details_to_dict import *
from consumatio.gateways.episode_images_to_dict import *
from consumatio.gateways.search_result_to_dict import *


class Tmdb():

    def get_movie_details(self, movie_id):
        data = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c4bd02adee6e73c4d17e69b039267c90&language=en-US').json()
        return movie_details_to_dict(data)

    def get_movie_providers(self, movie_id, country):
        data = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        data = data['results'][country]
        return movie_providers_to_dict(data)

    def get_movie_images(self, movie_id):
        data = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return movie_images_to_dict(data)

    def get_tv_details(self, tv_id):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}?api_key=c4bd02adee6e73c4d17e69b039267c90&language=en-US').json()
        return tv_details_to_dict(data)

    def get_tv_providers(self, tv_id, country):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}/watch/providers?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        data = data['results'][country]
        return tv_providers_to_dict(data)

    def get_tv_images(self, tv_id):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}/images?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return tv_images_to_dict(data)

    def get_season_details(self, tv_id, season_number):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return season_details_to_dict(data, tv_id)

    def get_season_images(self, tv_id, season_number):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/images?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return season_images_to_dict(data)

    def get_episode_details(self, tv_id, season_number, episode_number):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return episode_details_to_dict(data)

    def get_episode_images(self, tv_id, season_number, episode_number):
        data = requests.get(
            f'https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return episode_images_to_dict(data)

    def get_search_details(self, str):
        data = requests.get(
            f'https://api.themoviedb.org/3/search/multi?api_key=c4bd02adee6e73c4d17e69b039267c90&language=en-US&query={str}&page=1&include_adult=false').json()
        return search_result_to_dict(data)
