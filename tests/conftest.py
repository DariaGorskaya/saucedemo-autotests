from collections.abc import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import WebDriverWait

from helpers import login


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
    login(driver, username, password)

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html"),
        message="Страница с товарами не открылась", # noqa: RUF001
    )
    return driver
