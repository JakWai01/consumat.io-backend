import os

from consumatio.app import App
from consumatio.constants import DEFAULT_DATABASE_URI, TESTING_SECRET_KEY
from consumatio.external.db.db import Database
from consumatio.external.db.models import *
from tests.tmdb.tmdb_mock import TmdbMock


def setup_app():
    # Read config from env
    tmdb_key = os.getenv("TMDB_KEY")
    backend_secret = os.getenv("BACKEND_SECRET")
    database_uri = os.getenv("DATABASE_URI")

    # Set default values
    if backend_secret == None:
        backend_secret = TESTING_SECRET_KEY
    if database_uri == None:
        database_uri = DEFAULT_DATABASE_URI

    # Create app
    app = App(tmdb_key, backend_secret, database_uri, None, True)

    # Start app to drop the database
    app.configure()
    app.app.app_context().push()

    # Drop database
    db.reflect()
    db.drop_all()

    # Start app again for testing
    app.configure()
    app.app.app_context().push()

    # Return any parts of the app to used during testing
    return TmdbMock(tmdb_key, db), Database(db), db
