from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def login(driver: WebDriver, username: str, password: str) -> None:
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    driver.find_element(By.ID, "login-button").click()
