import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "selenium_chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(os.getenv("GYM_URL"))

wait = WebDriverWait(driver, 5)

classes_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0

def retry(func, retries=7, button=None, desc=""):
    try:
        if button is None:
            func()
        else:
            func(button, desc)
    except Exception as e:
        retries -= 1
        if retries > 0:
            print(f"Retrying {func.__name__}... {retries} retries left")
            return retry(func, retries, button, desc)
        else:
            print(f"Failed {func.__name__}")
            raise e

def login():
    wait.until(ec.presence_of_element_located((By.ID, "login-button")))
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input = driver.find_element(By.ID, "email-input")
    email_input.clear()
    email_input.send_keys(os.getenv("ACCOUNT_EMAIL"))

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(os.getenv("ACCOUNT_PASSWORD"))

    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "logout-button")))
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    print("Login successful!")

def booking():
    global classes_booked, waitlists_joined, already_booked_waitlisted
    days = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group-']")
    for day in days:
        date = day.find_element(By.CSS_SELECTOR, "h2")
        cards = day.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
        for card in cards:
            info = card.find_element(By.CSS_SELECTOR, "h3")
            time = card.find_element(By.CSS_SELECTOR, "p[id^='class-time']")
            button = card.find_element(By.CSS_SELECTOR, "button")
            # print("Processing", date.text, time.text)
            if "Tue" in date.text or "Thu" in date.text:
                if "6:00 PM" in time.text:
                    if button.text == "Book Class":
                        retry(book, button=button, desc="Booked")
                        print("Booked!", info.text, date.text, time.text)
                        classes_booked += 1
                    elif button.text == "Booked":
                        print("Already booked!", info.text, date.text, time.text)
                        already_booked_waitlisted += 1
                    elif button.text == "Join Waitlist":
                        retry(book, button=button, desc="Waitlisted")
                        print("Joined waitlist!", info.text, date.text, time.text)
                        waitlists_joined += 1
                    elif button.text == "Waitlisted":
                        print("Already on waitlist!", info.text, date.text, time.text)
                        already_booked_waitlisted += 1
                    break

    print("--- BOOKING SUMMARY ---")
    print(f"Classes Booked: {classes_booked}")
    print(f"Waitlists joined: {waitlists_joined}")
    print(f"Already booked/waitlisted: {already_booked_waitlisted}")
    print(f"Total: {classes_booked + waitlists_joined + already_booked_waitlisted}")

def book(button: WebElement, desc):
    button.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, button.get_attribute("id")), desc))

def verification():
    # Verification
    my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_link.click()
    wait.until(ec.presence_of_element_located((By.ID, "confirmed-bookings-title")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card']")
    print("--- VERIFICATION ---")
    verifications = 0
    for card in cards:
        when = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        if ("Tue" in when.text or "Thu" in when.text) and "6:00 PM" in when.text:
            heading = card.find_element(By.CSS_SELECTOR, "h3")
            print("Verified", heading.text)
            verifications += 1

    if verifications == classes_booked + waitlists_joined + already_booked_waitlisted:
        print("Verification passed!")
    else:
        print(
            f"Verification failed! Expected {verifications} but only got {classes_booked + waitlists_joined + already_booked_waitlisted}")


retry(login)
booking()
retry(verification)

# driver.quit()