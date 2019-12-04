import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def assert_title_is(i_title):
    page_title = driver.title
    print("title: " + page_title)
    assert i_title == page_title

def assert_header_is(title):
    h2_title = driver.find_element(By.XPATH, "//h2[1]").text
    print("first h2: " + h2_title)
    assert title == h2_title

def assert_image_is_present(image):
    p_len = len(driver.find_elements(By.XPATH, "//img[contains(@src, 'text')]".replace("text", image)))
    print(str(p_len))
    assert p_len>0

def test_home_page():
    assert_title_is("PetClinic :: a Spring Framework demonstration")
    assert_header_is("Welcome")
    assert_image_is_present("pets.png")

def goto_home_page():
    driver.find_element(By.XPATH, "//li/a[@title='home page']").click()

def goto_find_owners():
    driver.find_element(By.XPATH, "//li/a[@title='find owners']").click()

def goto_veterinarians():
    driver.find_element(By.XPATH, "//li/a[@title='veterinarians']").click()

def test_find_owners_page():
    goto_find_owners()
    assert_title_is("PetClinic :: a Spring Framework demonstration")
    assert_header_is("Find Owners")
    label_len = len(driver.find_elements(By.XPATH, "//label[contains(text(), 'Last name')]"))
    print("label len: " + str(label_len))
    assert label_len>0
    input_len = len(driver.find_elements(By.XPATH, "//input[contains(@id, 'lastName')]"))
    print("input len: " + str(input_len))
    assert input_len>0

def print_veterinarian_count():
    goto_veterinarians()
    vegetarian_count = len(driver.find_elements(By.XPATH, "//tbody/tr"))
    print("the number of veterinarians: " + str(vegetarian_count))

def print_veterinarian_names():
    goto_veterinarians()
    names = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    for name in names:
        print(name.text)

def print_veterinarian_with_specialities(speciality):
    goto_veterinarians()
    xpath: str ="//tbody/tr[td[span[contains(text(),'spec')]]]/td[1]"
    veterians_by_speciality = driver.find_elements(By.XPATH, xpath.replace('spec', speciality))
    print("The " + str(speciality)+ "('s)")
    for name in veterians_by_speciality:
        print(name.text)

def print_veterinarian_skill_count():
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    for row in rows:
        name = row.find_element(By.XPATH, "./td[1]")
        #print(name.text)
        spec_number = len(row.find_elements(By.XPATH, "./td[2]/span"))
        print(name.text + " "+ str(spec_number))

def get_veterinarian_names():
    names = []  ## Üres lista létrehozása
    names_tds = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    for name in names_tds:
        names.append(name.text)  ## Új elem hozzáadása
    print(names)
    return names

def print_veterinarian_name_contains(part):
    goto_veterinarians()
    names =get_veterinarian_names()
    for name in names:
        if (part in name):
            print(name)

def print_veterinarian_longer_than(number_of_characters):
    goto_veterinarians()
    names = get_veterinarian_names()
    print("Longer than " + str(number_of_characters) + " character(s):")
    for name in names:
        if len(name) > number_of_characters:
            print(name)

def print_longest_name():
    goto_veterinarians()
    names = get_veterinarian_names()
    the_longest_name = ""
    for name in names:
        if len(name) > len(the_longest_name):
            the_longest_name = name
    print("The longest name is: "+ the_longest_name)

def search_with(name):
    goto_find_owners()
    driver.find_element(By.ID, "lastName").send_keys(name)
    driver.find_element(By.XPATH,"//button[contains(text(),'Find')]").click()

def assert_owner_with_name(name):
    search_with(name)
    name_len = len(driver.find_elements(By.XPATH, "//a[text()='tname'".replace('tname',name)))
    assert name_len>0

def fill_database():
    goto_find_owners()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) span:nth-child(2)").click()
    driver.find_element(By.LINK_TEXT, "Add Owner").click()
    driver.find_element(By.ID, "firstName").send_keys("Kiss")
    driver.find_element(By.ID, "lastName").send_keys("Eszter")
    driver.find_element(By.ID, "address").send_keys("Pécs")
    driver.find_element(By.ID, "city").send_keys("Árok utca 7")
    driver.find_element(By.ID, "telephone").send_keys("3243546789")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys("Lili")
    driver.find_element(By.ID, "birthDate").send_keys("1999-12-12")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, ".active span:nth-child(2)").click()
    driver.find_element(By.LINK_TEXT, "Add Owner").click()
    driver.find_element(By.ID, "firstName").send_keys("Nagy")
    driver.find_element(By.CSS_SELECTOR, ".has-feedback").click()
    driver.find_element(By.ID, "lastName").send_keys("Eszter")
    driver.find_element(By.ID, "address").send_keys("Pécs")
    driver.find_element(By.ID, "city").send_keys("Árok utca 13")
    driver.find_element(By.ID, "telephone").send_keys("3243546784")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    driver.find_element(By.ID, "name").send_keys("Kinga")
    driver.find_element(By.ID, "birthDate").send_keys("1989-10-10")
    driver.find_element(By.ID, "type").click()
    dropdown = driver.find_element(By.ID, "type")
    dropdown.find_element(By.XPATH, "//option[. = 'dog']").click()
    driver.find_element(By.ID, "type").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, ".active > a").click()
    driver.find_element(By.LINK_TEXT, "Add Owner").click()
    driver.find_element(By.ID, "firstName").send_keys("Balogh")
    driver.find_element(By.ID, "lastName").send_keys("Petra")
    driver.find_element(By.ID, "address").send_keys("Pécs")
    driver.find_element(By.ID, "city").send_keys("Répa u. 7")
    driver.find_element(By.ID, "telephone").send_keys("6665556576")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys("Lala")
    driver.find_element(By.ID, "birthDate").send_keys("1999-12-12")
    driver.find_element(By.ID, "birthDate").send_keys("1999-12-20")
    driver.find_element(By.ID, "type").click()
    dropdown = driver.find_element(By.ID, "type")
    dropdown.find_element(By.XPATH, "//option[. = 'cat']").click()
    driver.find_element(By.ID, "type").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()

def count_number_of_owners():
    owner_count = len(driver.find_elements(By.XPATH, "//tbody/tr"))
    print("the number of owner: " + str(owner_count))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://localhost:8080")

test_home_page()
goto_find_owners()
goto_veterinarians()
goto_home_page()
test_find_owners_page()
print_veterinarian_count()
print_veterinarian_names()
print_veterinarian_with_specialities("radiology")
print_veterinarian_skill_count()
get_veterinarian_names()
print_veterinarian_name_contains("en")
print_veterinarian_longer_than(12)
print_longest_name()
fill_database()
search_with("Eszter")
count_number_of_owners()