# consumat.io-backend

Backend for https://github.com/alphahorizonio/consumat.io.

## Installation

🚧 This project is a work-in-progress! Instructions will be added as soon as it is usable. 🚧

## Contributing

To contribute, please use the [GitHub flow](https://guides.github.com/introduction/flow/).

To build and start a development version locally, run the following:

```shell
$ git clone https://github.com/alphahorizonio/consumat.io-backend.git
$ cd consumat.io-backend
$ docker volume create consumatio-postgres
$ docker run --name consumatio-postgres -d -e POSTGRES_USER=consumatio-postgres -e POSTGRES_PASSWORD=consumatio-postgres -e POSTGRES_DB=consumatio-postgres -p 5432:5432 -v consumatio-postgres:/var/lib/postgresql/data postgres
$ pip install -r requirements.txt
$ export DATABASE_URI=postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres
$ export TMDB_KEY=<YOUR_TMDB_API_KEY>
$ export BACKEND_SECRET="mysecret"
$ export FLASK_APP=./consumatio/external/api.py
$ export PORT=5000
$ flask run
```

The backend's GraphQL Playground should now be available on [http://localhost:5000/](http://localhost:5000/).

If you want to create and apply a migration, run the following:

```shell
$ export DATABASE_URI=postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres
$ flask db stamp head
$ flask db migrate -m "Add mynewtable."
$ flask db upgrade
```

You can also connect using `psql`:

```shell
$ PGPASSWORD=consumatio-postgres psql -h localhost -p 5432 -d consumatio-postgres -U consumatio-postgres
```

To reset the database, run:

```shell
$ docker rm -f consumatio-postgres
$ docker volume rm consumatio-postgres
```

## License

consumat.io-backend (c) 2021 Jakob Waibel and contributors

SPDX-License-Identifier: AGPL-3.0
