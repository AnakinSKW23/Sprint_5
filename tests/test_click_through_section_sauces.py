from src.locators import BurgerLocators
from conftest import driver

class TestClickThroughSauces():
    def test_click_through_sauces(self, driver):
        driver.find_element(*BurgerLocators.sauces).click()
        assert driver.find_element(*BurgerLocators.name_sauces).is_displayed()
