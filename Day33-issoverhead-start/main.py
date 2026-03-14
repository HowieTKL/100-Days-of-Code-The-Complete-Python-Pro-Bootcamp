import smtplib

import requests
import datetime as dt
import math

MY_LAT = 38.892059 # Your latitude
MY_LONG = -77.019913 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    return math.fabs(iss_latitude - MY_LAT) < 5 and math.fabs(iss_longitude - MY_LONG) < 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now(dt.timezone.utc)

def is_dark():
    return time_now.hour >= sunset or time_now.hour <= sunrise


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(is_iss_overhead(), is_dark())
if (is_iss_overhead() and is_dark()):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("elari.purple@gmail.com", "")
    connection.sendmail("elari.purple@gmail.com", "praecognita@gmail.com", msg="Subject:Lookup\n\nISS overhead!")

