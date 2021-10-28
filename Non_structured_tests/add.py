# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.set_window_size(778, 759)
search_calc = driver.find_element(By.NAME, "q")
search_calc.click()
search_calc.send_keys("calc")
search_calc.send_keys(Keys.ENTER)

calc = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(2) > .A2W7l > .XRsWPe")
calc.click()

driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .mF5fo > .MEdqYd").click()

calc.click()

driver.find_element(By.CSS_SELECTOR, ".UUhRt").click()

add = driver.find_element(By.CSS_SELECTOR, ".vUGUtc")
result = driver.find_element(By.ID, "cwos")

#print("Result of addition is: ",result.text)
print("Your addition is as follows: {0} {1} ".format(add.text,result.text))
  
driver.quit()