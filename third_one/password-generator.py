from flask import Flask, request, jsonify



app = Flask("__name__")

@app.route("/v1/get-api", methods=["GET"])


def get_methods():
    data = "naser si vole"
    return jsonify(data)

@app.route("/v1/api-post", methods = ["POST"])
def post_methods():
    posted_data = request.get_json()
    return (jsonify(posted_data))



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug = True)

