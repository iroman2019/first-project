from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server")

coord = driver.find_element(By.XPATH,"//tr[td[text()='"+"Dobogókő"+"']]/td[3]").text
print(coord)
print(type(coord))

nev = driver.find_element(By.XPATH,"//tr[td[text()='9277']]/td[2]").text
print(nev)
print(type(nev))

azon = driver.find_element(By.XPATH,"//tr[td[text()='Alattyán']]/td[1]").text
print(azon)
print(type(azon))

azon = driver.find_element(By.XPATH,"//tr[td[text()='Bakonybánk']]/td[1]").text
azon = int(azon)
print(azon)
print(type(azon))

azon = driver.find_element(By.XPATH,"//tr[td[text()='Zsámbék']]/td[3]").text
print(azon)
azon = float(azon)
print(azon)
print(type(azon))
