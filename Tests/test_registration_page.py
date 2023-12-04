from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from .locators import Locators
from .helper_functions import Helper_Functions
from faker import Faker


class TestRegistration:

    def test_registration_page(self, driver):
        fake = Faker()
        driver.get(Locators.page_login_url)
        driver.find_element(By.XPATH, Locators.page_login_registration_link).click()
        driver.find_element(By.XPATH, Locators.page_registration_register_button).click()
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located((By.XPATH, Locators.page_registration_enter_button)))
        driver.find_element(Locators.page_registration_name_field).send_keys("Fyz")
        driver.find_element(Locators.page_registration_email_field).send_keys(fake.email())
        driver.find_element(Locators.page_registration_email_field).send_keys("123456")
        assert driver.current_url == Locators.page_registration_url




