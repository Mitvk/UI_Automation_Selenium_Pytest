from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.utility import read_config, setup_logger


class LoginPage:
    def __init__(self, driver: WebDriver, test_name):
        self.driver = driver

        # Set up logger for the page
        self.logger = setup_logger(test_name)

        # Read the configuration data
        config = read_config()

        # Retrieve the login URL from config
        self.login_url = config['urls']['login_url']
        self.username = config['credentials']['username']
        self.password = config['credentials']['password']

        # Define locators
        self.username_locator = (By.ID, 'username')
        self.password_locator = (By.ID, 'password')
        self.login_button_locator = (By.XPATH, "//button[@type='submit']")

        self.logger.info("Initialized LoginPage")

    def open_login_page(self):
        # Open the login page URL
        self.driver.get(self.login_url)
        self.logger.info(f"Navigated to URL: {self.login_url}")

    def enter_username(self):
        self.driver.find_element(*self.username_locator).send_keys(self.username)
        self.logger.info(f"Entered username: {self.username}")

    def enter_password(self):
        self.driver.find_element(*self.password_locator).send_keys(self.password)
        self.logger.info(f"Entered password: {self.password}")

    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()
        self.logger.info("Clicked login button")
