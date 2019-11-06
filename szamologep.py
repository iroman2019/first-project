from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://iroman2019.github.io/first-project/")

driver.find_element(By.NAME,"a") .send_keys("3")
driver.find_element(By.NAME,"b") .send_keys("4")

