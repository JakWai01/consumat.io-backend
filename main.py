#!/usr/bin/env python3

import click
import os
from consumatio.app import App


@click.command()
@click.option("--tmdb-key", help="API key for the TMDB API", required=True)
@click.option("--backend-secret", help="Secret for the backend", required=True)
@click.option(
    "--database-uri",
    default=
    "postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres",
    help="URI for the database",
    required=True)
@click.option("--port", default=5000, envvar="PORT", help="Port to listen on")
@click.option("--debug",
              default=False,
              envvar="DEBUG",
              help="Enable debug mode")
def consumatio_backend(tmdb_key, backend_secret, database_uri, port, debug):
    """Backend for https://github.com/alphahorizonio/consumat.io."""
    app = App(tmdb_key, backend_secret, database_uri, port, debug)

    app.run()


if __name__ == '__main__':
    consumatio_backend(auto_envvar_prefix="consumatio")