from flask import Flask, Response

from .example import response as example_response


def router(app: Flask) -> Flask:
    @app.route("/status", methods=["GET"])
    def status() -> Response:
        return Response(None, status=200)

    @app.route("/example", methods=["GET"])
    def example() -> Response:
        return example_response()

    return app
