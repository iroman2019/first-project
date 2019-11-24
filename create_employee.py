import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def print_welcome():
    print("Kezdődhet a tesztelés")

def click_to_name_input():
    driver.find_element(By.ID, "create-form:name-input").click()

def type_to_name_input(name):
    driver.find_element(By.ID, "create-form:name-input").send_keys(name)

def click_to_header():
    driver.find_element(By.XPATH, "//h1").click()

def wait_for_error_message(error_message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class='invalid-feedback']"),
                                                          error_message))
    error_message = driver.find_element(By.XPATH, "//span[@class='invalid-feedback']").text
    print(error_message)

def wait_for_monogram(expected_monogram):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "create-form:monogram-text"),
                                                          expected_monogram))
    monogram=driver.find_element(By.ID, "create-form:monogram-text").text
    return monogram

def click_create_button():
    driver.find_element(By.ID, "create-form:save-button").click()

def fill_card_number_with_random_number(card_number):
    driver.find_element(By.ID, "create-form:card-number-input").send_keys(card_number + str(time.time()))



chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")
#driver.find_element(By.ID, "create-form:name-input").click()

print_welcome()
click_to_name_input()
click_to_header()
wait_for_error_message("Az alkalmazott nevét meg kell adni!")
type_to_name_input("Mr Incredible X")

print(wait_for_monogram("MIX"))
#type_to_name_input("Cserepes Virág")
click_create_button()
fill_card_number_with_random_number("1235")
click_create_button()

#emp_message=driver.find_element(By.CLASS_NAME, "invalid-feedback").text

