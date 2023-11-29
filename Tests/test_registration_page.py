from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data


def test_registration_page(driver):
    driver.get(data.page_login_url)
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]')


    WebDriverWait(driver, 3) \
        .until(expected_conditions
               .visibility_of_element_located((By.LINK_TEXT, "Регистрация")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"


