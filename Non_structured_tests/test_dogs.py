# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDogs():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dogs(self):
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(565, 759)
    element = self.driver.find_element(By.LINK_TEXT, "বাংলা")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("dogs")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    assert self.driver.find_element(By.CSS_SELECTOR, ".g:nth-child(1) > div:nth-child(2) .LC20lb").text == "Dog - Wikipedia"
    self.driver.find_element(By.CSS_SELECTOR, ".g:nth-child(1) > div:nth-child(2) .LC20lb").click()
    self.driver.find_element(By.ID, "firstHeading").click()
    assert self.driver.title == "Dog - Wikipedia"
  