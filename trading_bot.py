i# trading_bot.py

import time
from coinbase.wallet.client import Client
from config import API_KEY, API_SECRET
from db_test import connect_db  # Assuming we have a valid connection function

client = Client(API_KEY, API_SECRET)
conn = connect_db()

def fetch_all_assets():
    """Fetch all assets in your Coinbase account, including those with zero balance."""
    try:
        accounts = client.get_accounts()
        return accounts['data']
    except Exception as e:
        print(f"Error fetching account data: {e}")
        return []

def trading_logic():
    """Core logic for making buy/sell decisions for each cryptocurrency."""
    assets = fetch_all_assets()

    for account in assets:
        currency = account['currency']
        balance = float(account['balance']['amount'])

        # We want to trade even for assets with 0 balance
        if balance > 0 or account['balance']['amount'] == '0.00000000':
            try:
                ticker = client.get_spot_price(currency_pair=f"{currency}-USD")
                price = float(ticker['amount'])
                print(f"{currency}: Current Price = {price} USD, Balance = {balance}")

                # Decision-making logic for buying and selling
                if price < 50000:  # Example Buy condition
                    print(f"Buying {currency} at {price} USD")
                    # Add actual API call for buying here
                    # client.buy(currency, ...)

                elif price > 60000:  # Example Sell condition
                    print(f"Selling {currency} at {price} USD")
                    # Add actual API call for selling here
                    # client.sell(currency, ...)
                
            except Exception as e:
                print(f"Error processing {currency}: {e}")

def run_bot():
    """Run the bot continuously, making trades every 60 seconds."""
    while True:
        print("Executing trading logic...")
        trading_logic()
        time.sleep(60)  # Wait 60 seconds between executions
