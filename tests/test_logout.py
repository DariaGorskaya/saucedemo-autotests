import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data import VALID_CREDENTIALS


@pytest.mark.parametrize(
    ("username", "password"),
    VALID_CREDENTIALS,
)
def test_logout(logged_in_driver: WebDriver, username: str, password: str) -> None:  # noqa: ARG001
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.logout()

    login_page = LoginPage(logged_in_driver)
    login_page.wait_until_loaded()

    assert logged_in_driver.current_url == LoginPage.URL
    assert login_page.is_login_button_displayed()
