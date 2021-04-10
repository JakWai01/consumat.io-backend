from graphene import ObjectType, String, Schema, Decimal
from flask import Flask, request
from consumatio.external.database import Database
from consumatio.use_cases.add_movie import *
import json
import uuid

app = Flask(__name__)

class Query(ObjectType):
    addMovie = String(title=String(default_value="---"), year=Decimal(default_value=0), regisseur=String(default_value="---"), rating=Decimal(default_value=0))
    hello = String()

    def resolve_addMovie(root, info, title, year, regisseur, rating):
        repo = Database()

        add_movie(repo=repo, dict=Movie.from_dict(
             {
                 "code": uuid.uuid4(),
                 "title": title,
                 "year": int(year),
                 "regisseur": regisseur,
                 "rating": float(rating)
             }
        ).to_dict())

        return f'Added {title}'

    def resolve_hello(root, info):
        dict = {"num1": 1, "num2": 2, "name": "Jakob"}
        return dict

schema = Schema(query=Query)

@app.route('/graphql', methods=['POST'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)