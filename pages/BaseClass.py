from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    base_url = "https://artmas.by/"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url is None:
            self.driver.get(f"{self.base_url}")
        else:
            self.driver.get(f"{self.base_url}{self.page_url}")
