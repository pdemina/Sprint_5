from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from .locators import Locators
from .helper_functions import Helper_Functions


class TestConstructorTabsSwitching:
    def test_constructor_tabs_switching(self, driver):
        driver.get(Locators.page_main_url)
        driver.find_element(By.XPATH, Locators.page_main_button_gradient_button_xpath).click()
        Helper_Functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located((By.XPATH, Locators.page_main_name_label_xpath)))
        driver.find_element(By.XPATH, Locators.page_main_constructor_tab_xpath).click()
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located((By.XPATH, Locators.page_main_button_gradient_button_xpath)))
        driver.find_elements(By.XPATH,Locators.page_main_sections_xpath)



        assert driver.current_url == Locators.page_main_url