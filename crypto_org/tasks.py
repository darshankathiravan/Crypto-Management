from celery import shared_task
import requests
from datetime import datetime
from .models import Organization, CryptoPrice

@shared_task
def update_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        prices = response.json()
        btc_price = prices.get("bitcoin", {}).get("usd")
        eth_price = prices.get("ethereum", {}).get("usd")

        if btc_price and eth_price:
            timestamp = datetime.now()

            for org in Organization.objects.all():
                CryptoPrice.objects.update_or_create(
                    organization=org, symbol="BTC",
                    defaults={"price": btc_price, "timestamp": timestamp}
                )

                CryptoPrice.objects.update_or_create(
                    organization=org, symbol="ETH",
                    defaults={"price": eth_price, "timestamp": timestamp}
                )
    else:
        print("Failed to fetch crypto prices")
