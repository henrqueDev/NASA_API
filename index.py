import json
from flask import Flask
from flask_cors import CORS
import requests
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return "<p>Hello, Multiverse!</p>"

@app.route("/sateliteISS")
def radarSatelite():
    res =  requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    obj = json.loads(res.text)
    return obj
