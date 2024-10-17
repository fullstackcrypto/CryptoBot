import os
import logging
from coinbase.wallet.client import Client  # Importing the correct Coinbase client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Logging configuration
logging.basicConfig(
    filename=os.getenv("TRADE_LOG_PATH", "./logs/trade.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_jwt():
    # JWT generation logic if required
    return os.getenv("COINBASE_API_KEY")

def initialize_client():
    api_key = os.getenv("COINBASE_API_KEY")
    api_secret = os.getenv("COINBASE_API_SECRET")
    
    if not api_key or not api_secret:
        logging.error("Missing `api_key` or `api_secret`.")
        raise ValueError("API key or secret is missing.")
    
    client = Client(api_key, api_secret)
    return client

if __name__ == "__main__":
    logging.info("Starting CryptoBot...")

    try:
        jwt_token = generate_jwt()
        logging.info(f"JWT generated: {jwt_token}")

        # Initialize Coinbase client
        client = initialize_client()
        logging.info("Coinbase client initialized successfully.")

        # Further bot logic here...
    except Exception as e:
        logging.error(f"An error occurred in main: {e}")
