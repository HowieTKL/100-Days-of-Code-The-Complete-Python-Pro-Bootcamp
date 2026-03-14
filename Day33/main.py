import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)

parameters = {
    "lat": "38.892059",
    "lng": "-77.019913",
    "formatted": "0"
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
