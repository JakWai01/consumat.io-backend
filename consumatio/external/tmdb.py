import requests
from consumatio.gateways.movie_details_to_dict import * 
from consumatio.gateways.movie_providers_to_dict import * 
from consumatio.gateways.movie_images_to_dict import *
from consumatio.gateways.tv_details_to_dict import *
from consumatio.gateways.tv_providers_to_dict import *

class Tmdb():
    
    def get_movie_details(self, movie_id):
        data = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c4bd02adee6e73c4d17e69b039267c90&language=en-US').json()
        return movie_details_to_dict(data)

    def get_movie_providers(self, movie_id, country):
        data = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        data = data['results'][country]
        return movie_providers_to_dict(data)

    # add possibility to specify size
    def get_movie_images(self, movie_id):
        data = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        return movie_images_to_dict(data)

    def get_tv_details(self, tv_id):
        data = requests.get(f'https://api.themoviedb.org/3/tv/{tv_id}?api_key=c4bd02adee6e73c4d17e69b039267c90&language=en-US').json()
        return tv_details_to_dict(data)

    def get_tv_providers(self, tv_id, country):
        data = requests.get(f'https://api.themoviedb.org/3/tv/{tv_id}/watch/providers?api_key=c4bd02adee6e73c4d17e69b039267c90').json()
        data = data['results'][country]
        return tv_providers_to_dict(data)

    def get_tv_images(self):    
        pass

    def get_season_details(self):
        pass

    def get_season_images(self):
        pass

    def get_episode_details(self):
        pass

    def get_episode_images(self):
        pass

tmdb = Tmdb()
print(tmdb.get_tv_providers(1399, "AR"))