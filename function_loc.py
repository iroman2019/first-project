from selenium import webdriver
from selenium.webdriver.common.by import By

def print_coords_by_name(name):
    xpath = "//tr[td[text()='name']]/td[3]".replace("name", name)
    coords=driver.find_element(By.XPATH, xpath).text
    print(coords)
    return coords


driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server")

print_coords_by_name("Paks")

def larges(name):
    length=print_coords_by_name(name).split(",")
    length2=length[1]
    return float(length2)>48

print(larges("Paks"))

def favorit(name, coords):
    driver.set_window_size(1024, 612)
    driver.find_element(By.ID, "nameInput").send_keys(name)
    driver.find_element(By.ID, "coordsInput").send_keys(coords)
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

favorit("ildi_varos", "23,24")

def favorit2(name, coord1="47.21283333" , coord2="16.8435"):
    driver.set_window_size(1024, 612)
    driver.find_element(By.ID, "nameInput").send_keys(name)
    driver.find_element(By.ID, "coordsInput").send_keys(coord1+","+coord2)
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

favorit2("ildi2", "23", "34")