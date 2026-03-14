from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B075CYMYK6?th=1")
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

# driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# link = driver.find_element(By.CSS_SELECTOR, "div.documentation-widget p a")
# print(link.get_attribute("href"))
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

driver.get("https://www.python.org/")
time_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget div ul li a")
events_dict = {}
# for i in range(len(time_tags)):
#     events_dict[i] = {
#         "time": time_tags[i].text,
#         "event" : event_tags[i].text
#     }
events_dict = {i: {"time": time_tags[i].text, "event": event_tags[i].text} for i in range(len(time_tags))}
print(events_dict)






driver.quit()
