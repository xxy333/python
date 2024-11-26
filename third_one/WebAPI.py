from flask import Flask, request, jsonify, abort


app = Flask("__name__")


API_KEY = "123_123_VLAD"

def check_api_key():
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        abort(401)

@app.route("/v1/send-data-api", methods=["POST"])
def data_send():
    check_api_key()

    data = request.json
    return jsonify({"message": data})



if __name__ == "__main__":
    app.run(debug=True, port=8080)




