from consumatio.external.db.models import *
from consumatio.usecases.get_user_i18n import get_user_i18n
from tests.utils.setup_app import setup_app


def test_get_user_i18n():

    dict = {
        "country": "US",
        "language": "en-US",
    }

    assert dict == get_user_i18n("c44298fc1@c44298fc1.com", db)