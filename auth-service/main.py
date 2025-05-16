# auth-service/main.py
import os
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection (same database as dive-log-service)
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT', 3306),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_NAME')
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100)
)
""")
conn.commit()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    # In a real app, add checks (e.g., username uniqueness, strong password)
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                       (data['username'], data['password']))
        conn.commit()
        return jsonify({"status": "user created"}), 201
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    cursor.execute("SELECT id, password FROM users WHERE username=%s", (data['username'],))
    result = cursor.fetchone()
    if result and result[1] == data['password']:
        # In a real scenario, you'd return a JWT or session token here
        return jsonify({"status": "success", "user_id": result[0]})
    else:
        return jsonify({"status": "failed"}), 401

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5002))
    app.run(host="0.0.0.0", port=port)
