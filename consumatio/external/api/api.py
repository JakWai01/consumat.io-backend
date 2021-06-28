import os
from ariadne import (MutationType, ObjectType, QueryType, UnionType,
                     load_schema_from_path, make_executable_schema)
from consumatio.constants import CONSUMATIO_NAMESPACE_HEADER_KEY
from consumatio.external.logger import get_logger_instance
from consumatio.usecases.get_episode import *
from consumatio.usecases.get_list import *
from consumatio.usecases.get_movie import *
from consumatio.usecases.get_popular import *
from consumatio.usecases.get_search import *
from consumatio.usecases.get_season import *
from consumatio.usecases.get_season_episodes import *
from consumatio.usecases.get_tv import *
from consumatio.usecases.get_tv_seasons import *
from consumatio.usecases.get_watch_count import *
from consumatio.usecases.get_watch_time import *
from consumatio.usecases.set_favorite import *
from consumatio.usecases.set_number_of_watched_episodes import *
from consumatio.usecases.set_rating import *
from consumatio.usecases.get_by_rating import *
from consumatio.usecases.get_discover import *
from consumatio.usecases.set_watch_status import *
from consumatio.usecases.set_country import *
from consumatio.usecases.set_language import *
from consumatio.usecases.get_user_i18n import *
from flask import request
from consumatio.external.db.models import db


def register_query_resolvers(query, tmdb):
    @query.field("movie")
    def resolve_movie(*_, code: int) -> dict:
        """
        API endpoint for "movie" queries.
        :param code: <int> Id of the movie to get details for
        :return: <dict> Details of the movie
        """
        logger = get_logger_instance()
        logger.info("Movie was queried -> code:{}".format(code))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_movie(external_id, tmdb, code, db)

    @query.field("tv")
    def resolve_tv(*_, code: int) -> dict:
        """
        API endpoint for "tv" queries.
        :param code: <int> Id of the tv show to get details for
        :return: <dict> Details of the tv show
        """
        logger = get_logger_instance()
        logger.info("TV was queried -> code:{}".format(code))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_tv(external_id, tmdb, code, db)

    @query.field("season")
    def resolve_season(*_, code: int, seasonNumber: str) -> dict:
        """
        API endpoint for "season" queries.
        :param code: <int> Id of the tv show to get details for
        :param seasonNumber: <int> Number of the season to get details for
        :return: <dict> Details of the season 
        """
        logger = get_logger_instance()
        logger.info("Season was queried -> code:{}, season_number:{}".format(
            code, seasonNumber))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_season(external_id, tmdb, code, seasonNumber, db)

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
        logger = get_logger_instance()
        logger.info(
            "Episode was queried -> code:{}, season_number:{}, episode_number:{}"
            .format(code, seasonNumber, episodeNumber))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_episode(external_id, tmdb, code, seasonNumber,
                           episodeNumber, db)

    @query.field("search")
    def resolve_search(*_, keyword: str, page: int) -> dict:
        """
        API endpoint for "search" queries.
        :param keyword: <str> Search string
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Results of the search
        """
        logger = get_logger_instance()
        logger.info("Search was queried -> keyword:'{}'".format(keyword))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_search(external_id, tmdb, keyword, page, db)

    @query.field("popular")
    def resolve_popular(*_, type: str, page: int) -> dict:
        """
        API endpoint to get "popular" productions.
        :param type: <str> Media type, choose between "TV", "Movie"
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Results of either popular TV shows or movies
        """
        logger = get_logger_instance()
        logger.info("Popular was queried -> type:'{}'".format(type))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_popular(external_id, tmdb, type, page, db)

    @query.field("discover")
    def resolve_discover(*_, type: str, person: int, similarTo: int,
                         page: int) -> dict:
        """
        Get list of recommended media based on user ratings/favorites (popular as fallback)
        :param type: <str> Media type, choose between "TV", "Movie"
        :param person: <int> TMDB code of a person to get media w/ them (e.g. actor or director)
        :param similarTo: <int> TMDB code of a movie/TV show to search similar media
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Recommended media with respect to the user's watchStatus, favorites and ratings
        """
        logger = get_logger_instance()
        logger.info("Discover was queried -> type:'{}'".format(type))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_discover(external_id, tmdb, type, person, similarTo, page,
                            db)

    @query.field("byRating")
    def resolve_by_rating(*_, type: str, tmdbRating: float, minVotes: int,
                          releasedFrom: str, page: int) -> dict:
        """
        API endpoint to filter media based on rating.
        :param type: <str> Media type, choose between "TV", "Movie"
        :param tmdbRating: <float> Filter media with average rating greater than set value
        :param minVotes: <int> Filter results by minimum amount of votes
        :param releasedFrom: <str> Search for media released after specified date (YYYY-MM-DD)
        :param page: <int> Search page (minimum:1 maximum:1000)
        :return: <dict> Results of either TV shows or movies filtered by ratings
        """
        logger = get_logger_instance()
        logger.info("byRating was queried -> type:'{}'".format(type))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_by_rating(external_id, tmdb, type, tmdbRating, minVotes,
                             releasedFrom, page, db)

    @query.field("tvSeasons")
    def resolve_tv_seasons(*_, code: int) -> list:
        """
        API endpoint for "tvSeasons" queries.
        :param code: <int> Code of the TV show to get the seasons for
        :return: <list> List of dicts consisting of seasons
        """
        logger = get_logger_instance()
        logger.info("TVSeasons was queried -> code:'{}'".format(code))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_tv_seasons(external_id, tmdb, code, db)

    @query.field("seasonEpisodes")
    def resolve_season_episodes(*_, code: str, seasonNumber: int) -> dict:
        """
        API endpoint for "seasonEpisodes" queries.
        :param code: <int> Code of the TV show to get the episodes for 
        :param seasonNumber: <int> Number of the season to get the episodes for
        :return: <dict> List of dicts consisting of episodes
        """
        logger = get_logger_instance()
        logger.info(
            "seasonEpisodes was queried -> code:'{}', seasonNumber:'{}'".
            format(code, seasonNumber))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_season_episodes(external_id, tmdb, code, seasonNumber, db)

    @query.field("watchCount")
    def resolve_watch_count(*_, type: str) -> int:
        """
        API endpoint for "watchCount" queries.
        :param type: <str> Media type, choose between "TV", "Movie", "Season" and "Episode"
        :return: <int> Count of watched media of provided type
        """
        logger = get_logger_instance()
        logger.info("watchCount was queired -> type:'{}'".format(type))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_watch_count(tmdb, external_id, type, db)

    @query.field("watchTime")
    def resolve_watch_time(*_, type: str) -> int:
        """
        API endpoint for "watchTime" queries.
        :param type: <str> Media type, choose between "TV", "Movie"
        :return: <int> Runtime of watched media of provided type
        """
        logger = get_logger_instance()
        logger.info("watchTime was queried -> type:'{}'".format((type)))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_watch_time(tmdb, external_id, type, db)

    @query.field("list")
    def resolve_list(*_, type: str, watchStatus: str, favorite: bool) -> dict:
        """
        API endpoint for "list" queries.
        :param type: <str> Media type, choose between "TV", "Movie", "Season" and "Episode"
        :param watchStatus: <str> Choose between "Plan to watch", "Watching", "Dropped" and "Finished" or null
        :param favorite: <bool> Boolean to query media marked as favorite (best used with watchStatus = null)
        :return: <dict> Movie, TV, Season or Episode
        """
        logger = get_logger_instance()
        logger.info("List was queried -> type:'{}', watchStatus:'{}'".format(
            type, watchStatus))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_list(tmdb, external_id, type, watchStatus, favorite, db)

    @query.field("user")
    def resolve_user(*_) -> dict:
        """
        Get user preferences
        :return: <dict> Currently returns user's country & language settings
        """
        logger = get_logger_instance()
        logger.info("user was queried")
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return get_user_i18n(external_id, db)


def register_mutation_resolvers(mutation, tmdb, database):
    @mutation.field("favorite")
    def resolve_favorite(*_, code: int, type: str, favorite: bool,
                         seasonNumber: int, episodeNumber: int) -> dict:
        """
        Mutation endpoint to set meida as favorite.
        :param code: <int> TMDB code of the item to set as favorite 
        :param type: <str> Media type, choose between "TV", "Movie", "Season" and "Episode"
        :param favorite: <bool> Boolean to set favorite to
        :param seasonNumber: <int> Number of season if type is season else set to null
        :param episodeNumber: <int> Number of episode if type is episode else set to null
        :return: <dict> Dict containing status of mutation
        """
        logger = get_logger_instance()
        logger.info(
            "favorite was queried -> type:'{}', code:'{}', seasonNumber:'{}', episodeNumber:'{}', favorite:'{}'"
            .format(type, code, seasonNumber, episodeNumber, favorite))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return set_favorite(tmdb, database, external_id, type, code,
                            seasonNumber, episodeNumber, favorite)

    @mutation.field("rating")
    def resolve_rating(*_, code: int, type: str, rating: int) -> dict:
        """
        Mutation endpoint to rate media.
        :param code: <int> TMDB code of the item
        :param type: <str> Media type, choose between "TV", "Movie"
        :param rating: <int> Rating of media to store for user.
        :return: <dict> Dict containing status of mutation
        """
        logger = get_logger_instance()
        logger.info(
            "rating was queried -> type:'{}', code:'{}', rating:'{}'".format(
                type, code, rating))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return set_rating(database, external_id, type, code, rating)

    @mutation.field("numberOfWatchedEpisodes")
    def resolve_number_of_watched_episodes(
            *_, code: int, seasonNumber: int,
            numberOfWatchedEpisodes: int) -> dict:
        """
        Mutation endpoint to set amount of watched episodes
        :param code: <int> TMDB code of the item
        :param seasonNumber: <int> Number of season the episodes are part of
        :param numberOfWatchedEpisodes: <int> Amount of watched episodes
        :return: <dict> Dict containing status of mutation
        """
        logger = get_logger_instance()
        logger.info(
            "number of watched episodes was queried -> code:'{}', seasonNumber:'{}', numberOfWatchedEpisodes:'{}'"
            .format(code, seasonNumber, numberOfWatchedEpisodes))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return set_number_of_watched_episodes(tmdb, database, external_id,
                                              code, seasonNumber,
                                              numberOfWatchedEpisodes)

    @mutation.field("watchStatus")
    def resolve_watch_status(*_, code: int, type: str,
                             watchStatus: str) -> dict:
        """
        Mutation endpoint to set the watchStatus of a TV show or movie
        :param code: <int> TMDB code of the item to change the watchStatus for
        :param type: <str> Media type, choose between "TV", "Movie", "Season" and "Episode"
        :param watchStatus: <str> Choose between "Plan to watch", "Watching", "Dropped" and "Finished"
        :return: <dict> Dict containing status of mutation
        """
        logger = get_logger_instance()
        logger.info(
            "watchStatus was queried -> code:'{}', type:'{}', watchStatus:'{}'"
            .format(code, type, watchStatus))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return set_watch_status(database, external_id, code, type, watchStatus)

    @mutation.field("country")
    def resolve_country(*_, country: str) -> dict:
        """
        Mutation endpoint to set the current user's preferred country
        :param country: <str> ISO 3166-1 alpha-2 country code (e.g. 'DE' or 'US')
        :return: <dict> Dict containing status of mutation
        """
        logger = get_logger_instance()
        logger.info("country was queried -> country:'{}'".format(country))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return set_country(database, external_id, country)

    @mutation.field("language")
    def resolve_language(*_, language: str) -> dict:
        """
        Mutation endpoint to set the current user's preferred language
        :param language: <str> RFC 5646 BCP language tag (e.g. 'de-DE' or 'en-US')
        :return: <dict> Dict containing status of mutation
        """
        logger = get_logger_instance()
        logger.info("language was queried -> language:'{}'".format(language))
        external_id = request.headers.get(CONSUMATIO_NAMESPACE_HEADER_KEY)
        return set_language(database, external_id, language)

    return resolve_favorite, resolve_rating, resolve_number_of_watched_episodes, resolve_watch_status, resolve_country, resolve_language


def get_schema(tmdb, database):
    # Setup queries
    query = QueryType()
    register_query_resolvers(query, tmdb)

    # Setup mutations
    mutation = MutationType()
    resolve_favorite, resolve_rating, resolve_number_of_watched_episodes, resolve_watch_status, resolve_country, resolve_language = register_mutation_resolvers(
        mutation, tmdb, database)

    # Register aliases for mutations
    favorite = MutationType()
    favorite.set_field("favorite", resolve_favorite)

    rating = MutationType()
    rating.set_field("rating", resolve_rating)

    number_of_watched_episodes = MutationType()
    # TODO: Alias
    number_of_watched_episodes.set_field("numberOfWatchedEpisodes",
                                         resolve_number_of_watched_episodes)

    watch_status = MutationType()
    # TODO: Alias
    watch_status.set_field("watchStatus", resolve_watch_status)

    country = MutationType()
    country.set_field("country", resolve_country)

    language = MutationType()
    language.set_field("language", resolve_language)

    # Register aliases for objects
    movie = ObjectType("Movie")
    movie.set_alias("ratingAverage", "rating_average")
    movie.set_alias("ratingCount", "rating_count")
    movie.set_alias("releaseInitial", "release_date")
    movie.set_alias("backdropPath", "backdrop_path")
    movie.set_alias("posterPath", "poster_path")
    movie.set_alias("tmdbUrl", "tmdb_url")
    movie.set_alias("watchStatus", "watch_status")
    movie.set_alias("ratingUser", "rating_user")

    tv = ObjectType("TV")
    tv.set_alias("ratingAverage", "rating_average")
    tv.set_alias("ratingCount", "rating_count")
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

    # Read the GraphQL schema
    type_defs = load_schema_from_path(
        os.path.join(os.path.dirname(__file__), "api.graphql"))

    # Connect the schema to the resolvers
    return make_executable_schema(type_defs, query, mutation, rating,
                                  watch_status, movie, tv, season, episode,
                                  media_page, director, cast,
                                  number_of_watched_episodes, favorite)
