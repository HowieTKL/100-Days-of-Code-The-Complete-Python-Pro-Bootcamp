import os
import requests
import datetime as dt

def create_auth_token():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
    }
    body = {
        "client_id": os.environ["AMA_API_KEY"],
        "client_secret": os.environ["AMA_API_SECRET"],
        "grant_type": "client_credentials",
    }
    response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token",
                             data=body, headers=headers)
    response.raise_for_status()
    access_token = response.json()['access_token']
    return access_token


class FlightSearch:
    def __init__(self):
        self.access_token = create_auth_token()

    def get_flights(self, origin_city_code, destination_city_code):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        today_date = dt.date.today()
        from_time = today_date + dt.timedelta(days=1)
        to_time = today_date + dt.timedelta(days=7)
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        print(f"Flights from {origin_city_code} to {destination_city_code}", data)
        return data

    def get_flights_by_date_range(self, origin_city_code, destination_city_code, max_price):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        today_date = dt.date.today()
        from_time = today_date + dt.timedelta(days=1)
        from_end_time = today_date + dt.timedelta(days=15)
        params = {
            "origin": origin_city_code,
            "destination": destination_city_code,
            "departureDate": f"{from_time.strftime('%Y-%m-%d')},{from_end_time.strftime('%Y-%m-%d')}",
            "duration": 7,
            "nonStop": "true",
            "maxPrice": max_price
        }
        print(params)
        response = requests.get(url="https://test.api.amadeus.com/v1/shopping/flight-dates", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        print(f"Flights from {origin_city_code} to {destination_city_code}", data)
        return data

