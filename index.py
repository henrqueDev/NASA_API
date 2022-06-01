import json
from flask import Flask
import sqlite3
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, Multiverse!</p>"

@app.route("/sateliteISS")
def radarSatelite():
    res =  requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    obj = json.loads(res.text)
    return obj
