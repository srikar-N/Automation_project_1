import os
import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from PageObject_version.utils.Logger import get_logger

logger = get_logger("conftest")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="initiate browser"
    )


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(2)  # implicit wait
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("-private")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(2)  # implicit wait
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument("-inprivate")
        driver = webdriver.Edge(options=options)
        driver.implicitly_wait(2)  # implicit wait
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        logger.info("Taking screenshot for failure")
        # Get the driver from the test's setup fixture
        driver = item.funcargs.get("setup")

        if driver:
            # Get the path to the HTML report from pytest's configuration
            pytest_html = item.config.pluginmanager.getplugin('html')
            report_path = item.config.getoption("htmlpath")
            report_dir = os.path.dirname(report_path)

            os.makedirs(report_dir, exist_ok=True)

            # Save the screenshot in the same directory as the HTML report
            file_name = os.path.join(report_dir, f"{item.name}.png")
            driver.save_screenshot(file_name)

            # Create an HTML link to the saved file using a relative path
            relative_file_path = os.path.basename(file_name)
            html_content = (
                f'<div>'
                f'<a href="{relative_file_path}" target="_blank">'
                f'<img src="{relative_file_path}" alt="screenshot" style="width:300px;height:200px;" />'
                f'</a>'
                f'</div>'
            )

            extra.append(extras.html(html_content))

    report.extras = extra
