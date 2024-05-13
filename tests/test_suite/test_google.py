from tests.pages.login_page import LoginPage


def test_login(browser):
    # Unpack the browser and logger from the fixture
    browser, logger = browser

    # Initialize the LoginPage with the browser and test name
    test_name = 'test_login'
    login_page = LoginPage(browser, test_name)

    # Open the login page
    login_page.open_login_page()

    # Perform actions using the page object
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login_button()

    # Add any additional test logic or assertions
