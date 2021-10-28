from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://shop.one-shore.com/index.php")

articles = driver.find_element_by_tag_name("article")

for article in articles:
    print(article.text)
    action = ActionChains(driver)
