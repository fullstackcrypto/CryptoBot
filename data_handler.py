import requests
from config import API_KEY, API_SECRET

def fetch_data():
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
