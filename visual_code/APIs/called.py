import requests
from flask import Flask, request, jsonify, abort


app = Flask("__main__")


@app.route("/v1/recieved-data", methods=["GET"])

def recieved_data():
    try:
        data = request.json
        if not data:
            abort(400, "Data not recieved")

        return jsonify({f"message: {data}"}), 200

    except Exception as e:
        print(f"errror {e}")
        return jsonify({f"error": {str(e)}}), 500


if __name__ == "__main__":
    app.run(debug=True, port= 8081)