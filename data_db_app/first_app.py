import requests
from flask import Flask, request, jsonify, abort


app = Flask(__name__)

forward_url = "http://localhost:8082/v1/data-request"

stored_data = []

@app.route("/v1/send-data", methods=["POST"])
def send_data():

    data = request.get_json()
    if not data:
        abort(400, "No data to send")
    data_set = {
        "name": data.get("name"),
        "email": data.get("email")
    }

    stored_data.append(data_set)
    print(stored_data)

    try:
        response = requests.post(forward_url, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        abort(500, f"Forwarding failed {e}")

    return jsonify(response.json(),response.status_code), 201   


if __name__ == "__main__":
    app.run(debug=True, port=8081)