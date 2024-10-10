# db_test.py

import psycopg2
from config import DATABASE  # Assuming the database connection settings are in config.py

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DATABASE['dbname'],
            user=DATABASE['user'],
            password=DATABASE['password'],
            host=DATABASE['host'],
            port=DATABASE['port']
        )
        print("Connected to the database successfully.")
        return conn
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        return None

# Test connection
if __name__ == "__main__":
    connect_db()
