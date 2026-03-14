import os

import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = get_data()

def get_data():
    # sheety_headers = {
    #     "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
    # }
    #
    # response = requests.get("https://api.sheety.co/c59fbc659e2590d981e5233ebe301d1e/destinations/prices", headers=sheety_headers)
    # response.raise_for_status()
    # print(response.json())
    # return response.json()["prices"]

    return [
        {
          'city': 'Paris',
          'iataCode': 'PAR',
          'lowestPrice': 54,
          'id': 2
        },
        {
          'city': 'Frankfurt',
          'iataCode': 'FRA',
          'lowestPrice': 42,
          'id': 3
        },
        {
          'city': 'Tokyo',
          'iataCode': 'TYO',
          'lowestPrice': 485,
          'id': 4
        },
        {
          'city': 'Hong Kong',
          'iataCode': 'HKG',
          'lowestPrice': 551,
          'id': 5
        },
        {
          'city': 'Istanbul',
          'iataCode': 'IST',
          'lowestPrice': 95,
          'id': 6
        },
        {
          'city': 'Kuala Lumpur',
          'iataCode': 'KUL',
          'lowestPrice': 414,
          'id': 7
        },
        {
          'city': 'New York',
          'iataCode': 'NYC',
          'lowestPrice': 240,
          'id': 8
        },
        {
          'city': 'San Francisco',
          'iataCode': 'SFO',
          'lowestPrice': 260,
          'id': 9
        },
        {
          'city': 'Dublin',
          'iataCode': 'DUB',
          'lowestPrice': 378,
          'id': 10
        }
    ]
