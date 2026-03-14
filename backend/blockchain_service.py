import requests

ETH_API_KEY = "7GJ6UKXZX45AQ79H8XMA9F2U8EU2G2ICG9"


def get_wallet_transactions(address):

    url = f"https://api.etherscan.io/api"

    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": ETH_API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["status"] != "1":
        return []

    return data["result"]
