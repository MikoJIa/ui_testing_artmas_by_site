from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.customer_main_page import CustomerMainPage
from utils.switch_to_telegram import switching_to_desktop_telegram


@pytest.fixture
def driver(request):
    #switching_to_desktop_telegram(Options())
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture
def main_page(driver):
    return CustomerMainPage(driver)