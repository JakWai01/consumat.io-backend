import pytest
from consumatio.exceptions.invalid_parameter import InvalidParameter
from consumatio.external.db.models import *
from consumatio.usecases.set_watch_status import set_watch_status
from tests.utils.setup_app import setup_app


def test_set_watch_status_movie():
    tmdb, database, db = setup_app()

    set_watch_status(database, "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
                     12, "Movie", "Finished")

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Movie", User.external_id_content ==
        "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
        MediaData.media_id_content == 12).first()

    assert "Finished" == query.watch_status_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(User.external_id_content ==
                      "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com").delete()

    db.session.commit()


def test_set_watch_status_tv():
    tmdb, database, db = setup_app()

    set_watch_status(database, "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
                     1399, "TV", "Finished")

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "TV", User.external_id_content ==
        "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
        MediaData.media_id_content == 1399).first()

    assert "Finished" == query.watch_status_content

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(User.external_id_content ==
                      "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com").delete()

    db.session.commit()


def test_set_watch_status_season():
    tmdb, database, db = setup_app()

    with pytest.raises(InvalidParameter):
        set_watch_status(database,
                         "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com", 12,
                         "Season", "Finished")

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Season", User.external_id_content ==
        "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
        MediaData.media_id_content == 12).first()

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(User.external_id_content ==
                      "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com").delete()

    db.session.commit()


def test_set_watch_status_episode():
    tmdb, database, db = setup_app()

    with pytest.raises(InvalidParameter):
        set_watch_status(database,
                         "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com", 12,
                         "Episode", "Finished")

    query = MediaData.query.join(User).filter(
        User.user_id_content == MediaData.user_id_content_media_data,
        MediaData.media_type_content == "Episode", User.external_id_content ==
        "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com",
        MediaData.media_id_content == 12).first()

    id = query.user_id_content_media_data

    query = MediaData.query.filter(
        MediaData.user_id_content_media_data == id).delete()

    User.query.filter(User.external_id_content ==
                      "b5715dc83f4a921d36c@b5715dc83f4a921d36c.com").delete()

    db.session.commit()
