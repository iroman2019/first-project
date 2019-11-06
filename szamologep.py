from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://iroman2019.github.io/first-project/")

driver.find_element(By.NAME,"a") .send_keys("23")
driver.find_element(By.NAME,"b") .send_keys("34")
header_text = driver.find_element(By.XPATH,"//h1").text
print(header_text)
assert header_text=="Számológép"
driver.find_element(By.ID,"submit-button").click()
result=driver.find_element(By.ID,"result-input").get_attribute("value")
print("eredmény: "+result)
assert result=="57"




