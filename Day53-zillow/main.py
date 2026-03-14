import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "selenium_chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

ul = soup.find(name="ul", class_="List-c11n-8-84-3-photo-cards")
items = ul.find_all("li")
wait = WebDriverWait(driver, 10)

for item in items:
    driver.get("https://forms.gle/A8a7tBSt1jGW8yHp8")
    wait.until(ec.presence_of_element_located(
        (By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")))
    anchor = item.find("a")
    if anchor != None:
        address = anchor.text.strip()
        index = address.find("|")
        if index != -1:
            address = address[index + 2:].strip()
        price = item.find("span", class_="PropertyCardWrapper__StyledPriceLine")
        if price != None:
            price = price.text.strip()
            index = price.find("+")
            if index != -1:
                price = price[:index]
            index = price.find("/")
            if index != -1:
                price = price[:index]

            address_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            address_input.clear()
            address_input.send_keys(address)

            price_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price_input.clear()
            price_input.send_keys(price)

            link_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link_input.clear()
            link_input.send_keys(anchor["href"])

            submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
            submit.click()

            time.sleep(1)

            print(address)
            print(price)
            print(anchor['href'])


# driver.quit()