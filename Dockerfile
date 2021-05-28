# Build container
FROM debian AS build

# Setup environment
RUN mkdir -p /data
WORKDIR /data

# Build the release
COPY . .
RUN ./Hydrunfile

CMD gunicorn -b :$PORT --chdir ./consumatio/external api:api
