import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/")

def delete_by_name(name):
    driver.find_element(By.XPATH, "//tr[td[contains(text(),'" + name + "')]]/td[last()]/form/input[2]").click()

def find_id_by_name(name):
    return driver.find_element(By.XPATH, "//tr[td[contains(text(),'" + name + "')]]/td[1]").text

delete_by_name("Mr Incredible X")
WebDriverWait(driver, 10).until(
    expected_conditions.text_to_be_present_in_element((By.XPATH, "//li[@class='alert alert-info']"),
                                                      "Employee has deleted"))
find_id_by_name("Mr Incredible X")