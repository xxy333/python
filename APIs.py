from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
db_server = MongoClient("mongodb://localhost:27017/")
db = db_server["mydatabase"]

@app.route('/send_new_data', methods=['POST'])  # Corrected route syntax
def send_data():
    data = request.json  # Get JSON data from the request
    db_scheme = db["anothercollection"]  # Collection name needs quotes
    data_receive = db_scheme.insert_one(data)  # Insert data into the collection
    return jsonify({"message": "Data successfully sent!", "id": str(data_receive.inserted_id)}), 201  # Corrected JSON response

@app.route('/data_callback', methods=['GET'])  # Corrected route syntax
def return_data():
    return jsonify({"message": "API test sucessfull"})  # JSON response formatting

if __name__ == '__main__':  # Corrected main check
    app.run(host='localhost', port=8080, debug=True)  # Corrected host parameter
