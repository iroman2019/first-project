from selenium.webdriver.chrome.webdriver import WebDriver


class LocationDetails:
    def __init__(self, parameter_driver:WebDriver):
        self.driver = parameter_driver

    def click_to_back_to_list_link(self):
        self.driver.find_element_by_link_text("Back to list").click()

    def assert_message_has_been_appeared(self, expected_message):
        message = self.driver.find_element_by_class_name("alert").text
        assert message == expected_message

    def assert_details_are(self, expected_name, expected_coords):
        name = self.driver.find_element_by_xpath("//tr[td[1][text() = 'Name']]/td[2]").text
        coords = self.driver.find_element_by_xpath("//tr[td[1][text() = 'Coordinates']]/td[2]").text
        assert name == expected_name
        assert coords == expected_coords