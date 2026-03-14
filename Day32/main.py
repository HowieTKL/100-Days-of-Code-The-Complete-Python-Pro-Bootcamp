import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)

my_email = "elari.purple@gmail.com"
full_msg = f"Subject: Quote\n\n{quote}"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
session = connection.login(user=my_email, password="")
print(session)
connection.sendmail(from_addr=my_email, to_addrs="praecognita@gmail.com", msg=full_msg)
