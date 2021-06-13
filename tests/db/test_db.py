from consumatio.external.db.db import *
import datetime
import os
from consumatio.external.db.models import db
from consumatio.app import App


def test_cache():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    query_param = "dummy_query_cache"
    body_param = "dummy_body_cache"

    database.cache(query_param, body_param)

    query = Cache.query.filter_by(
        query_content=query_param).first().body_content

    assert "dummy_body_cache" == query

    Cache.query.filter(Cache.query_content == query_param).delete()
    db.session.commit()


def test_is_cached_doesnt_exist():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    query_param = "dummy_query_is_cached_doesnt_exist"

    return_value = database.is_cached(query_param)

    assert return_value == False


def test_is_cached_too_old():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    query_param = "dummy_query_is_cached_too_old"
    body_param = "dummy_body_is_cached_too_old"

    database.cache(query_param, body_param)

    Cache.query.filter(Cache.query_content ==
                       query_param).first().last_changed = datetime.datetime(
                           2021, 1, 20)
    db.session.commit()

    print(
        Cache.query.filter(
            Cache.query_content == query_param).first().last_changed)

    return_value = database.is_cached(query_param)

    assert return_value == False


def test_is_cached_exists():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    query_param = "dummy_query_is_cached_exists"
    body_param = "dummy_body_is_cached_exists"

    database.cache(query_param, body_param)

    return_value = database.is_cached(query_param)

    assert return_value == True

    Cache.query.filter(Cache.query_content == query_param).delete()
    db.session.commit()


def test_get_from_cache():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    query_param = "dummy_query_is_chached_exists"
    body_param = "dummy_body_is_chached_exists"

    database.cache(query_param, body_param)

    return_value = database.get_from_cache(query_param)

    assert return_value == body_param

    Cache.query.filter(Cache.query_content == query_param).delete()
    db.session.commit()


def test_user():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    user = "dummy_user"

    database.user(user)

    query = User.query.filter_by(
        external_id_content=user).first().external_id_content

    assert "dummy_user" == query

    User.query.filter(User.external_id_content == user).delete()
    db.session.commit()


def test_user_exists():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    user = "dummy_user"

    database.user(user)

    return_value = database.user_exists(user)

    assert True == return_value

    User.query.filter(User.external_id_content == user).delete()
    db.session.commit()


def test_user_exists_not():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    user = "dummy_user"

    return_value = database.user_exists(user)

    assert False == return_value


def test_get_user_id():
    tmdb_key = os.getenv("TMDB_KEY")
    app = App(
        tmdb_key, "mysecret",
        "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
        None, False)
    app.configure()
    database = Database(db)
    app.app.app_context().push()

    user = "dummy_user"
    id = 2147483647

    database.user(user)

    User.query.filter(
        User.external_id_content == user).first().user_id_content = id

    return_value = database.get_user_id(user)

    assert id == return_value

    User.query.filter(User.external_id_content == user).delete()
    db.session.commit()
