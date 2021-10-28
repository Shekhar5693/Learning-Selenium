from selenium_page import SeleniumPage
from webdriver_helpers import *

class SearchPage(SeleniumPage):
	
	URL = "https://shop.one-shore.com/index.php?controller=search"
	product_description_locator = By.CSS_SELECTOR,".product-description a"

	def __init__(self,driver = webdriver):
		super().__init__(driver, self.URL)

	def ger_header():