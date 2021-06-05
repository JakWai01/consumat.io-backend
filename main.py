#!/usr/bin/env python3

import os

import click

from consumatio.app import App
from consumatio.exceptions.undefined_environment_variable import \
    UndefinedEnvironmentVariable

DEFAULT_DATABASE_URI = "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres"


@click.command()
@click.option("--tmdb-key",
              envvar="TMDB_KEY",
              help="API key for the TMDB API",
              required=True)
@click.option("--backend-secret",
              envvar="BACKEND_SECRET",
              help="Secret for the backend",
              required=True)
@click.option("--database-uri",
              default=DEFAULT_DATABASE_URI,
              envvar="DATABASE_URI",
              help="URI for the database",
              required=True)
@click.option("--port", default=5000, envvar="PORT", help="Port to listen on")
@click.option("--debug",
              default=False,
              envvar="DEBUG",
              help="Enable debug mode")
def run_consumatio_backend_cli(tmdb_key, backend_secret, database_uri, port,
                               debug):
    """Backend for https://github.com/alphahorizonio/consumat.io."""
    # Configure the app
    app = App(tmdb_key, backend_secret, database_uri, port, debug)

    app.configure()

    print(f"Listening on port {port}")

    # Start the app
    app.run()


if __name__ == '__main__':
    # Running as CLI
    run_consumatio_backend_cli()
else:
    # Running with WSGI, so manually read env variables
    tmdb_key = os.getenv("TMDB_KEY")
    backend_secret = os.getenv("BACKEND_SECRET")
    database_uri = os.getenv("DATABASE_URI")
    port = os.getenv("PORT")
    debug = os.getenv("DEBUG")

    # Check if env variables are set
    if tmdb_key == None:
        raise UndefinedEnvironmentVariable(
            "Please specify the TMDB_KEY env variable")
    if backend_secret == None:
        raise UndefinedEnvironmentVariable(
            "Please specify the BACKEND_SECRET env variable")
    if database_uri == None:
        database_uri = DEFAULT_DATABASE_URI
    if debug == None:
        debug = False

    # Configure the app
    app = App(tmdb_key, backend_secret, database_uri, None, debug)

    app.configure()

    # Expose the Flask app instance to WSGI
    api = app.app
