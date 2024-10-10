import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variables
database_url = os.getenv("DATABASE_URL")

try:
    # Parse the DATABASE_URL and establish a connection
    conn = psycopg2.connect(database_url)
    print("Connected to the database successfully!")
    
    # Close the connection
    conn.close()

except Exception as e:
    print(f"Failed to connect to the database: {e}")
