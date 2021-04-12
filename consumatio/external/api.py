from graphene import ObjectType, String, Schema, Decimal, Int, List, Field
from flask import Flask, request
import json
from consumatio.external.tmdb import Tmdb

app = Flask(__name__)

class Movie(ObjectType):
    code = Int()
    title = String() 
    genres = List(String)
    overview = String()
    popularity = Decimal()
    vote_average = Decimal()
    release_date = String()
    runtime = Int()
    status = String()

class Query(ObjectType):
    movie_details = Field(Movie, id=Decimal())

    def resolve_movie_details(root, info, id):
        tmdb = Tmdb()
        dict = tmdb.get_movie_details(id)
        return Movie(code=dict.get("code"), title=dict.get("title"), genres=dict.get("genres"), overview=dict.get("overview"), popularity=dict.get("popularity"), vote_average=dict.get("vote_average"), release_date=dict.get("release_date"), runtime=dict.get("runtime"), status=dict.get("status"))

schema = Schema(query=Query)

@app.route('/graphql', methods=['GET'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)