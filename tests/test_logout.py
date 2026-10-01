from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from test_data import VALID_CREDENTIALS


@pytest.mark.parametrize(
    ("username", "password"),
    VALID_CREDENTIALS
)


def test_logout(logged_in_driver, username, password):
    logged_in_driver.find_element(By.ID, "react-burger-menu-btn").click()

    wait = WebDriverWait(logged_in_driver, 10)
    logout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()

    wait.until(
        EC.url_to_be("https://www.saucedemo.com/"),
        message="Пользователь не вернулся на страницу входа"
    )
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        ),
        message="После выхода не появилась кнопка Login"
    )