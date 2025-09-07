import json
import time
import pytest
from selenium.webdriver.common.by import By
from PageObject_version.utils.Logger import get_logger
from PageObject_version.page_objects.LoginPage import LoginPage

logger = get_logger("Fail Tests")

with open("PageObject_version/test_data.json") as f:
    test_data = json.load(f)
    data_Fail = test_data["fail_data"]


@pytest.mark.smoke
@pytest.mark.parametrize("item", data_Fail)
def test_login_failure(setup, item):
    # Getting the driver from the setup function
    driver = setup

    # Navigating to the login page
    logger.info("Navigating to the Login Page")
    driver.get(item["login_URL"])

    # Creating a LoginPage object with the driver
    login_page = LoginPage(driver)

    # Using the login method of the LoginPage object
    login_page.login(item["username"], item["password"], item["dd_option"])

    # Waiting for 2 seconds
    time.sleep(2)

    # Taking a screenshot of the failure
    logger.info("taking screenshot for failure")
    driver.get_screenshot_as_file(r"screenshots\failure.png")

    # Validating the error message
    logger.info("Validating the Error message")
    alert_text = driver.find_element(By.CSS_SELECTOR, "div[class ='alert alert-danger col-md-12']").text

    # Asserting that the error message is in the alert text
    assert item["Error_message"] in alert_text  # deliberately Failing the Test case
