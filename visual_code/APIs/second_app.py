from flask import Flask, request, jsonify


mock_db = []

app = Flask(__name__)

@app.route("/v1/send-data", methods=["POST"])
def send_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    data_to_save = {
        "id": len(mock_db) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }

    mock_db.append(data_to_save)
    print(mock_db)
    
    return jsonify({"Data sucesfully recieved": mock_db}), 200


if __name__ == "__main__":
    app.run(debug=True, port=8081)