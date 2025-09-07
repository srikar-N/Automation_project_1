from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObject_version.utils.Logger import get_logger
from PageObject_version.page_objects.BasePage import BasePage
from PageObject_version.page_objects.ShopPage import ShopPage


class LoginPage(BasePage):
    """
    Class for handling the login page
    This class is designed to encapsulate all the functionalities related to the login page.
    It extends the BasePage class and provides methods to interact with the elements
    specific to the login page.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.dropdown = (By.CSS_SELECTOR, "select[class='form-control']")
        self.terms = (By.CSS_SELECTOR, "#terms")
        self.signin_button = (By.NAME, "signin")

    def login(self, username, password, dd_option):
        """Performs the login operation."""
        self.logger.info(f"Entering username {username}")
        self.type_text(self.username, username)
        self.logger.info(f"Entering password")
        self.type_text(self.password, password)

        # dropdowns
        self.logger.info(f"Selecting Option from the Dropdown : {dd_option}")
        dd = Select(self.driver.find_element(*self.dropdown))
        dd.select_by_value(dd_option)

        # checkbox
        self.logger.info("clicking on the checkbox")
        self.driver.find_element(*self.terms).click()

        # Taking Ss to confirm the details added
        self.logger.info(f"getting a SS of the filled details")
        self.driver.get_screenshot_as_file("PageObject_version/screenshots/login_details.png")

        self.logger.info("Clicking on the Signin button")
        self.driver.find_element(*self.signin_button).click()

    def validate_sign_in(self, target_url):
        """Validates the sign-in operation."""
        self.logger.info("Validating the Sign in ")
        self.wait_for_url(target_url)
        assert self.driver.current_url == target_url, f"Expected URL: {target_url}, Actual URL: {self.driver.current_url}"

        self.logger.info("Navigating to the Shop Page")
        shop_page = ShopPage(self.driver)
        return shop_page
