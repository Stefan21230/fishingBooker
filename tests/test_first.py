from tests.base_test import BaseTest
from methods.tripsPage import *
from methods.populateTripDataPage import *
from methods.payingPage import *
import time


class FirstTest(BaseTest):
    def test_first(self, user_config):
        self.trips_page = TripsPage(self.driver)
        self.populate_trip_data = PopulateTripDataPage(self.driver)
        self.paying_page = PayingPage(self.driver)

        self.trips_page.booking_trip()

        self.populate_trip_data.populate_data(user_config("firstname"), user_config("lastname"),
                                              user_config("email"), user_config("phone"))

        self.paying_page.choose_payment()

        self.paying_page.populate_paying_data_and_book(user_config("card_number"), user_config("expiry"),
                                                       user_config("cvv"), user_config("card_name"), user_config("zip"))
