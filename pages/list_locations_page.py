from selenium.webdriver.chrome.webdriver import WebDriver


class ListLocationsPage:

    def __init__(self, parameter_driver:WebDriver):
        self.driver = parameter_driver

    def go(self):
        self.driver.get("http://localhost:8080/server")

    def assert_title_is_ok(self):
        assert "Locations"==self.driver.find_element_by_xpath("//h1").text

    def assert_table_contains_location(self, name, expected_coords):
        # Use literal string interpolation
        # https://realpython.com/python-string-formatting/
        xpath = "//tr[td[text() = 'name']]/td[2]".replace("name", name)
        coords = self.driver.find_element_by_xpath(xpath).text
        print("Actual:" + coords)
        print("Expected: " + expected_coords)
        # Doesn't print actual and expected values
        assert coords == expected_coords

    def assert_count_of_table_rows_is(self, expected_count):
        xpath = "//tbody/tr"
        count = len(self.driver.find_elements_by_xpath(xpath))
        assert count == expected_count

    def click_to_create_location_link(self):
        self.driver.find_element_by_link_text("Create location").click()