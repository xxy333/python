from flask import Flask, request, jsonify


app = Flask("__name__")


@app.route("/v1/api/get-data", methods=["GET"])

def get_api():
    data = "{Message recieved : Completed!}"
    return jsonify(data)


@app.route("/v1/api/post-data", methods=["POST"])

def post_api():
    data = request.get_json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)




