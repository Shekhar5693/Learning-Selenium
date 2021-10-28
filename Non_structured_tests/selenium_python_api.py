from time import sleep
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://shop.one-shore.com")
    print("Driver name: ",driver.name)
    #print(driver.capabilities)
    print("Session ID: ",driver.session_id)
    print("Title: {0}, URL: {1}".format(driver.title,driver.current_url))

finally:
    sleep(3)
    driver.quit()