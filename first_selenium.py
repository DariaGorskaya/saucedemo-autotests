from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Страница с товарами не открыта'
products_page_title = driver.find_element(By.CLASS_NAME, "title")
assert products_page_title.text == 'Products', 'Неверный заголовок страницы'
products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
assert products, 'Нет товаров на странице'

driver.quit()