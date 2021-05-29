from ariadne import ObjectType, QueryType, make_executable_schema, graphql_sync, load_schema_from_path, UnionType, MutationType
from consumatio.external.tmdb import Tmdb
from consumatio.usecases.set_number_of_watched_episodes import *
from consumatio.usecases.get_movie_details import *
from consumatio.usecases.get_tv_details import *
from consumatio.usecases.get_season_details import *
from consumatio.usecases.get_episode_details import *
from consumatio.usecases.get_search_details import *
from consumatio.usecases.get_popular_details import *
from consumatio.usecases.get_tv_season_details import *
from consumatio.usecases.get_tv_episode_details import *
from consumatio.usecases.get_watch_count import *
from consumatio.usecases.get_list import *
from consumatio.usecases.get_watch_time import *
from consumatio.usecases.set_favorite import *
from consumatio.usecases.set_rating import *
from consumatio.usecases.set_watch_status import *
from consumatio.external.db import Database
from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne.constants import PLAYGROUND_HTML
from consumatio.external.exceptions.undefined_environment_variable import UndefinedEnvironmentVariable
from consumatio.external.models import *
import os
from flask import request
from flask import Flask
from flask_migrate import Migrate, upgrade
from consumatio.external.logger import get_logger_instance

query = QueryType()


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
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_movie_details(external_id, tmdb, code, country)


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
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_tv_details(external_id, tmdb, code, country)


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
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_season_details(external_id, tmdb, code, seasonNumber)


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
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_episode_details(external_id, tmdb, code, seasonNumber,
                               episodeNumber)


@query.field("search")
def resolve_search(*_, keyword: str, page: int) -> dict:
    """
    API endpoint for "search" queries.
    :param keyword: <str> Search string
    :param page: <int> Search page (minimum:1 maximum:1000)
    :return: <dict> Results of the search
    """
    logger.info("Search was queried -> keyword:'{}'".format(keyword))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_search_details(external_id, tmdb, keyword, page)


@query.field("popular")
def resolve_popular(*_, type: str, country: str, page: int) -> dict:
    """
    API endpoint for "popular" queries.
    :param type: <str> Choose between "tv" or "movie" to get popular results
    :param country: <str> Country abbreviation to get corresponding providers (e.g. "DE" -> Germany)
    :param page: <int> Search page (minimum:1 maximum:1000)
    :return: <dict> Details of the movie/tv
    """
    logger.info("Popular was queried -> type:'{}', country:'{}'".format(
        type, country))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_popular_details(external_id, tmdb, type, country, page)


@query.field("tvSeasons")
def resolve_tvSeasons(*_, code: int) -> list:
    """
    API endpoint for "tvSeasons" queries.
    :param code: <int> Code of the TV show to get the seasons for
    :return: list of dicts consisting of seasons
    """
    logger.info("TVSeasons was queried -> code:'{}'".format(code))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_tv_season_details(external_id, tmdb, code)


@query.field("seasonEpisodes")
def resolve_tvEpisodes(*_, code: str, seasonNumber: int) -> dict:
    """
    API endpoint for "seasonEpisodes" queries.
    :param code: <int> Code of the TV show to get the episodes for 
    :param seasonNumber: <int> Number of the season to get the episodes for
    :return: list of dicts consisting of episodes
    """
    logger.info(
        "seasonEpisodes was queried -> code:'{}', seasonNumber:'{}'".format(
            code, seasonNumber))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_tv_episode_details(external_id, tmdb, code, seasonNumber)


@query.field("watchCount")
def resolve_watchCount(*_, type: str) -> int:
    """
    API endpoint for "watchCount" queries.
    :param type: <str> Type to return count for (Movie, TV, genre, Episode)
    :return: <int> Count of watched media of provided type
    """
    logger.info("watchCount was queired -> type:'{}'".format(type))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_watch_count(tmdb, external_id, type)


@query.field("watchTime")
def resolve_watchTime(*_, type: str) -> int:
    """
    API endpoint for "watchTime" queries.
    :param type: <str> Type to return count for (Movie, TV)
    :return: <int> Runtime of watched media of provided type
    """
    logger.info("watchTime was queried -> type:'{}'".format((type)))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_watch_time(tmdb, external_id, type)


@query.field("list")
def resolve_list(*_, type: str, watchStatus: str, favorite: bool) -> dict:
    """
    API endpoint for "list" queries.
    :param type: <str> Choose between "tv", "movie", "season" and "episode"
    :param watchStatus: <str> Choose between "Plan to watch", "Watching", "Dropped" and "Finished" or "any"
    :param favorite: <bool> to query media marked as favorite (best used with watchStatus = "any")
    :return: <dict> Movie, TV, Season or Episode
    """
    logger.info("List was queried -> type:'{}', watchStatus:'{}'".format(
        type, watchStatus))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return get_list(tmdb, external_id, type, watchStatus, favorite)


mutation = MutationType()


@mutation.field("favorite")
def resolve_favorite(*_, code: int, media: str, favorite: bool,
                     seasonNumber: int, episodeNumber: int) -> dict:
    logger.info(
        "favorite was queried -> media:'{}', code:'{}', seasonNumber:'{}', episodeNumber:'{}', favorite:'{}'"
        .format(media, code, seasonNumber, episodeNumber, favorite))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return set_favorite(tmdb, database, external_id, media, code, seasonNumber,
                        episodeNumber, favorite)


@mutation.field("rating")
def resolve_rating(*_, code: int, media: str, rating: int) -> dict:
    logger.info(
        "rating was queried -> media:'{}', code:'{}', rating:'{}'".format(
            media, code, rating))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return set_rating(tmdb, database, external_id, media, code, rating)


@mutation.field("numberOfWatchedEpisodes")
def resolve_number_of_watched_episodes(*_, code: int, seasonNumber: int,
                                       numberOfWatchedEpisodes: int) -> dict:
    logger.info(
        "number of watched episodes was queried -> code:'{}', seasonNumber:'{}', numberOfWatchedEpisodes:'{}'"
        .format(code, seasonNumber, numberOfWatchedEpisodes))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return set_number_of_watched_episodes(tmdb, database, external_id, code,
                                          seasonNumber,
                                          numberOfWatchedEpisodes)


@mutation.field("watchStatus")
def resolve_watch_status(*_, code: int, media: str, watchStatus: str) -> dict:
    logger.info(
        "watchStatus was queried -> code:'{}', media:'{}', watchStatus:'{}'".
        format(code, media, watchStatus))
    external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
    return set_watch_status(database, external_id, code, media, watchStatus)


app = Flask(__name__)
CORS(app)


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


TMDB_KEY_KEY = os.getenv('TMDB_KEY')
if (TMDB_KEY_KEY == None):
    raise UndefinedEnvironmentVariable(
        "Please specify a valid API key for TMDB_KEY environment variable")

BACKEND_SECRET = os.getenv('BACKEND_SECRET')
if (BACKEND_SECRET == None):
    raise UndefinedEnvironmentVariable(
        "Please specify a valid API key for BACKEND_SECRET environment variable"
    )

CONSUMATIO_NAMESPACE_HEADER_KEY = 'X-Consumatio-Namespace'
if (CONSUMATIO_NAMESPACE_HEADER_KEY == None):
    raise UndefinedEnvironmentVariable(
        "Please specify a valid API key for CONSUMATIO_NAMESPACE_HEADER_KEY environment variable"
    )

CONSUMATIO_SECRET_HEADER_KEY = 'X-Consumatio-Secret'
if (CONSUMATIO_SECRET_HEADER_KEY == None):
    raise UndefinedEnvironmentVariable(
        "Please specify a valid API key for CONSUMATIO_SECRET_HEADER_KEY environment variable"
    )

DATABASE_URI = os.getenv('DATABASE_URI')
if (DATABASE_URI == None):
    raise UndefinedEnvironmentVariable(
        "Please sepcify a valid API key for DATABASE_URI environment variable")

PORT = int(os.environ['PORT'])
if (PORT == None):
    raise UndefinedEnvironmentVariable(
        "Please specify a valid API key for PORT environment variable")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
tmdb = Tmdb(TMDB_KEY_KEY, db)
migrate = Migrate(app, db)

logger = get_logger_instance()

db.init_app(app)

favorite = MutationType()
favorite.set_field("favorite", resolve_favorite)

rating = MutationType()
rating.set_field("rating", resolve_rating)

numberOfWatchedEpisodes = MutationType()
numberOfWatchedEpisodes.set_field("numberOfWatchedEpisodes",
                                  resolve_number_of_watched_episodes)

watchStatus = MutationType()
watchStatus.set_field("watchStatus", resolve_watch_status)

movie = ObjectType("Movie")
movie.set_alias("ratingAverage", "rating_average")
movie.set_alias("releaseInitial", "release_date")
movie.set_alias("backdropPath", "backdrop_path")
movie.set_alias("posterPath", "poster_path")
movie.set_alias("tmdbUrl", "tmdb_url")
movie.set_alias("watchStatus", "watch_status")
movie.set_alias("ratingUser", "rating_user")

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

season = ObjectType("Season")
season.set_alias("tvCode", "tv_code")
season.set_alias("seasonNumber", "season_number")
season.set_alias("posterPath", "poster_path")
season.set_alias("numberOfEpisodes", "number_of_episodes")
season.set_alias("airDate", "air_date")
season.set_alias("numberOfWatchedEpisodes", "number_of_watched_episodes")

episode = ObjectType("Episode")
episode.set_alias("episodeNumber", "episode_number")
episode.set_alias("seasonNumber", "season_number")
episode.set_alias("airDate", "air_date")
episode.set_alias("ratingAverage", "rating_average")
episode.set_alias("stillPath", "still_path")

media_page = ObjectType("MediaPage")
media_page.set_alias("totalPages", "total_pages")

director = ObjectType("Director")
director.set_alias("imagePath", "image_path")

cast = ObjectType("Cast")
cast.set_alias("imagePath", "image_path")

searchResult = UnionType("Media")

database = Database(db)

type_defs = load_schema_from_path(
    os.path.join(os.path.dirname(__file__), "api.graphql"))

schema = make_executable_schema(type_defs, query, mutation, rating,
                                watchStatus, movie, tv, season, episode,
                                media_page, director, cast,
                                numberOfWatchedEpisodes, favorite)

# Run migrations
migrate.init_app(app, db)

with app.app_context():
    upgrade(directory=os.path.join(os.path.dirname(__file__), "..", "..",
                                   "migrations"))

api = app

if __name__ == "__main__":
    if os.getenv('DEBUG') != None:
        app.run(debug=True, port=PORT, host="0.0.0.0")
    else:
        app.run(port=PORT, host="0.0.0.0")
