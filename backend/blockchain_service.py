import requests
import os
from dotenv import load_dotenv

load_dotenv()

ETH_API_KEY = os.getenv("ETHERSCAN_API_KEY")


def get_wallet_transactions(address):

    url = "https://api.etherscan.io/v2/api"

    params = {
        "chainid": 1,                 # ⭐ REQUIRED for V2
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "offset": 200,
        "page": 1,
        "apikey": ETH_API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    print("ETHERSCAN RESPONSE:", data)

    if data["status"] != "1":
        return []

    return data["result"]
