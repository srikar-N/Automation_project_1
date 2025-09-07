

from selenium.webdriver.common.by import By

from PageObject_version.utils.Logger import get_logger
from PageObject_version.page_objects.BasePage import BasePage


class CheckoutPage(BasePage):
    """
    CheckoutPage class is a page object model for the checkout page.
    It contains the methods and attributes required for the checkout page.
    It extends the BasePage class and provides methods to interact with the elements
    specific to the checkout page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.table_rows = (By.XPATH, "//tbody/tr")
        self.device = (By.XPATH, "//div/h4")
        self.total = (By.XPATH, "//td[@class='text-right']/h3")
        self.checkout = (By.CSS_SELECTOR, "button.btn-success")
        self.country_name = (By.ID, "country")
        self.country = (By.XPATH, "//div[@class='suggestions']")
        self.select_country = (By.LINK_TEXT, "India")
        self.check_box = (By.CSS_SELECTOR, "div.checkbox")
        self.purchase_button = (By.CSS_SELECTOR, "input.btn-success")
        self.alert = (By.CSS_SELECTOR, "div.alert")

    def remove_item(self, target_device):
        """Removes an item from the checkout page."""
        self.logger.info("removing a device from checkout")
        table = self.driver.find_elements(*self.table_rows)
        for row in table:
            if row.find_element(By.XPATH, ".//h4").text == target_device:
                row.find_element(By.CSS_SELECTOR, "button").click()
                break

    def validate_checkout(self, target_device):
        """Validates the checkout page."""
        self.logger.info("Validating checkout")
        device_in_checkout = self.driver.find_element(*self.device).text
        assert target_device == device_in_checkout, f"Expected {target_device} but found {device_in_checkout}"

        self.logger.info("Validating total")
        current_total = int(self.driver.find_element(*self.total).text.replace("₹. ", ""))
        assert current_total > 0, f"The current total should be greater than 0, "

        self.logger.info("clicking on the checkout button")
        self.driver.find_element(*self.checkout).click()

    def delivery_address(self, target_country):
        """Enters the delivery address."""
        self.logger.info("Entering the country")
        # dynamic dropdowns
        self.type_text(self.country_name, target_country)
        self.is_visible(self.country)

        self.logger.info("Selecting the country")
        self.driver.find_element(*self.select_country).click()

    def validate_success(self, message):
        """Validates the success message."""
        self.logger.info("Clicking the checkbox")
        self.driver.find_element(*self.check_box).click()
        self.logger.info("Clicking the purchase button")
        self.driver.find_element(*self.purchase_button).click()

        self.logger.info("Validating the Success message")
        alert_text = self.get_text(self.alert)
        assert message in alert_text, "Checkout is not successful"
