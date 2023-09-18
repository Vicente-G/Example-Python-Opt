from argparse import ArgumentParser

from flask import Flask

from src.config import PORT
from src.routes import router

parser = ArgumentParser()
parser.add_argument("--debug", default=False, action="store_true")
args, unknown = parser.parse_known_args()

app = Flask(__name__)
app = router(app)

if __name__ == "__main__":
    app.run(debug=args.debug, host="0.0.0.0", port=PORT)
