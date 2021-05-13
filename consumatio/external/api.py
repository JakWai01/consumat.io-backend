from ariadne import ObjectType, QueryType, gql, make_executable_schema, graphql_sync, load_schema_from_path, UnionType, MutationType
from flask.signals import Namespace
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.movie_details import *
from consumatio.usecases.tv_details import *
from consumatio.usecases.season_details import *
from consumatio.usecases.episode_details import *
from consumatio.usecases.search_details import *
from consumatio.usecases.popular_details import *
from consumatio.usecases.list import *
from consumatio.external.db import Database
from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne.constants import PLAYGROUND_HTML
from consumatio.external.exceptions.undefined_environment_variable import UndefinedEnvironmentVariable
from consumatio.external.models import *
import os
from flask import request
from flask import Flask
from flask_migrate import Migrate

DATABASE_URI = os.getenv('DATABASE_URI')
from consumatio.external.logger import get_logger_instance

logger = get_logger_instance()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
CORS(app)

db.init_app(app)

query = QueryType()
mutation = MutationType()

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
    logger.info("Movie was queried -> code:{}, country:'{}'".format(
        code, country))
    movie = MovieDetails()
    user = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return movie.get_movie_details(user, tmdb, code, country)


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
    logger.info("TV was queried -> code:{}, country:'{}'".format(
        code, country))
    tv = TVDetails()
    user = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return tv.get_tv_details(user, tmdb, code, country)


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
    logger.info("Season was queried -> code:{}, season_number:{}".format(
        code, seasonNumber))

    season = SeasonDetails()
    user = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return season.get_season_details(user, tmdb, code, seasonNumber)


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
    logger.info(
        "Episode was queried -> code:{}, season_number:{}, episode_number:{}".
        format(code, seasonNumber, episodeNumber))

    episode = EpisodeDetails()
    user = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return episode.get_episode_details(user, tmdb, code, seasonNumber,
                                       episodeNumber)


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
    :param keyword: <str> Search string
    :return: <dict> Results of the search
    """
    logger.info("Search was queried -> keyword:'{}'".format(keyword))

    search = SearchDetails()
    return search.get_search_details(tmdb, keyword)


search = UnionType("Media")


@query.field("popular")
def resolve_popular(*_, type: str, country: str) -> dict:
    """
    API endpoint for "popular" queries.
    :param type: <str> Choose between "tv" or "movie" to get popular results
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :return: <dict> Details of the movie/tv
    """
    logger.info("Popular was queried -> type:'{}', country:'{}'".format(
        type, country))

    popular = PopularDetails()

    return popular.get_popular_details(tmdb, type, country)


@query.field("list")
def resolve_list(*_, type: str, watchStatus: str) -> dict:
    """
    API endpoint for "list" queries.
    :param type: <str> Choose between "tv", "movie", "season" and "episode"
    :param watchStatus: <str> Choose between "Plan to watch", "Watching", "Dropped" and "Finished"
    :return: <dict> Movie, TV, Season or Episode
    """
    logger.info("List was queried -> type:'{}', watchStatus:'{}'".format(
        type, watchStatus))

    watch_list = List()
    user = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)

    return watch_list.get_list(tmdb, database, user, type, watchStatus)


director = ObjectType("Director")

director.set_alias("imagePath", "image_path")

cast = ObjectType("Cast")

cast.set_alias("imagePath", "image_path")

searchResult = UnionType("Media")

database = Database(db)


@mutation.field("rating")
def resolve_rating(*_, code: int, media: str, rating: float) -> dict:
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    if not database.media_data_exists(user_id, media, code):
        database.media_Data(user_id, media, code)

    database.rating(user_id, media, code, rating)
    return {"status": True}


rating = MutationType()
rating.set_field("rating", resolve_rating)


@mutation.field("watchStatus")
def resolve_watch_status(*_, code: int, media: str, watchStatus: str) -> dict:
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    if not database.media_data_exists(user_id, media, code):
        database.media_Data(user_id, media, code)

    database.watch_status(user_id, media, code, watchStatus)
    return {"status": True}


watchStatus = MutationType()
watchStatus.set_field("watchStatus", resolve_watch_status)

type_defs = load_schema_from_path(
    os.path.join(os.path.dirname(__file__), "api.graphql"))
schema = make_executable_schema(type_defs, query, mutation, rating,
                                watchStatus, movie, tv, season, episode,
                                search, director, cast)


@app.route("/", methods=["GET"])
def graphql_playground() -> str:
    """
    If get request was made on "/", route to playground.
    :return: <str>, <statuscode> Return playground html with status code 200
    """
    # log.DEBUG("Routed to playground -> code:{}".format(200))
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

api = app
