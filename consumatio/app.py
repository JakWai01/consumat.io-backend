import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, upgrade

from consumatio.external.api.api import get_schema
from consumatio.external.db.db import Database
from consumatio.external.logger import get_logger_instance
from consumatio.external.db.models import *
from consumatio.external.api.routes import register_routes
from consumatio.external.tmdb.tmdb import Tmdb


class App:
    def __init__(self, tmdb_key, backend_secret, database_uri, port, debug):
        self.tmdb_key = tmdb_key
        self.backend_secret = backend_secret
        self.database_uri = database_uri
        self.port = port
        self.debug = debug

    def configure(self):
        # Create the app
        app = Flask(__name__)

        # Disable CORS
        CORS(app)

        # Setup the TMDB API client
        tmdb = Tmdb(self.tmdb_key, db)

        # Set up the database
        database = Database(db)
        app.config['SQLALCHEMY_DATABASE_URI'] = self.database_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

        # Get the executable schema
        schema = get_schema(tmdb, database)

        # Setup migrations
        migrate = Migrate(app, db)
        db.init_app(app)
        migrate.init_app(app, db)

        # Run migrations
        with app.app_context():
            upgrade(directory=os.path.join(os.path.dirname(__file__), "..",
                                           "migrations"))

        # Register the routes
        register_routes(app, schema, self.backend_secret)

        # Expose the Flask app
        self.app = app

    def run(self):
        # Start the app
        self.app.run(debug=self.debug, port=self.port, host="0.0.0.0")
