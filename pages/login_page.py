from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Represent the SauceDemo login page."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def enter_password(self, password: str) -> None:
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login_button(self) -> None:
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
