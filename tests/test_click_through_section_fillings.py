from src.locators import BurgerLocators
from conftest import driver

class TestClickThroughFillings():
    def test_click_through_fillings(self, driver):
        driver.find_element(*BurgerLocators.fillings).click()
        assert driver.find_element(*BurgerLocators.name_fillings).is_displayed()