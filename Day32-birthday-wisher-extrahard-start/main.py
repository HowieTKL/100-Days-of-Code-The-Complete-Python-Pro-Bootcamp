import random
import smtplib
import os
import datetime as dt
import pandas as pd

letters = os.listdir("letter_templates")

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login("elari.purple@gmail.com", "")

now = dt.datetime.now()
birthdays = pd.read_csv("birthdays.csv")
birthdays_today = birthdays[(birthdays.month == now.month) & (birthdays.day == now.day)]

for index, row in birthdays_today.iterrows():
    letter = random.choice(letters)
    with open(f"letter_templates/{letter}", "r") as f:
        letter_contents = "".join(f.readlines())
        letter_contents = letter_contents.replace("[NAME]", row["name"])
    msg = f"Subject:Happy Birthday!\n\n{letter_contents}"
    connection.sendmail("elari.purple@gmail.com", row["email"], msg)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
