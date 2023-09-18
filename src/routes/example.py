from flask import Response

from src.example import main


def response() -> Response:
    body = str(main())
    return Response(body, status=200, mimetype="application/json")
