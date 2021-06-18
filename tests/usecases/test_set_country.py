from consumatio.external.db.models import *
from consumatio.usecases.set_country import set_country 
from tests.utils.setup_app import setup_app


def test_set_country():
    tmdb, database, db = setup_app()

    user = "83f4a921d36@83f4a921d36.com"

    set_country(database, user, "DE")

    query = User.query.filter_by(external_id_content=user).first()

    assert "DE" == query.country

    User.query.filter(
        User.external_id_content == user).delete()

    db.session.commit()