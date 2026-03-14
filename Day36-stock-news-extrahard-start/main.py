import datetime as dt
import math
import os
import requests
from twilio.rest import Client

STOCK = "V"
COMPANY_NAME = "Visa Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

today_date = dt.date.today()
previous_workday = today_date - dt.timedelta(days=1)
if previous_workday.weekday() > 4:
    previous_workday = previous_workday - dt.timedelta(days=previous_workday.weekday() - 4)
day_before_previous = previous_workday - dt.timedelta(days=1)
print(previous_workday, day_before_previous)

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": os.environ["AV_API_KEY"],
#     "outputsize": "compact"
# }
# response = requests.get("https://www.alphavantage.co/query", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
# data_list = [value for (key, value) in data['Time Series (Daily)'].items()]
# print(data_list)
# time_series = data['Time Series (Daily)']
# previous_workday_price = float(time_series[previous_workday.strftime("%Y-%m-%d")]['4. close'])
# day_before_previous_workday_price = float(time_series[day_before_previous.strftime("%Y-%m-%d")]['4. close'])
# print(previous_workday_price, day_before_previous_workday_price)
#
# print((previous_workday_price - day_before_previous_workday_price) / previous_workday_price)

parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": os.environ["NEWS_API_KEY"]
}
response = requests.get("https://newsapi.org/v2/everything", params=parameters)
response.raise_for_status()
articles = response.json()["articles"]
three_articles = articles[:3]
print(three_articles)
formatted_articles = [f"{article['title']}\n{article['url']}" for article in three_articles]

# if math.fabs(previous_workday_price - day_before_previous_workday_price) / previous_workday_price > 0.05:
#     print("over 5% change!")

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
# whatsapp
for article in formatted_articles:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=article,
        to='whatsapp:+17033001497'
    )
