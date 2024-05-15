from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utility import read_config, setup_logger


class base:

    def __init__(self, driver: WebDriver, test_name):
        self.driver = driver

        # Set up logger for the page
        self.logger = setup_logger(test_name)

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, element_locator, timeout=5):
        element: WebElement
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(element_locator)
            )
        except TimeoutException:
            self.logger.info("Element not found within the given time")
        return element

    def click_element(self, element_locator, timeout=5):
        element = self.wait_for_element(element_locator=element_locator)
        element.click()

    def enter_text(self, element_locator, text, timeout=5):
        element = self.wait_for_element(element_locator=element_locator)
        element.send_keys(text)
