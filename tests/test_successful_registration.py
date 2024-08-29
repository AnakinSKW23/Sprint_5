from src.helpers import generate_user_data
from src.locators import BurgerLocators
from conftest import driver
from src.data import BurgerData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestSuccessfulRegistration():

    def test_successful_registration(self, driver):
        user_name = BurgerData.user_name
        url_login = BurgerData.url_login
        email_data, password_data = generate_user_data()
        driver.find_element(*BurgerLocators.personal_account).click()
        driver.find_element(*BurgerLocators.registration_button).click()
        driver.find_element(*BurgerLocators.registration_name).send_keys(user_name)
        driver.find_element(*BurgerLocators.registration_email).send_keys(email_data)
        driver.find_element(*BurgerLocators.registration_password).send_keys(password_data)
        driver.find_element(*BurgerLocators.registration_text_btn).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        assert driver.current_url == url_login


