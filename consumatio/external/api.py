from ariadne import ObjectType, QueryType, gql, make_executable_schema, graphql_sync
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.usecases.season_details import *
from consumatio.usecases.episode_details import *
from consumatio.usecases.search_details import *
from flask import Flask, request, jsonify
from ariadne.constants import PLAYGROUND_HTML
import os


# TODO @Danny: Fix the error which is probably caused because we get
#              a list with objects

type_defs = gql("""
    type Query {
        movie(code: Int, country: String): Movie!
        tv(code: Int, country: String): TV!
        season(code: Int, seasonNumber: Int): Season!
        episode(code: Int, seasonNumber: Int, episodeNumber: Int): Episode!
        search(str: String): [[String]]!
    }

    type Movie {
        code: Int
        title: String
        genres: [String]
        overview: String
        popularity: Float
        voteAverage: Float
        releaseDate: String
        runtime: Int
        status: String
        backdrops: String
        posters: String
        providers: [String]
        watchStatus: String
        rating: Float
        favorite: Boolean
    }

    type TV {
        code: Int
        name: String
        genres: [String]
        overview: String
        popularity: Float
        voteAverage: Float
        firstAirDate: String
        lastAirDate: String
        status: String
        backdrops: String
        posters: String
        providers: [String]
        watchStatus: String
        rating: Float
        favorite: Boolean
    }

    type Season {
        code: Int
        tvCode: Int
        seasonNumber: Int
        name: String
        overview: String
        posters: String
        watchStatus: String
        rating: Float
        favorite: Boolean
    }

    type Episode {
        code: Int
        name: String
        episodeNumber: Int
        seasonNumber: Int
        overview: String
        airDate: String
        voteAverage: Float 
        stills: String
        watchStatus: String
        rating: Float
        favorite: Boolean
    }
""")

app = Flask(__name__)

query = QueryType()


@query.field("movie")
def resolve_movie(*_, code, country):
    tmdb = Tmdb()
    return movie_details(tmdb, code, country)


movie = ObjectType("Movie")


@query.field("tv")
def resolve_tv(*_, code, country):
    tmdb = Tmdb()
    return tv_details(tmdb, code, country)


tv = ObjectType("TV")


@query.field("season")
def resolve_season(*_, code, seasonNumber):
    tmdb = Tmdb()
    return season_details(tmdb, code, seasonNumber)


season = ObjectType("Season")


@query.field("episode")
def resolve_episode(*_, code, seasonNumber, episodeNumber):
    tmdb = Tmdb()
    return episode_details(tmdb, code, seasonNumber, episodeNumber)


episode = ObjectType("Episode")


@query.field("search")
# TODO @Danny: Implement minLength: 2
#                         pattern:([a-z]{2})-([A-Z]{2})
def resolve_search(*_, str):
    tmdb = Tmdb()
    return search_details(tmdb, str)


#search = ObjectType("Search")


schema = make_executable_schema(type_defs, query, movie, tv, season)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


port = int(os.environ['PORT'])

if __name__ == "__main__":
    app.run(debug=True, port=port, host="0.0.0.0")
