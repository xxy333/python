from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

db_server = MongoClient("mongodb://localhost:27017/")
db = db_server["mydatabase"]


@app.route(/send_new_data, methods = [POST])
def send_data():
    data = request.json
    db_scheme = db[anothercollection]
    data_recieve = db_scheme.insert_one(data)
    return jsonify({message : Data succesefully send!, id : str(data_recieve.inserted_id)}), 201

@app.route(/data_callback, methods = [GET])
def return_data():
    
    return (Ha, provolal jsi mě!)


if __name__ == __main__:
    app.run(host=localhost, port=8080, debug=True)

