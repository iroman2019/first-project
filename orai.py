from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server")

id1 = driver.find_element(By.XPATH,"//tr[td[text()='Velence']]/td[1]").text
id2 = driver.find_element(By.XPATH,"//tr[td[text()='Báta']]/td[1]").text
print(int(id1) + int(id2))

name = driver.find_element(By.XPATH,"//tr[td[text()='9876']]/td[2]").text
print(name[:3])

name = driver.find_element(By.XPATH,"//tr[td[text()='9898']]/td[2]").text
print(name[::-1])

name = driver.find_element(By.XPATH,"//tr[td[text()='9742']]/td[2]").text
print(len(name))

valt ='11115'

name = driver.find_element(By.XPATH,"//tr[td[text()='"+valt+"']]/td[2]").text
print(name.upper())
print(name.lower())

valt1 = 11116
valt2 = 11117
valt3 =11118
name1 = driver.find_element(By.XPATH,"//tr[td[text()='"+str(valt1)+"']]/td[2]").text
name2 = driver.find_element(By.XPATH,"//tr[td[text()='"+str(valt2)+"']]/td[2]").text
name3 = driver.find_element(By.XPATH,"//tr[td[text()='"+str(valt3)+"']]/td[2]").text
print(name1 + '-' + name2 + '-' + name3)

valt3 = "Tolmács"
name1 = driver.find_element(By.XPATH,"//tr[td[text()='"+str(valt1)+"']]/td[3]").text
print((name1.replace("," , " ")).replace(".",","))




