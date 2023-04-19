from methods.basePage import BasePage
from pages import names_populate_trip_data_page as trip_data


class PopulateTripDataPage(BasePage):
    def populate_data(self, first_name, last_name, email, phone):
        self.input(first_name, trip_data.first_name_input)
        self.input(last_name, trip_data.last_name_input)
        self.input(email, trip_data.email_input)
        self.input(phone, trip_data.phone_input)
        self.input("Hello Captain !", trip_data.special_request_input)
        self.submit()

    def submit(self):
        self.scroll_to_center_of_element(trip_data.continue_button)
        self.click(trip_data.continue_button)
