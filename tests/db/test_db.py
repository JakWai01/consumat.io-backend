from consumatio.external.db.db import *
import datetime
import pytest
from tests.utils.setup_app import setup_app


def test_cache():
    database = setup_app()[1]

    query_param = "dummy_query_cache"
    body_param = "dummy_body_cache"

    database.cache(query_param, body_param)

    query = Cache.query.filter_by(
        query_content=query_param).first().body_content

    assert query == body_param


def test_is_cached_doesnt_exist():
    database = setup_app()[1]

    query_param = "dummy_query_is_cached_doesnt_exist"

    return_value = database.is_cached(query_param)

    assert return_value is False


def test_is_cached_too_old():
    database = setup_app()[1]

    query_param = "dummy_query_is_cached_too_old"
    body_param = "dummy_body_is_cached_too_old"

    database.cache(query_param, body_param)

    Cache.query.filter(Cache.query_content ==
                       query_param).first().last_changed = datetime.datetime(
                           2021, 1, 20)

    return_value = database.is_cached(query_param)

    assert return_value is False


def test_is_cached_exists():
    database = setup_app()[1]

    query_param = "dummy_query_is_cached_exists"
    body_param = "dummy_body_is_cached_exists"

    database.cache(query_param, body_param)

    return_value = database.is_cached(query_param)

    assert return_value is True


def test_get_from_cache():
    database = setup_app()[1]

    query_param = "dummy_query_is_chached_exists"
    body_param = "dummy_body_is_chached_exists"

    database.cache(query_param, body_param)

    return_value = database.get_from_cache(query_param)

    assert return_value == body_param


def test_user():
    database = setup_app()[1]

    user = "dummy_user"

    database.user(user)

    query = User.query.filter_by(
        external_id_content=user).first().external_id_content

    assert query == user


def test_user_exists():
    database = setup_app()[1]

    user = "dummy_user"

    database.user(user)

    return_value = database.user_exists(user)

    assert return_value is True


def test_user_exists_not():
    database = setup_app()[1]

    user = "dummy_user"

    return_value = database.user_exists(user)

    assert return_value is False


def test_get_user_id():
    database = setup_app()[1]

    user = "dummy_user"

    database.user(user)

    return_value = database.get_user_id(user)

    assert return_value is 1


def test_user_country():
    database = setup_app()[1]

    user = "dummy_user"
    country = "DG"

    database.user(user)
    database.user_country(database.get_user_id(user), country)

    query = User.query.filter_by(external_id_content=user).first().country

    assert query == country


def test_user_language():
    database = setup_app()[1]

    user = "dummy_user"
    language = "de"

    database.user(user)
    database.user_language(database.get_user_id(user), language)

    query = User.query.filter_by(external_id_content=user).first().language

    assert query == language


def test_media_data_exists():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    return_value = database.media_data_exists(database.get_user_id(user),
                                              "Movie", 12)

    assert return_value is True


def test_media_data_exists_not():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    return_value = database.media_data_exists(database.get_user_id(user),
                                              "Movie", 12)

    assert return_value is False


def test_media_data_exists_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    with pytest.raises(InvalidParameter):
        database.media_data_exists(database.get_user_id(user),
                                   "dsfa23sdf234sdf", 12)


def test_media_data():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    return_value = MediaData.query.filter_by(
        user_data_id_content=1).first().user_id_content_media_data

    assert return_value == 1


def test_media_data_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    with pytest.raises(InvalidParameter):
        database.media_data(database.get_user_id(user), "asdf324kjl12h1l", 12,
                            None)


def test_get_media_data_id():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    return_value = database.get_media_data_id(database.get_user_id(user),
                                              "Movie", 12)

    assert return_value == 1


def test_get_media_data_id_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    with pytest.raises(InvalidParameter):
        database.get_media_data_id(database.get_user_id(user),
                                   "sadf23142hk21hk2hjk3k213", 12)


def test_rating_exists():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)
    database.rating(database.get_user_id(user), "Movie", 12, 8)

    return_value = database.rating_exists(database.get_user_id(user), "Movie",
                                          12)

    assert return_value is True


def test_rating_exists_not():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    return_value = database.rating_exists(database.get_user_id(user), "Movie",
                                          12)

    assert return_value is False


def test_rating_exists_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)
    database.rating(database.get_user_id(user), "Movie", 12, 8)

    with pytest.raises(InvalidParameter):
        database.rating_exists(database.get_user_id(user),
                               "21jk231kg34gfh2134", 12)


def test_rating():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    rating = 9

    database.media_data(database.get_user_id(user), "Movie", 12, None)
    database.rating(database.get_user_id(user), "Movie", 12, rating)

    return_value = MediaData.query.filter_by(
        user_data_id_content=1).first().rating_content

    assert return_value == rating


def test_rating_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    rating = 9

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    with pytest.raises(InvalidParameter):
        database.rating(database.get_user_id(user), "2h3k2134h2j4klh4hjk23jh",
                        12, rating)


def test_number_of_watched_episodes():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    number_of_watched_episodes = 9

    database.media_data(database.get_user_id(user), "Season", 3573, 1396)
    database.number_of_watched_episodes(database.get_user_id(user), 3573,
                                        number_of_watched_episodes)

    return_value = MediaData.query.filter_by(
        user_data_id_content=1).first().number_of_watched_episodes

    assert return_value == number_of_watched_episodes


def test_watch_status_exists():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    watch_status = "Planning"

    database.media_data(database.get_user_id(user), "Movie", 12, None)
    database.watch_status(database.get_user_id(user), "Movie", 12,
                          watch_status)

    return_value = database.watch_status_exists(database.get_user_id(user),
                                                "Movie", 12)

    assert return_value is True


def test_watch_status_exists_not():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    return_value = database.watch_status_exists(database.get_user_id(user),
                                                "Movie", 12)

    assert return_value is False


def test_watch_status_exists_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)
    database.media_data(database.get_user_id(user), "Movie", 12, None)

    with pytest.raises(InvalidParameter):
        database.watch_status_exists(database.get_user_id(user),
                                     "asdf2234sdfassdf", 12)


def test_watch_status():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    watch_status = "Planning"

    database.media_data(database.get_user_id(user), "Movie", 12, None)
    database.watch_status(database.get_user_id(user), "Movie", 12,
                          watch_status)

    return_value = MediaData.query.filter_by(
        user_data_id_content=1).first().watch_status_content

    assert return_value == watch_status


def test_watch_status_exception():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    watch_status = "sdakjfhkssafd13425sdaf1"

    database.media_data(database.get_user_id(user), "Movie", 12, None)

    with pytest.raises(InvalidParameter):
        database.watch_status(database.get_user_id(user), "Movie", 12,
                              watch_status)


def test_favorite():
    database = setup_app()[1]

    user = "dummy_user"
    database.user(user)

    database.media_data(database.get_user_id(user), "Movie", 12, None)
    database.favorite(database.get_user_id(user), "Movie", 12, True)

    return_value = MediaData.query.filter_by(
        user_data_id_content=1).first().favorite_content

    assert return_value is True
