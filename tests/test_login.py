from selenium.webdriver.remote.webdriver import WebDriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data import STANDARD_USER_CREDENTIALS


def test_login(driver: WebDriver) -> None:
    username, password = STANDARD_USER_CREDENTIALS
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.wait_until_loaded()

    assert inventory_page.get_title_text() == "Products", "Неверный заголовок страницы"
    assert len(inventory_page.get_inventory_items()) > 0, "На странице нет товаров"  # noqa: RUF001
