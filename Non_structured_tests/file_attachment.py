from time import sleep
import os
from selenium import webdriver
from socket import gethostname

#from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

if "console" in gethostname():
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://shop.one-shore.com/index.php")
driver.find_element_by_css_selector("div[id='contact-link'] a").click()
file_path = os.path.abspath("1.jpg")
attachment_locator = ".contact-form input[type=file]"
attachment_field = driver.find_element_by_css_selector(attachment_locator)
attachment_field.send_keys(file_path)



#sleep(2)
driver.quit()