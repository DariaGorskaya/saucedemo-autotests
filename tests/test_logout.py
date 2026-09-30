from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_to_be
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(logged_in_driver):
    logged_in_driver.find_element(By.ID, "react-burger-menu-btn").click()
    wait = WebDriverWait(logged_in_driver, 10)
    logout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()
    wait.until(
        url_to_be("https://www.saucedemo.com/"),
        message="Пользователь не вернулся на страницу входа"
    )
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        ),
        message="После выхода не появилась кнопка Login"
    )