import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestMug():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mug(self):
    self.driver.get("https://shop.one-shore.com/index.php")
    self.driver.set_window_size(710, 759)
    self.driver.find_element(By.NAME, "s").click()
    self.driver.find_element(By.NAME, "s").send_keys("mug")
    self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .product-miniature img").click()
    self.driver.find_element(By.NAME, "textField1").click()
    self.driver.find_element(By.NAME, "textField1").send_keys("I am a mug.")
    self.driver.find_element(By.NAME, "submitCustomizedData").click()
    self.driver.find_element(By.CSS_SELECTOR, ".customization-message > label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".customization-message > label").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".customization-message > label").text == "I am a mug."
  
