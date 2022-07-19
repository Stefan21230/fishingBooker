from methods.basePage import BasePage
from pages.names_populate_trip_data_page import *


class PopulateTripDataPage(BasePage):
    def populate_data(self, first_name, last_name, email, phone):
        self.input(first_name, first_name_input)
        self.input(last_name, last_name_input)
        self.input(email, email_input)
        self.input(phone, phone_input)
        self.input("Hello Captain !", special_request_input)
        self.submit()

    def submit(self):
        self.scroll_to_center_of_element(continue_button)
        self.click(continue_button)