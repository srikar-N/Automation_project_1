from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """ Base class for all pages """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def type_text(self, locator, text):
        """Types the given text into the element located by the given locator."""
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        """Gets the text of the element located by the given locator."""
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Checks if the element is visible on the page."""
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_for_url(self, url):
        """Waits until the url matches the given url."""
        return self.wait.until(ec.url_to_be(url))
