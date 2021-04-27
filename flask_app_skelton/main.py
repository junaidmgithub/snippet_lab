import argparse

from flask import Flask, Blueprint, jsonify
from flask_cors import CORS


blue_print1 = Blueprint('bp1', __name__, url_prefix='/api/v1/url1')
blue_print2 = Blueprint('bp2', __name__, url_prefix='/api/v1/url2')
blue_print3 = Blueprint('bp3', __name__, url_prefix='/api/v1/url3')


@blue_print1.route('/', methods=("GET",))
def hello_world1():
   return jsonify(data='Hello World 1')

@blue_print2.route('/', methods=("GET",))
def hello_world2():
   return 'Hello World 2'

@blue_print3.route('/', methods=("GET", "POST", "PUT", "DELETE"))
def hello_world3():
   return 'Hello World 3'


if __name__ == '__main__':

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--host", help="Port", default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Port", default="8000")
    parser.add_argument("-s", "--settings", help="Settings file", default="settings.py")
    args = parser.parse_args()

    # Init
    app = Flask(__name__)
    settings = app.config

    # Load config
    settings.from_pyfile(args.settings)

    CORS(app, origins=settings['CORS_ORIGINS'])

    @app.route("/api/ping", methods=("GET",))
    def ping():
        return dict(status="online")

    def get_blueprints():
        return [
            blue_print1,
            blue_print2,
            blue_print3
        ]

    def register_blueprints(blue_prints):
        for bp in blue_prints:
            app.register_blueprint(bp)
    register_blueprints(get_blueprints())

    # Start
    app.run(host=args.host, port=args.port)
