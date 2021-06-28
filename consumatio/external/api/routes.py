from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from consumatio.constants import CONSUMATIO_SECRET_HEADER_KEY
from consumatio.external.logger import get_logger_instance
from flask import jsonify, request


def register_routes(app, schema, backend_secret):
    @app.route("/", methods=["GET"])
    def graphql_playground() -> str:
        """
        If get request was made on "/", route to the GraphQL playground.
        :return: <str>, <statuscode> Return playground HTML with HTTP status code 200
        """
        logger = get_logger_instance()
        logger.debug("Routed to playground -> code:{}".format(200))

        return PLAYGROUND_HTML, 200

    @app.route("/", methods=["POST"])
    def graphql_server() -> str:
        """
        If post request was made on "/", resolve the queries.
        :return: <str>, <statuscode> Return response to request with HTTP status code (200 or 400)
        """
        data = request.get_json()

        if request.headers.get(CONSUMATIO_SECRET_HEADER_KEY) != backend_secret:
            status_code = 401

            return "unauthorized", status_code

        success, result = graphql_sync(schema,
                                       data,
                                       context_value=request,
                                       debug=app.debug)

        status_code = 200 if success else 400
        return jsonify(result), status_code
