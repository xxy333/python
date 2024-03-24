from flask import Flask, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)

db_server = MongoClient("mongodb://localhost:27017/")
db = db_server["mydatabase"]


@app.route("/send_data_database", methods = ["POST"])
def send_data():
    data = request.json
    db_client = db["mynewcollection"]
    data_input = db_client.insert_one(data)
    return jsonify({"message" : "Data succesfully send!", "id" : str(data_input.inserted_id)}, 201)


if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)


