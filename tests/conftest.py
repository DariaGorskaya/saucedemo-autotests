import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {"profile.password_manager_leak_detection": False}
    )
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("visual_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html"),
        message="Страница с товарами не открылась"
    )
    yield driver