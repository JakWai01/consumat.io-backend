import os

import pytest
from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI
from consumatio.exceptions.invalid_parameter import InvalidParameter
from consumatio.external.db.db import Database
from consumatio.external.db.models import *
from consumatio.usecases.set_rating import set_rating
from tests.utils.setup_app import setup_app


def test_set_rating_movie():
    tmdb, database, db = setup_app()

    set_rating(database, "d8007d620@d8007d620.com", "Movie", 12, 10)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Movie",
        User.external_id_content == "d8007d620@d8007d620.com",
        MediaData.media_id_content == 12).first()

    assert 10 == query.rating_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "d8007d620@d8007d620.com").delete()

    db.session.commit()


def test_set_rating_tv():
    tmdb, database, db = setup_app()

    set_rating(database, "d8007d620@d8007d620.com", "TV", 1399, 10)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "TV",
        User.external_id_content == "d8007d620@d8007d620.com",
        MediaData.media_id_content == 1399).first()

    assert 10 == query.rating_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "d8007d620@d8007d620.com").delete()

    db.session.commit()


def test_set_rating_season():
    tmdb, database, db = setup_app()

    with pytest.raises(InvalidParameter):
        set_rating(database, "d8007d620@d8007d620.com", "Season", 1399, 10)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Season",
        User.external_id_content == "d8007d620@d8007d620.com",
        MediaData.media_id_content == 1399).first()

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "d8007d620@d8007d620.com").delete()

    db.session.commit()


def test_set_rating_episode():
    tmdb, database, db = setup_app()

    with pytest.raises(InvalidParameter):
        set_rating(database, "d8007d620@d8007d620.com", "Episode", 1399, 10)

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Episode",
        User.external_id_content == "d8007d620@d8007d620.com",
        MediaData.media_id_content == 1399).first()

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(
        User.external_id_content == "d8007d620@d8007d620.com").delete()

    db.session.commit()
