from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from .locators import Locators


class Helper_Functions:
    def login_function(email, password, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.field_email_xpath)))
        driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Data.user_email)
        driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Data.user_password)
        driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()

