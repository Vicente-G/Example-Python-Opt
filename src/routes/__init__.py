from flask import Flask, Response, request

from .start import response as start_response


def router(app: Flask) -> Flask:
    @app.route("/status", methods=["GET"])
    def status() -> tuple[Response, int]:
        return Response(None), 200

    @app.route("/start", methods=["POST"])
    def start() -> tuple[Response, int]:
        return start_response(request)

    return app
