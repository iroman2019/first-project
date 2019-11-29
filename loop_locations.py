import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.learnwebservices.com/locations/server")

xpath = "//tr/td[2]"
nodes = driver.find_elements(By.XPATH, xpath)
print(nodes)
for node in nodes[::2]:
    print(node.text)

print(len(nodes))

input = driver.find_element(By.ID, "nameInput")
text = ''
for i in range(1,41):
    input.send_keys('a')

#for i in range(1,6):

#input.send_keys(text)