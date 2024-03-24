from flask import Flask
import requests 
import jsonify

from pymongo import MongoClient

app = Flask(__name__)

db_server = MongoClient("mongodb://localhost:23707/")
db = db_server["mydatabase"]


app.route("/send_new_data", methods = ["POST"])
def send_data():
    data = json.req



