import json
import time
import urllib.request

API_URL = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'


def fetch_price():
    with urllib.request.urlopen(API_URL) as response:
        data = json.load(response)
        return float(data['bpi']['USD']['rate_float'])


def monitor(interval=60):
    last_price = None
    while True:
        try:
            price = fetch_price()
            if last_price is not None:
                diff = price - last_price
                symbol = '↑' if diff > 0 else '↓' if diff < 0 else '-'
                print(f"BTC price: ${price:.2f} ({symbol}{diff:+.2f})")
            else:
                print(f"BTC price: ${price:.2f}")
            last_price = price
        except Exception as e:
            print(f"Error fetching price: {e}")
        time.sleep(interval)


if __name__ == '__main__':
    monitor()
