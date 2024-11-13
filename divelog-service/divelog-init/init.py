import mysql.connector
from mysql.connector import Error
import os
import time
import logging

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

def wait_for_db():
    """Wait for database to be ready"""
    while True:
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                logger.info("Successfully connected to MySQL database")
                connection.close()
                exit(0)
        except Error as e:
            logger.warning(f"Database connection failed: {e}")
            time.sleep(2)

wait_for_db()
