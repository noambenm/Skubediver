# dive-log-service/main.py
import os
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read database configuration from environment
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT', 3306),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_NAME')
}

# Connect to MySQL and ensure the dive_logs table exists
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS dive_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    location VARCHAR(255),
    depth FLOAT,
    duration INT,
    notes TEXT
)
""")
conn.commit()

@app.route("/logs", methods=["GET"])
def list_logs():
    cursor.execute("SELECT id, user_id, location, depth, duration, notes FROM dive_logs")
    rows = cursor.fetchall()
    logs = []
    for (id, user_id, location, depth, duration, notes) in rows:
        logs.append({
            "id": id,
            "user_id": user_id,
            "location": location,
            "depth": depth,
            "duration": duration,
            "notes": notes
        })
    return jsonify(logs)

@app.route("/logs", methods=["POST"])
def create_log():
    data = request.get_json()
    # In a real app, validate data and handle missing fields, etc.
    cursor.execute(
        "INSERT INTO dive_logs (user_id, location, depth, duration, notes) VALUES (%s, %s, %s, %s, %s)",
        (data.get('user_id'), data['location'], data['depth'], data['duration'], data.get('notes', ''))
    )
    conn.commit()
    return jsonify({"status": "ok", "inserted_id": cursor.lastrowid}), 201

if __name__ == "__main__":
    # Use 0.0.0.0 to allow access in container, and port from env or default 5001
    port = int(os.getenv('PORT', 5001))
    app.run(host="0.0.0.0", port=port)
