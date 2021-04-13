from graphene import ObjectType, String, Schema, Decimal, Int, List, Field, Boolean, Float
from flask import Flask, request
import json
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *

app = Flask(__name__)

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

class Query(ObjectType):
    movie_details = Field(Movie, code=Decimal(), country=String())

    def resolve_movie_details(root, info, code, country):
        tmdb = Tmdb()
        return Movie.from_dict(movie_details(tmdb, code, country))

schema = Schema(query=Query)

@app.route('/graphql', methods=['GET'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)