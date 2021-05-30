class App:
    def __init__(self, tmdb_key, backend_secret, database_uri, port, debug):
        self.tmdb_key = tmdb_key
        self.backend_secret = backend_secret
        self.database_uri = database_uri
        self.port = port
        self.debug = debug

    def run(self):
        print(self.tmdb_key, self.backend_secret, self.database_uri, self.port,
              self.debug)
