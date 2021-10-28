import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

# @pytest.fixture

def chrome():
    driver = webdriver.Chrome()
    yield driver
    sleep(3)
    driver.quit()
    
def test_LoginForm(driver):
    url = "https://shop.one-shore.com/index.php"
    driver.get(url)

    heading_locator = By.CSS_SELECTOR, "h1"

    sign_in_locator = By.PARTIAL_LINK_TEXT, "Sign in"
    sign_in = driver.find_element(*sign_in_locator)
    sign_in.click()
    
    heading = driver.find_element(*heading_locator).text
    assert heading == "Log in to your account"
    
    new_account_locator = By.CSS_SELECTOR, ".no-account > a"
    new_account = driver.find_element(*new_account_locator)
    new_account.click()

    heading = driver.find_element(*heading_locator).text
    assert heading == "Create an account"

    mr_locator = By.CSS_SELECTOR, "input[name='id_gender'][value='1']"
    mr = driver.find_element(*mr_locator)
    mr.click()
    titles_locator = By.CSS_SELECTOR, ".radio-inline"
    titles_visible = expected.presence_of_all_elements_located(titles_locator)
    for title in titles_visible:
	    print(title.text)
	    if title.text == "Mr.":
		    title.click()

    first_name_locator = By.CSS_SELECTOR, "input[name='firstname']"
    name = "Chuck"
    first_name = driver.find_element(*first_name_locator)
    first_name.send_keys(name)

    last_name_locator = By.CSS_SELECTOR, "input[name='lastname']"
    last = "Norris"
    last_name = driver.find_element(*last_name_locator)
    last_name.send_keys(last)

    email_locator = By.CSS_SELECTOR, "div[class='col-md-6'] input[name='email']"
    my_email = "abc@def.com"
    email = driver.find_element(*email_locator)
    email.send_keys(my_email)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Password1!")

    checkbox_locator = By.CSS_SELECTOR, ".register-form input[type=checkbox]"
    checkboxes = driver.find_elements(*checkbox_locator)
    required_checkboxes = list(filter(lambda checkbox: checkbox.get_attribute("required"), checkboxes))
    [checkbox.click() for checkbox in required_checkboxes if not checkbox.is_selected()]

    save_button_locator = By.CSS_SELECTOR, ".register-form button[type=submit]"
    save = driver.find_element(*save_button_locator)
    save.click()

    user_check_locator = By.CSS_SELECTOR, "a[title='View my customer account'] span[class='hidden-sm-down']"
    user = driver.find_element(*user_check_locator).text ==  