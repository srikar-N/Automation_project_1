from selenium.webdriver.common.by import By

from PageObject_version.utils.Logger import get_logger
from PageObject_version.page_objects.BasePage import BasePage
from PageObject_version.page_objects.CheckoutPage import CheckoutPage


class ShopPage(BasePage):
    """
    ShopPage class for the ShopPage of the application.

    This class inherits from BasePage and provides methods for interacting with the ShopPage.
    It extends the BasePage class and provides methods to interact with the elements
    specific to the checkout page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.items = (By.CSS_SELECTOR, "div[class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class ='nav-link btn btn-primary']")

    def add_items(self, target_device_1, target_device_2):
        """Adds items to the cart."""
        self.logger.info("Searching for items to add to the cart")
        items_list = self.driver.find_elements(*self.items)  # locating multiple items

        self.logger.info(f"Adding items to the cart")
        for item in items_list:
            current_item = item.find_element(By.CSS_SELECTOR, "div h4").text  # locator chaining
            if (current_item == target_device_1) or (current_item == target_device_2):
                item.find_element(By.CSS_SELECTOR, " div button").click()

        self.logger.info("clicking on the checkout button")
        self.driver.find_element(*self.checkout_button).click()

        self.logger.info("Proceeding to checkout page")
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
