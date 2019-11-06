import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://learnwebservices.com/locations/server")
ts = time.time()
name = "ildi" + str(ts)
print (name)
driver.find_element(By.ID,"nameInput").click()
driver.find_element(By.ID,"nameInput").send_keys(name)
driver.find_element(By.ID,"coordsInput").click()
driver.find_element(By.ID,"coordsInput").send_keys("1,1")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
driver.find_element(By.XPATH, "//tr[td[text()='" + name + "']]/td[6]/form/button").click()
assert driver.switch_to.alert.text == "Are you sure?"
driver.switch_to.alert.accept()
elements = driver.find_elements(By.XPATH, "//td[text()='" + name + "']")
assert len(elements) == 0

