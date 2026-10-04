from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from test_data import STANDARD_USER_CREDENTIALS


def test_login(driver: WebDriver) -> None:
    username, password = STANDARD_USER_CREDENTIALS
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html"),
        message="Страница с товарами не открылась", # noqa: RUF001
    )
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name"),
        ),
        message="Нет товаров на странице",
    )

    products_page_title = driver.find_element(By.CLASS_NAME, "title")
    assert products_page_title.text == "Products", "Неверный заголовок страницы"
