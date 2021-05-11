from ariadne import ObjectType, QueryType, gql, make_executable_schema, graphql_sync, load_schema_from_path, UnionType
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.usecases.season_details import *
from consumatio.usecases.episode_details import *
from consumatio.usecases.search_details import *
from consumatio.usecases.popular_details import *
from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne.constants import PLAYGROUND_HTML
from consumatio.external.exceptions import UndefinedEnvironmentVariable
from consumatio.external.models import *
import os
from flask import request
from flask import Flask
from flask_migrate import Migrate

DATABASE_URI = os.getenv('DATABASE_URI')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
CORS(app)

db.init_app(app)

query = QueryType()

TMDB_KEY_KEY = 'TMDB_KEY'
BACKEND_SECRET = os.getenv('BACKEND_SECRET')

CONSUMATIO_NAMESPACE_HEADER_KEY = 'X-Consumatio-Namespace'
CONSUMATIO_SECRET_HEADER_KEY = 'X-Consumatio-Secret'

api_key = os.getenv(TMDB_KEY_KEY)

if (api_key == None):
    raise UndefinedEnvironmentVariable(
        "Please specify a valid API key for TMDB_KEY environment variable")

tmdb = Tmdb(api_key, db)

migrate = Migrate(app, db)


@query.field("movie")
def resolve_movie(*_, code: int, country: str) -> dict:
    """
    API endpoint for "movie" queries.
    :param code: <int> Id of the movie to get details for
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :return: <dict> Details of the movie
    """
    movie = MovieDetails()
    return movie.get_movie_details(tmdb, code, country)


movie = ObjectType("Movie")

movie.set_alias("ratingAverage", "rating_average")
movie.set_alias("releaseInitial", "release_date")
movie.set_alias("backdropPath", "backdrop_path")
movie.set_alias("posterPath", "poster_path")
movie.set_alias("tmdbUrl", "tmdb_url")
movie.set_alias("watchStatus", "watch_status")
movie.set_alias("ratingUser", "rating_user")


@query.field("tv")
def resolve_tv(*_, code: int, country: str) -> dict:
    """
    API endpoint for "tv" queries.
    :param code: <int> Id of the tv show to get details for
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :return: <dict> Details of the tv show
    """
    tv = TVDetails()
    return tv.get_tv_details(tmdb, code, country)


tv = ObjectType("TV")

tv.set_alias("ratingAverage", "rating_average")
tv.set_alias("releaseInitial", "first_air_date")
tv.set_alias("releaseFinal", "last_air_date")
tv.set_alias("backdropPath", "backdrop_path")
tv.set_alias("posterPath", "poster_path")
tv.set_alias("numberOfEpisodes", "number_of_episodes")
tv.set_alias("numberOfSeasons", "number_of_seasons")
tv.set_alias("tmdbUrl", "tmdb_url")
tv.set_alias("watchStatus", "watch_status")
tv.set_alias("ratingUser", "rating_user")
tv.set_alias("directors", "creators")


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

season.set_alias("tvCode", "tv_code")
season.set_alias("seasonNumber", "season_number")
season.set_alias("posterPath", "poster_path")
season.set_alias("watchStatus", "watch_status")
season.set_alias("ratingUser", "rating_user")
season.set_alias("numberOfEpisodes", "number_of_episodes")
season.set_alias("airDate", "air_date")


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
    episode = EpisodeDetails()
    return episode.get_episode_details(tmdb, code, seasonNumber, episodeNumber)


episode = ObjectType("Episode")

episode.set_alias("episodeNumber", "episode_number")
episode.set_alias("seasonNumber", "season_number")
episode.set_alias("airDate", "air_date")
episode.set_alias("ratingAverage", "rating_average")
episode.set_alias("stillPath", "still_path")
episode.set_alias("watchStatus", "watch_status")
episode.set_alias("ratingUser", "rating_user")


@query.field("search")
def resolve_search(*_, keyword: str) -> dict:
    """
    API endpoint for "search" queries.
    :param keyword: <str> search string
    :return: <dict> Results of the search
    """
    search = SearchDetails()
    return search.get_search_details(tmdb, keyword)


search = UnionType("Media")


@query.field("popular")
def resolve_popular(*_, type: str, country: str) -> dict:
    """
    API endpoint for "popular" queries.
    :param type: <str> choose between "tv" or "movie" to get popular results
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :return: <dict> Details of the movie/tv
    """
    popular = PopularDetails()

    return popular.get_popular_details(tmdb, type, country)


director = ObjectType("Director")

director.set_alias("imagePath", "image_path")

cast = ObjectType("Cast")

cast.set_alias("imagePath", "image_path")

searchResult = UnionType("Media")
type_defs = load_schema_from_path("consumatio/external/api.schema")
schema = make_executable_schema(type_defs, query, movie, tv, season, episode,
                                search, director, cast)


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

    if (BACKEND_SECRET == None):
        raise UndefinedEnvironmentVariable(
            "Please specify a valid backend secret for BACKEND_SECRET environment variable"
        )

    if request.headers.get(CONSUMATIO_SECRET_HEADER_KEY) != BACKEND_SECRET:
        status_code = 401

        return "unauthorized", status_code

    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code


port = int(os.environ['PORT'])

if __name__ == "__main__":
    migrate.init_app(app, db)
    app.run(debug=True, port=port, host="0.0.0.0")