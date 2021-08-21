# this is a very basic 'extract/transform/load' script
# the goal is to output selected data into a CSV file

import requests
import csv

# this is where we will extract
def get_coin_data(url):
    coin_data = requests.get(url)
    return coin_data.json()

"""
    sample json response:
    {
    "data": [
        {
            "id": "44425",
            "symbol": "CELO",
            "name": "Celo",
            "nameid": "celo",
            "rank": 101,
            "price_usd": "3.10",
            "percent_change_24h": "-0.49",
            "percent_change_1h": "0.13",
            "percent_change_7d": "-2.03",
            "price_btc": "0.000064",
            "market_cap_usd": "571184401.01",
            "volume24": 10985575.460062979,
            "volume24a": 8807428.230585493,
            "csupply": "184447717.00",
            "tsupply": "1000000000",
            "msupply": "1000000000"
        },
        {
            "id": "48581",
            "symbol": "CRV",
            "name": "Curve DAO Token",
            "nameid": "curve-dao-token",
            "rank": 102,
            "price_usd": "2.22",
            "percent_change_24h": "0.29",
            "percent_change_1h": "1.90",
            "percent_change_7d": "-5.40",
            "price_btc": "0.000046",
            "market_cap_usd": "562497971.18",
            "volume24": 226689020.86659354,
            "volume24a": 191419986.20984644,
            "csupply": "253834039.00",
            "tsupply": "1459000697.8068",
            "msupply": "3303030299"
        },

"""

# transform
def transfer_data(data_payload):
    coin_id = []
    coin_name = []
    price_usd = []
    rank_number = []

    for coin in data_payload["data"]:
        coin_id.append(coin["id"])
        coin_name.append(coin["name"])
        price_usd.append(coin["price_usd"])
        rank_number.append(coin["rank"])

        #Loads data to CSV
        with open('coin-data.csv', 'w', newline='') as f:
            for a, b, c, d in zip(coin_id, coin_name, price_usd, rank_number):
                writer = csv.writer(f)
                writer.writerow([a, b, c, d])


result = get_coin_data('https://api.coinlore.net/api/tickers/?start=100&limit=100')

transfer_data(result)
