import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
DRIVER_PATH='./chromedriver'


@pytest.fixture(scope="function")
def driver():
    #service = Service(executable_path=DRIVER_PATH)
    #options = Options()
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
