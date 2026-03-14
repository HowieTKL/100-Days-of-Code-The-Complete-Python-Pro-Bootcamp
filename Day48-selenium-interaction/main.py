from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(articles.text)
# articles.click()
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python language", Keys.ENTER)

# driver.get("https://secure-retreat-92358.herokuapp.com/")
# driver.find_element(By.NAME, "fName").send_keys("Howie")
# driver.find_element(By.NAME, "lName").send_keys("Lee")
# driver.find_element(By.NAME, "email").send_keys("hlee@test.com")
# driver.find_element(By.CSS_SELECTOR, ".btn").click()

driver.get("https://ozh.github.io/cookieclicker/")
sleep(3)
lang = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang.click()

sleep(1)
cookie = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
cookie.click()

sleep(1)
big_cookie = driver.find_element(By.ID, "bigCookie")

five_secs = time() + 5
five_mins = time() + 1 * 60
while True:
    big_cookie.click()

    if time() > five_secs:
        products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
        products.reverse()

        for product in products:
            if "enabled" in product.get_attribute("class"):
                product.click()
                break
        five_secs = time() + 5

    if time() > five_mins:
        cookies_per_second = driver.find_element(By.ID, 'cookiesPerSecond')
        print(cookies_per_second.text)
        break


driver.quit()