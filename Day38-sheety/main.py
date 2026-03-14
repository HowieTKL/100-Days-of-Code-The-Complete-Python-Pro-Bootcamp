import os
import requests
import datetime as dt

query = input("Describe your exercise: ")

headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["APP_KEY"]
}
parameters = {
    "query": query
}
response = requests.post(url="https://app.100daysofpython.dev/v1/nutrition/natural/exercise", headers=headers, json=parameters)
response.raise_for_status()
exercises = response.json()["exercises"]
print(exercises)

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

print(date, time)

sheety_headers = {
    "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
}

for ex in exercises:
    print(ex)
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }
    print(sheety_parameters)
    response = requests.post("https://api.sheety.co/c59fbc659e2590d981e5233ebe301d1e/myWorkouts/workouts", headers=sheety_headers, json=sheety_parameters)
    response.raise_for_status()
    print(response.json())
