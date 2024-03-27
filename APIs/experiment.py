from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["mydatabase"]

@app.route("/POST_SAVE", methods = ['POST'])
def save_data():
    data = request.json
    collection = db["mycollection"]
    result = collection.insert_one(data)
    return jsonify({"message" : "Data uložena", "id" : str(result.inserted_id)}), 201


app.run(host="localhost", port="8000", debug=True)