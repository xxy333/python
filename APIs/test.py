from pymongo import MongoClient
from flask import Flask, request, jsonify


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']


@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json
    collection = db['mycollection']
    result = collection.insert_one(data)
    return jsonify({'message' : 'Data uložena', 'id': str(result.inserted_id)}, 201)

if __name__ == '__main__':
    app.run(debug=True)