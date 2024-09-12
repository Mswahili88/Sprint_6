import pytest
from selenium import webdriver
from data import URL

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL.FIRST_PAGE)

    yield driver

    driver.quit()