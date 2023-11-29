from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data


def test_login_from_main_page(driver):
    driver.get(data.page_main_url)
    driver.find_element(By.XPATH, data.page_main_button_gradient_button_xpath).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, data.field_email_xpath)))
    driver.find_element(By.XPATH, data.field_email_xpath).send_keys(data.user_email)
    driver.find_element(By.XPATH, data.field_password_xpath).send_keys(data.user_password)
    driver.find_element(By.XPATH, data.page_login_button_xpath).click()
    WebDriverWait(driver, 3) \
        .until(expected_conditions
               .visibility_of_element_located((By.XPATH, data.page_main_name_label_xpath)))
    assert driver.find_element(By.XPATH, data.page_main_button_gradient_button_xpath).text == "Оформить заказ"


def test_login_from_personal_account(driver):
    driver.get(data.page_main_url)
    driver.find_element(By.XPATH, data.page_main_personal_account_tab_xpath).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, data.field_email_xpath)))
    driver.find_element(By.XPATH, data.field_email_xpath).send_keys(data.user_email)
    driver.find_element(By.XPATH, data.field_password_xpath).send_keys(data.user_password)
    driver.find_element(By.XPATH, data.page_login_button_xpath).click()
    WebDriverWait(driver, 3) \
        .until(expected_conditions
               .visibility_of_element_located((By.XPATH, data.page_main_name_label_xpath)))
    assert driver.current_url == data.page_main_url


def test_login_from_registration_page(driver):
    driver.get(data.page_registration_url)
    driver.find_element(By.XPATH, data.page_registration_enter_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, data.field_email_xpath)))
    driver.find_element(By.XPATH, data.field_email_xpath).send_keys(data.user_email)
    driver.find_element(By.XPATH, data.field_password_xpath).send_keys(data.user_password)
    driver.find_element(By.XPATH, data.page_login_button_xpath).click()
    WebDriverWait(driver, 3) \
        .until(expected_conditions
               .visibility_of_element_located((By.XPATH, data.page_main_name_label_xpath)))
    assert driver.find_element(By.XPATH, data.page_main_button_gradient_button_xpath).text == "Оформить заказ"


def test_login_from_forgot_password_page(driver):
    driver.get(data.page_forgot_password_url)
    driver.find_element(By.XPATH, data.page_forgot_password_enter_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, data.field_email_xpath)))
    driver.find_element(By.XPATH, data.field_email_xpath).send_keys(data.user_email)
    driver.find_element(By.XPATH, data.field_password_xpath).send_keys(data.user_password)
    driver.find_element(By.XPATH, data.page_login_button_xpath).click()
    WebDriverWait(driver, 3) \
        .until(expected_conditions
               .visibility_of_element_located((By.XPATH, data.page_main_name_label_xpath)))
    assert driver.find_element(By.XPATH, data.page_main_button_gradient_button_xpath).text == "Оформить заказ"

