import os
from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.config import read_config
import logging
from utilities.utility import setup_logger

config = read_config()  # Ensure this function is defined as described above


@pytest.fixture
def browser():
    # Set up the logger
    logger = setup_logger('test')

    # Use ChromeDriverManager to get the correct version of ChromeDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Log the start of the test
    logger.info("Starting a new test with Chrome browser.")

    # Customize browser settings
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait time

    # Yield the driver and logger to the tests
    yield driver, logger

    # Teardown: Quit the browser after the test completes
    logger.info("Test complete. Closing the browser.")
    driver.quit()


@pytest.fixture(scope="session")
def reports_dir():
    # Define the root reports directory
    root_reports_dir = os.path.join(os.getcwd(), 'reports')

    # Get the current date in YYYYMMDD format
    date_today = datetime.now().strftime("%Y%m%d")

    # Create a date-based subfolder under the root reports directory
    date_folder = os.path.join(root_reports_dir, date_today)

    # Ensure the date folder exists
    os.makedirs(date_folder, exist_ok=True)

    # Yield the date folder path to the tests
    yield date_folder


def pytest_configure(config):
    # Automatically get the reports directory from the `reports_dir` fixture
    reports_dir = os.path.join(os.getcwd(), 'reports', datetime.now().strftime('%Y%m%d'))

    # Define paths for the HTML and JUnit XML reports
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_report_path = os.path.join(reports_dir, f"report_{timestamp}.html")
    xml_report_path = os.path.join(reports_dir, f"report_{timestamp}.xml")

    # Set the paths in Pytest options
    config.option.htmlpath = html_report_path
    config.option.xmlpath = xml_report_path


try:
    import pytest_html
except ImportError:
    pytest_html = None
