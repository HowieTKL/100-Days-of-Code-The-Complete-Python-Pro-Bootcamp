import os
import requests
import datetime as dt

PIXELA_USERS_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": os.environ["PIXELA_TOKEN"],
    "username": "elari",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_USERS_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.json())

headers = {
    "X-USER-TOKEN": os.environ["PIXELA_TOKEN"]
}
# parameters = {
#     "id": "shower0",
#     "name": "shower",
#     "unit": "count",
#     "type": "int",
#     "color": "sora"
# }
# response = requests.post(url="https://pixe.la/v1/users/elari/graphs", json=parameters, headers=headers)
# response.raise_for_status()
# print(response)

# new pixel
# today = dt.datetime.now().strftime("%Y%m%d")
# print(today)
# parameters = {
#     "date": "20260130",
#     "quantity": "1"
# }
# response = requests.post(url="https://pixe.la/v1/users/elari/graphs/shower0", json=parameters, headers=headers)
# response.raise_for_status()
# print(response)

# delete pixel
response = requests.delete(url="https://pixe.la/v1/users/elari/graphs/shower0/20260130", headers=headers)
response.raise_for_status()
print(response)



