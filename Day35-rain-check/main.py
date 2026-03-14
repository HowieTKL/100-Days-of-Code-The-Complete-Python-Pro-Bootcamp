import os

import requests
from twilio.rest import Client

parameters = {
    "lat": 38.8951,
    "lon": -77.0364,
    "cnt": 4,
    "appid": os.environ['OWM_APPID']
}

# api.openweathermap.org/data/2.5/forecast
# api.openweathermap.org/data/2.5/weather
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_next_12 = weather_data["list"]
print(weather_data)
for i in weather_next_12:
    condition_code = i["weather"][0]["id"]
    print(condition_code, type(condition_code))
    if condition_code < 700:
        account_sid = os.environ['TWILIO_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        # sms
        # message = client.messages.create(
        #     body="Testing | Bring an umbrella!",
        #     from_="+18775607479",
        #     to="+18777804236",
        # )

        # whatsapp
        message = client.messages.create(
          from_='whatsapp:+14155238886',
          body='Testing | Bring an umbrella!',
          to='whatsapp:+17033001497'
        )
        print("Bring an umbrella")
