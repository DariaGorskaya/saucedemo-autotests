from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    """Represent the SauceDemo inventory page."""

    URL = "https://www.saucedemo.com/inventory.html"
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_LIST = (By.CSS_SELECTOR, '[data-test="inventory-list"]')
    INVENTORY_ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def wait_until_loaded(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.url_to_be(self.URL),
            message="Страница с товарами не открылась",  # noqa: RUF001
        )
        wait.until(
            EC.visibility_of_element_located(self.TITLE),
        )
        wait.until(
            EC.visibility_of_element_located(self.INVENTORY_LIST),
            message="Список товаров не появился",
        )
        wait.until(
            EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS),
            message="Карточки товаров не появились",
        )

    def get_title_text(self) -> str:
        return self.driver.find_element(*self.TITLE).text

    def get_inventory_items(self) -> list[WebElement]:
        return self.driver.find_elements(*self.INVENTORY_ITEMS)

    def logout(self) -> None:
        wait = WebDriverWait(self.driver, 10)

        menu_button = wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON),
        )
        menu_button.click()

        logout_button = wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON),
        )
        logout_button.click()
