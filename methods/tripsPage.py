from methods.basePage import BasePage
from pages.names_trips_page import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class TripsPage(BasePage):
    def booking_trip(self, day="1"):
        self.scroll_to_center_of_element(checker_form)
        self.pick_the_first_available_date()
        self.pick_number_of_days(day)
        # self.pick_group_size()
        self.click(check_availability_btn)
        self.choose_package()

    def pick_the_first_available_date(self):
        self.click(booking_date_search)
        date = self.wait_for_elements_to_be_presence(date_picker_li)
        self.click(date[1])

    def pick_number_of_days(self, day="1"):
        self.click(day_picker)
        days_obj = self.wait_for_elements_to_be_presence(days)
        for d in days_obj:
            if day == d.get_attribute("value"):
                self.click(d)

    def pick_group_size(self):
        self.click(group_pickers)
        adults_number_obj = self.wait_for_elements_to_be_presence(adults_number)
        print(adults_number_obj[1].text)
        # self.wait_for_elements_to_be_presence(adults_minus_btn)
        # self.click(adults_plus_btn)

    def choose_package(self):
        self.scroll_to_center_of_element(packages_ul)
        all_packages = self.wait_for_elements_to_be_visible(packages_li)
        for package in all_packages:
            package_title = package.find_element(By.CSS_SELECTOR, "span[class='package-title']")
            if package_title.text == "4 hour trip":
                self.click(first_package_button)
                break
