from src.locators import BurgerLocators
from conftest import driver
from src.data import BurgerData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogInToAccount():

    def test_log_in_to_account(self, driver):
        user_email = BurgerData.user_email
        user_password = BurgerData.user_password
        driver.find_element(*BurgerLocators.enter_account).click()
        driver.find_element(*BurgerLocators.registration_email).send_keys(user_email)
        driver.find_element(*BurgerLocators.registration_password).send_keys(user_password)
        driver.find_element(*BurgerLocators.login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(BurgerLocators.place_an_order))
        assert driver.find_element(*BurgerLocators.order_button).is_displayed()
