from src.locators import BurgerLocators
from conftest import driver
from src.data import BurgerData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogInRegistrationForm():

    def test_log_in_registration_form(self, driver):
        user_email = BurgerData.user_email
        user_password = BurgerData.user_password
        driver.find_element(*BurgerLocators.personal_account).click()
        driver.find_element(*BurgerLocators.registration_button).click()
        driver.find_element(*BurgerLocators.login_button_entrance).click()
        driver.find_element(*BurgerLocators.registration_email).send_keys(user_email)
        driver.find_element(*BurgerLocators.registration_password).send_keys(user_password)
        driver.find_element(*BurgerLocators.login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BurgerLocators.enter))
        assert driver.find_element(*BurgerLocators.order_button).is_displayed()
