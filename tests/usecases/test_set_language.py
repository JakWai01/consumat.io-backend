from consumatio.external.db.models import *
from consumatio.usecases.set_language import set_language
from tests.utils.setup_app import setup_app


def test_set_language():
    tmdb, database, db = setup_app()

    user = "83f4a921d36@83f4a921d36.com"

    set_language(database, user, "de-DE")

    query = User.query.filter_by(external_id_content=user).first()

    assert "de-DE" == query.language

    User.query.filter(
        User.external_id_content == user).delete()

    db.session.commit()