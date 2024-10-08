# main.py
import data_handler

def main():
    print("Starting CryptoBot...")
    data = data_handler.fetch_data()
    print("Data fetched:", data)

if __name__ == '__main__':
    main()
