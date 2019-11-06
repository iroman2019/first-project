from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://learnwebservices.com/locations/server")
driver.find_element(By.ID,"coordsInput").click()
driver.find_element(By.ID,"coordsInput").send_keys("1,1")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
alerts = driver.find_elements(By.XPATH, "/html/body/div/form/div[1]/div")
print("hello")
print(alerts[0].text)
assert alerts[0].text=="must not be blank"