from model import load_spots
import flask
from flask_cors import CORS, cross_origin

spots = load_spots()
spots.sort(key=lambda x: (x.latitude, x.longitude))
app = flask.Flask(__name__)
CORS(app, resource=r'/*')