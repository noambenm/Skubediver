from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
import time
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
}

def create_dive_log_table():
    """Create dive_logs table with retry mechanism"""
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS dive_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                dive_date DATE NOT NULL,
                dive_time TIME NOT NULL,
                max_depth FLOAT NOT NULL,
                o2_percentage FLOAT NOT NULL
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            cursor.close()
            connection.close()
            logger.info("Table 'dive_logs' checked/created successfully.")
            return True
    except Error as e:
        logger.error(f"Error creating table: {e}")
        return False

def insert_dive_log(dive_date, dive_time, max_depth, o2_percentage):
    """Insert dive log with better error handling"""
    try:
        if not all([dive_date, dive_time, max_depth, o2_percentage]):
            return False, "Missing required fields"
            
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            query = """
                INSERT INTO dive_logs (dive_date, dive_time, max_depth, o2_percentage)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (dive_date, dive_time, max_depth, o2_percentage))
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Success"
    except Error as e:
        logger.error(f"Database Error: {e}")
        return False, f"Database Error: {str(e)}"
    except Exception as e:
        logger.error(f"General Error: {e}")
        return False, f"General Error: {str(e)}"

@app.route('/add_dive_log', methods=['POST'])

def add_dive_log():
    """Handle POST requests with better error handling"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "message": "Failed to add dive log.",
                "error": "No JSON data received"
            }), 400

        dive_date = data.get('dive_date')
        dive_time = data.get('dive_time')
        max_depth = data.get('max_depth')
        o2_percentage = data.get('o2_percentage')

        success, message = insert_dive_log(dive_date, dive_time, max_depth, o2_percentage)
        
        if success:
            return jsonify({"message": "Dive log added successfully!"}), 201
        else:
            return jsonify({
                "message": "Failed to add dive log.",
                "error": message,
                "received_data": {
                    "dive_date": dive_date,
                    "dive_time": dive_time,
                    "max_depth": max_depth,
                    "o2_percentage": o2_percentage
                }
            }), 500
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({
            "message": "Failed to add dive log.",
            "error": str(e),
            "received_data": data if 'data' in locals() else None
        }), 500

def initialize_app() -> bool:
    """Initialize the application with database connection and table creation
    
    Returns:
        bool: True if initialization successful, False otherwise
    """
    try:
        if create_dive_log_table():
            logger.info("Application initialized successfully")
            return True
        
        logger.error("Failed to create table")
        return False
        
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        return False


if __name__ == '__main__':
    # Initialize the app before running
    if initialize_app():
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        logger.error("Failed to initialize application. Exiting...")
        exit(1)