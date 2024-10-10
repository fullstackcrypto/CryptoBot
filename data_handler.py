import requests
from config import API_KEY, COINBASE_API_URL

def fetch_data():
    url = f"{COINBASE_API_URL}/v2/prices/spot?currency=USD"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code} {response.text}")
        return None
