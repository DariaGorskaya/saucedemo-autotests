from collections.abc import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {"profile.password_manager_leak_detection": False},
    )
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver: WebDriver, username: str, password: str) -> WebDriver:
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.wait_until_loaded()

    return driver
