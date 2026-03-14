import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InternetSpeedTest:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "selenium_chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go_button.click()

        wait = WebDriverWait(self.driver, 60)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".audience-survey-answer")))

        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

        self.driver.quit()


class TweeterBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "selenium_chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Chrome(options=chrome_options)

    def tweet(self, text):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        compose_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        compose_button.click()
        time.sleep(3)
        tweet_compose = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_compose.send_keys(text)

# speed = InternetSpeedTest()
# speed.get_internet_speed()
tweeter = TweeterBot()
# tweeter.tweet(f"{speed.down} {speed.up}")
tweeter.tweet("Hello World!")