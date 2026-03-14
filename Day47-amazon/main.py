import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Accept-Language": "en-US",
}
response = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
price = float(soup.select_one("span.a-price-whole").text + soup.select_one("span.a-price-fraction").text)
print(price)

print(os.getenv("SMTP_SERVER"))
with smtplib.SMTP(os.getenv("SMTP_SERVER"), port=587) as smtp:
    print(smtp.starttls())
    # print(smtp.login(os.getenv("EMAIL"), os.getenv("PASSWORD")))
    # smtp.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=os.getenv("TO_EMAIL"), msg="Subject:test\n\ntesttesttest")
