import time

from flask import Flask, request, jsonify, abort
import psycopg2
from datetime import datetime


app = Flask(__name__)

# Connect to the PostgreSQL database
db_config = {
    "dbname": "appdb",
    "user": "postgres",
    "password": "5HnJc1XNYIdFUEZBXpJ4",
    "host": "localhost",
    "port": "5432"  # Default PostgreSQL port
}


def get_db_connection():
    return psycopg2.connect(**db_config)


current_id = 0


@app.route("/v1/data-request", methods=["POST"])
def data_request():
    global current_id
    data = request.get_json()
    if not data:
        abort(400, "Empty data!")


    name = data.get("name")
    email = data.get("email")
    created_at = datetime.now()


    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO app_db_scheme.app_db (name, email, created_at) VALUES (%s, %s, %s) RETURNING id",
            (name, email, created_at),
        )
        new_id = cursor.fetchone()[0]
        current_id += 1
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
        abort(500, f"Database error {e}")


    return jsonify({"message": "Data sucesfully recieved",
                    "id": new_id,
                    "created_at": created_at.isoformat()}), 201




if __name__ == "__main__":
    app.run(debug=True, port=8082)