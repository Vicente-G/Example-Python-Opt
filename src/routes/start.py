from flask import Request, Response, jsonify

from src.start import main


def response(req: Request) -> tuple[Response, int]:
    try:
        return jsonify(main(req.files["data"])), 200
    except KeyError as error:
        return jsonify({"error": str(error)}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 500
