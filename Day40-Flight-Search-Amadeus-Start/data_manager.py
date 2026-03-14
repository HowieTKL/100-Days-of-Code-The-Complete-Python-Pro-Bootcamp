import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT="https://api.sheety.co/c59fbc659e2590d981e5233ebe301d1e/destinations/prices"
SHEETY_USERS_ENDPOINT="https://api.sheety.co/c59fbc659e2590d981e5233ebe301d1e/destinations/users"


class DataManager:

    def __init__(self):
        self._token = os.environ["SHEETY_TOKEN"]
        self.destination_data = {}
        self.emails = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        sheety_headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_headers = {
                "Authorization": f"Bearer {self._token}"
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers
            )
            response.raise_for_status()
            print("Update destination codes", response.text)

    def get_customer_emails(self):
        sheety_headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.emails = data["users"]
        return self.emails

