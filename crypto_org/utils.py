# crypto_org/utils.py
import requests

def fetch_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return {
        'BTC': data['bitcoin']['usd'],
        'ETH': data['ethereum']['usd'],
    }
