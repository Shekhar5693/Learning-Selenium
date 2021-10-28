from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

def test_demo_shop(browser):
    browser.get("https://shop.one-shore.com/index.php")
    assert "ONESHORE" in browser.title

