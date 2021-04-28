from ariadne import ObjectType, QueryType, gql, make_executable_schema, graphql_sync, load_schema_from_path
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.usecases.season_details import *
from consumatio.usecases.episode_details import *
from consumatio.usecases.search_details import *
from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne.constants import PLAYGROUND_HTML
import os

app = Flask(__name__)
CORS(app)

query = QueryType()


# couldn't add type annotation on this parameter
def tmdb_client(api_key=os.getenv('TMDB_KEY')) -> object:
    """
    Create a tmdb client.
    :param api_key: <str> API key for tmdb provided in an environment variable
    :return: <object> Tmdb object
    """
    return Tmdb(api_key)


@query.field("movie")
def resolve_movie(*_, code: int, country: str) -> dict:
    """
    API endpoint for "movie" queries.
    :param code: <int> Id of the movie to get details for
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :return: <dict> Details of the movie
    """
    tmdb = tmdb_client()
    movie = MovieDetails()
    return movie.get_movie_details(tmdb, code, country)


movie = ObjectType("Movie")


@query.field("tv")
def resolve_tv(*_, code: int, country: str) -> dict:
    """
    API endpoint for "tv" queries.
    :param code: <int> Id of the tv show to get details for
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :return: <dict> Details of the tv show
    """
    tmdb = tmdb_client()
    tv = TVDetails()
    return tv.get_tv_details(tmdb, code, country)


tv = ObjectType("TV")


@query.field("season")
def resolve_season(*_, code: int, seasonNumber: str) -> dict:
    """
    API endpoint for "season" queries.
    :param code: <int> Id of the tv show to get details for
    :param seasonNumber: <int> Number of the season to get details for
    :return: <dict> Details of the season 
    """
    tmdb = tmdb_client()
    season = SeasonDetails()
    return season.get_season_details(tmdb, code, seasonNumber)


season = ObjectType("Season")


@query.field("episode")
def resolve_episode(*_, code: int, seasonNumber: int,
                    episodeNumber: int) -> dict:
    """
    API endpoint for "episode" queries.
    :param code: <int> Id of the tv show to get details for
    :param seasonNumber: <int> Number of the season to get details for
    :param episodeNumber: <int> Number of the episode to get details for
    :return: <dict> Details of the episode
    """
    tmdb = tmdb_client()
    episode = EpisodeDetails()
    return episode.get_episode_details(tmdb, code, seasonNumber, episodeNumber)


episode = ObjectType("Episode")


@query.field("search")
def resolve_search(*_, keyword: str) -> dict:
    """
    API endpoint for "search" queries.
    :param keyword: <str> search string
    :return: <dict> Results of the search
    """
    tmdb = tmdb_client()
    search = SearchDetails()
    return search.get_search_details(tmdb, keyword)


search = ObjectType("Search")

type_defs = load_schema_from_path("consumatio/external/api.schema")
schema = make_executable_schema(type_defs, query, movie, tv, season, search)


@app.route("/", methods=["GET"])
def graphql_playground() -> str:
    """
    If get request was made on "/", route to playground.
    :return: <str>, <statuscode> Return playground html with status code 200
    """
    return PLAYGROUND_HTML, 200


@app.route("/", methods=["POST"])
def graphql_server() -> str:
    """
    If post request was made on "/", resolve the queries.
    :return: <str>, <statuscode> Return response to request with statuscode (200 or 400)
    """
    data = request.get_json()

    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code


port = int(os.environ['PORT'])

if __name__ == "__main__":
    app.run(debug=True, port=port, host="0.0.0.0")
