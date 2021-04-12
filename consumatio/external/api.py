from graphene import ObjectType, String, Schema, Decimal
from flask import Flask, request
import json
from consumatio.external.tmdb import Tmdb

app = Flask(__name__)

class Query(ObjectType):
    movieDetails = String(id=Decimal())

    def resolve_movieDetails(root, info, id):
        tmdb = Tmdb()
        return tmdb.get_movie_details(id)

schema = Schema(query=Query)

@app.route('/graphql', methods=['GET'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)