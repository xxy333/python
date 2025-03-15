from flask import Flask, request, jsonify

data_store = []


app = Flask("__name__")


@app.errorhandler(400)
def handle_bad_request(error):
    return jsonify({"error": "request must be JSON"}), 400



@app.route("/v1/data-reciever", methods=["POST"])

def data_recieve():

    data = request.json
    if not data:
       
       return jsonify({"error": "No data to recieved"}), 400
    
    data_store.append(data)
    return jsonify({"message sucesfully send" : data}), 200


@app.route("/v1/get-data", methods=["GET"])

def get_data():
   
   return jsonify({"message" : data_store})
   






if __name__ == "__main__":
    app.run(debug=True)#, host="0.0.0.0")

