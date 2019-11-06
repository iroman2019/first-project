from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://iroman2019.github.io/first-project/")

# driver.find_element(By.NAME,"a") .send_keys("23")

#first_input_field=driver.find_element(By.NAME,"a")
# first_input_field.send_keys(66)
first=input("Első szám?")
driver.find_element(By.NAME,"a") .send_keys(first)
second=input("Második szám?")
driver.find_element(By.NAME,"b") .send_keys(second)
#first_input_field.screenshot("first-input.png")
#driver.find_element(By.NAME,"b") .send_keys("34")
header_text = driver.find_element(By.XPATH,"//h1").text
print(header_text)
assert header_text=="Számológép"
driver.find_element(By.ID,"submit-button").click()
result_wait=int(first)+int(second)
print(type(result_wait))
result=driver.find_element(By.ID,"result-input").get_attribute("value")
print(type(result))
driver.save_screenshot("result.png")
assert int(result)==result_wait




