# consumat.io Backend

Backend for [github.com/alphahorizonio/consumat.io](https://github.com/alphahorizonio/consumat.io).

[![hydrun CI](https://github.com/alphahorizonio/consumat.io-backend/actions/workflows/hydrun.yaml/badge.svg)](https://github.com/alphahorizonio/consumat.io-backend/actions/workflows/hydrun.yaml)
[![Docker CI](https://github.com/alphahorizonio/consumat.io-backend/actions/workflows/docker.yaml/badge.svg)](https://github.com/alphahorizonio/consumat.io-backend/actions/workflows/docker.yaml)
[![Matrix](https://img.shields.io/matrix/consumatio:matrix.org)](https://matrix.to/#/#consumatio:matrix.org?via=matrix.org)
[![Docker Pulls](https://img.shields.io/docker/pulls/alphahorizonio/consumatio-backend?label=docker%20pulls)](https://hub.docker.com/r/alphahorizonio/consumatio-backend)
[![Binary Downloads](https://img.shields.io/github/downloads/alphahorizonio/consumat.io-backend/total?label=binary%20downloads)](https://github.com/alphahorizonio/consumat.io-backend/releases)

## Overview

🚧 This project is a work-in-progress! More instructions will be added as soon as it is usable. 🚧

## Installation

### Containerized

You can get the Docker container like so:

```shell
$ docker pull alphahorizonio/consumatio-backend
```

### Natively

If you prefer a native installation, static binaries are also available on [GitHub releases](https://github.com/alphahorizonio/consumat.io-backend/releases).

You can install them like so:

```shell
$ curl -L -o /tmp/consumatio-backend https://github.com/alphahorizonio/consumat.io-backend/releases/latest/download/consumatio-backend.linux-$(uname -m)
$ sudo install /tmp/consumatio-backend /usr/local/bin
```

### About the Frontend

The frontend is also available on [alphahorizonio/consumat.io-frontend](https://github.com/alphahorizonio/consumat.io-frontend) if you prefer to self-host. For most users, this shouldn't be necessary though; consumat.io is a progressive web app. By simply visiting the [public deployment](https://consumat-io-frontend.vercel.app/) once, it will be available for offline use whenever you need it:

[<img src="https://github.com/alphahorizonio/webnetesctl/raw/main/img/launch.png" width="240">](https://consumat-io-frontend.vercel.app/)

## Usage

🚧 This project is a work-in-progress! More instructions will be added as soon as it is usable. 🚧

## Contributing

### Starting the Backend

To contribute, please use the [GitHub flow](https://guides.github.com/introduction/flow/) and follow our [Code of Conduct](./CODE_OF_CONDUCT.md).

To build and start a development version of the consumat.io backend locally, run the following:

```shell
# Clone the repo
$ git clone https://github.com/alphahorizonio/consumat.io-backend.git
$ cd consumat.io-backend
# Start the database
$ docker volume create consumatio-postgres
$ docker run --name consumatio-postgres -d -e POSTGRES_USER=consumatio-postgres -e POSTGRES_PASSWORD=consumatio-postgres -e POSTGRES_DB=consumatio-postgres -p 5432:5432 -v consumatio-postgres:/var/lib/postgresql/data postgres
# Install dependencies
$ make depend
# Start the backend
$ DATABASE_URI="postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres" TMDB_KEY="mytmdbkey" BACKEND_SECRET="mysecret" make dev
```

The backend should now be started and the GraphQL playground should be available on [http://localhost:5000/](http://localhost:5000/). Whenever you change a source file, the backend will automatically be re-compiled and restarted.

To authorize in the playground, set the following HTTP headers:

```json
{
  "X-Consumatio-Namespace": "you@example.com",
  "X-Consumatio-Secret": "mysecret"
}
```

### Creating new Migrations

If you want to create and apply a migration, run the following; migrations are also applied ("upgraded") automatically on startup:

```shell
$ MSG="mymigrationdescription" DATABASE_URI="postgresql://consumatio-postgres:consumatio-postgres@localhost:5432/consumatio-postgres" make migrations
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

### Getting Help

Have any questions or need help? Chat with us [on Matrix](https://matrix.to/#/#consumatio:matrix.org?via=matrix.org)!

## License

consumat.io Backend (c) 2021 Jakob Waibel and contributors

SPDX-License-Identifier: AGPL-3.0
