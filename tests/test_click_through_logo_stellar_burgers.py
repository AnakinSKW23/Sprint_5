from src.locators import BurgerLocators
from conftest import driver
from src.data import BurgerData

class TestClickThroughLogo():

    def test_click_through_logo(self, driver):
        user_email = BurgerData.user_email
        user_password = BurgerData.user_password
        start_page = BurgerData.start_page
        driver.find_element(*BurgerLocators.enter_account).click()
        driver.find_element(*BurgerLocators.registration_email).send_keys(user_email)
        driver.find_element(*BurgerLocators.registration_password).send_keys(user_password)
        driver.find_element(*BurgerLocators.login_button).click()
        driver.find_element(*BurgerLocators.personal_account).click()
        driver.find_element(*BurgerLocators.logo).click()
        assert driver.current_url == start_page
