from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://0.0.0.0:27017/')  # Připojení k MongoDB serveru
db = client['mydatabase']  # Výběr databáze

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json  # Získání dat z POST požadavku
    collection = db['mycollection']  # Výběr kolekce v databázi
    result = collection.insert_one(data)  # Uložení dat do MongoDB
    return jsonify({'message': 'Data uložena', 'id': str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 

