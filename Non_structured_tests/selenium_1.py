from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
print("got title: '{}'".format(driver.title))
driver.quit()