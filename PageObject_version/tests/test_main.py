import json
import pytest

from PageObject_version.utils.Logger import get_logger
from PageObject_version.page_objects.LoginPage import LoginPage

logger = get_logger("test_e2e")

with open("PageObject_version/test_data.json") as f:
    test_data = json.load(f)
    data_list = test_data["data"]


@pytest.mark.parametrize("item", data_list)
def test_e2e(setup, item):
    # Initialize the driver
    driver = setup

    # Navigate to the login page
    logger.info("Navigating to the Login Page")
    driver.get(item["login_URL"])

    # Instantiate the LoginPage object
    login_page = LoginPage(driver)

    # Perform the login operation
    logger.info("Performing the login operation")
    login_page.login(item["username"], item["password"], item["dd_option"])

    # Validate the sign-in operation and get the ShopPage object
    target_url = item["Target_URL"]
    shop_page = login_page.validate_sign_in(target_url)

    # Performing shopping and checkout operations
    # Adding items to the cart
    target_device_1 = item["device1"]
    target_device_2 = item["device2"]
    checkout_page = shop_page.add_items(target_device_1, target_device_2)  # Add items to the cart

    # Proceeding to the checkout page
    # Removing an item from the checkout page
    checkout_page.remove_item(item["remove_device"])  # Remove an item from the checkout page

    # Validating the checkout page
    checkout_page.validate_checkout(target_device_1)  # Validate the checkout page

    # Entering the delivery address
    country = item["country"]
    checkout_page.delivery_address(country)  # Enter the delivery address

    # Validating the success message
    checkout_page.validate_success(item["Success_message"])  # Validate the success message
