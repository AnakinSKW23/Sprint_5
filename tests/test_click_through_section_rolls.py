from src.locators import BurgerLocators
from conftest import driver

class TestClickThroughRolls():
    def test_click_through_rolls(self, driver):
        driver.find_element(*BurgerLocators.fillings).click()
        driver.find_element(*BurgerLocators.rolls).click()
        assert driver.find_element(*BurgerLocators.name_rolls).is_displayed()
