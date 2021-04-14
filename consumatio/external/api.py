from graphene import ObjectType, String, Schema, Decimal, Int, List, Field, Boolean, Float
from flask import Flask, request
import json
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.usecases.season_details import *
from consumatio.usecases.episode_details import *
import dataclasses
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Movie(ObjectType):
    code = Int()
    title = String()
    genres = List(String)
    overview = String()
    popularity = Float()
    vote_average = Float()
    release_date = String()
    runtime = Int()
    status = String()
    backdrops = List(String)
    posters = List(String)
    providers = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class TV(ObjectType):
    code = Int()
    name = String()
    genres = List(String)
    overview = String()
    popularity = Float()
    vote_average = Float()
    first_air_date = String()
    last_air_date = String()
    status = String()
    backdrops = List(String)
    posters = List(String)
    providers = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class Season(ObjectType):
    code = Int()
    tv_code = Int()
    season_number = Int()
    name = String()
    overview = String()
    posters = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class Episode(ObjectType):
    code = Int()
    name = String()
    episode_number = Int()
    season_number = Int()
    overview = String()
    air_date = String()
    vote_average = Float()
    stills = List(String)
    watch_status = String()
    rating = Float()
    favorite = Boolean()

    @classmethod 
    def from_dict(self, dict):
        return self(**dict)

class Query(ObjectType):
    movie_details = Field(Movie, code=Int(), country=String())
    tv_details = Field(TV, code=Int(), country=String())
    season_details = Field(Season, code=Int(), season_number=Int())
    episode_details = Field(Episode, code=Int(), season_number=Int(), episode_number=Int())

    def resolve_movie_details(root, info, code, country):
        tmdb = Tmdb()
        return Movie.from_dict(movie_details(tmdb, code, country))

    def resolve_tv_details(root, info, code, country):
        tmdb = Tmdb()
        return TV.from_dict(tv_details(tmdb, code, country))

    def resolve_season_details(root, info, code, season_number):
        tmdb = Tmdb()
        return Season.from_dict(season_details(tmdb, code, season_number))

    def resolve_episode_details(root, info, code, season_number, episode_number):
        tmdb = Tmdb()
        return Episode.from_dict(episode_details(tmdb, code, season_number, episode_number))

schema = Schema(query=Query)

@app.route('/graphql', methods=['POST', 'GET'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)