# main.py
import data_handler
from trading_bot import run_bot

def main():
    print("Starting CryptoBot...")
    
    # Fetch data (if this is part of the logic)
    data = data_handler.fetch_data()
    print("Data fetched:", data)
    
    # Run the bot continuously (60s intervals)
    run_bot()

if __name__ == "__main__":
    main()  # Call the main function which includes all necessary logic
