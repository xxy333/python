import requests
from flask import Flask, request, jsonify, abort


app = Flask("__main__")


forward_url = "http://127.0.0.1:8081/v1/recieved-data"
@app.route("/v1/send-data", methods=["GET"])


def send_data():
    try:
        header = {
            "Content-Type": "application/json"
        }
        response = requests.get(forward_url, headers=header)
        response.raise_for_status
        data = request.json
        modified_data = {
            "original": data,
            "malformed": True
        }
        return jsonify({f"message": modified_data})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    



if __name__ == "__main__":
    app.run(debug=True, port=8008)  