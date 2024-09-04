from src.locators import BurgerLocators
from conftest import driver
from selenium.webdriver.common.by import By

class TestWrongPassword():

    def test_wrong_password(self, driver):
        driver.find_element(*BurgerLocators.personal_account).click()
        driver.find_element(*BurgerLocators.registration_button).click()
        driver.find_element(*BurgerLocators.registration_password).send_keys("222")
        driver.find_element(*BurgerLocators.registration_text_btn).click()
        assert driver.find_element(*BurgerLocators.wrong_password).text == 'Некорректный пароль'
