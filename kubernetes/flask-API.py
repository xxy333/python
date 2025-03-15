from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello and welcome to my first DevOps API"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)


