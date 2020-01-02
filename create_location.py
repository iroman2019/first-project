from selenium import webdriver

from db.db_operations import DbOperation
from pages.create_location_page import CreateLocationPage
from pages.list_locations_page import ListLocationsPage
from pages.location_details_page import LocationDetails

db_operations=DbOperation()
db_operations.delete_locations()
driver=webdriver.Chrome()
list_page = ListLocationsPage(driver)
list_page.go()
list_page.assert_title_is_ok()
#list_page.assert_table_contains_location("Paks", "12.2, 10.02")
list_page.assert_count_of_table_rows_is(0)
list_page.click_to_create_location_link()
create_page = CreateLocationPage(driver)
create_page.fill_create_location_form("Paks2", "1.23,1.45")
create_page.click_to_create_button()
#list_page.go()
location_details=LocationDetails(driver)
location_details.click_to_back_to_list_link()
list_page.assert_count_of_table_rows_is(1)
list_page.assert_table_contains_location("Paks2", "1.23, 1.45")