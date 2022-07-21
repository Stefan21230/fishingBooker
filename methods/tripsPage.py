from methods.basePage import BasePage
from pages.names_trips_page import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time


class TripsPage(BasePage):
    def booking_trip(self, day="1"):
        self.scroll_to_center_of_element(checker_form)
        self.pick_number_of_days(day)
        # self.pick_group_size()
        self.choose_package()

    def pick_the_first_available_date(self, counter=1):
        self.scroll_to_center_of_element(booking_date_search)
        self.click(booking_date_search)
        date_days = self.wait_for_elements_to_be_presence(date_picker_li) + \
                    self.wait_for_elements_to_be_presence(date_new_picker_li)
        self.click(date_days[counter])
        self.click(check_availability_btn)
        counter += 1
        return counter

    def pick_number_of_days(self, day="1"):
        self.scroll_to_center_of_element(day_picker)
        self.click(day_picker)
        days_obj = self.wait_for_elements_to_be_presence(days)
        for d in days_obj:
            if day == d.get_attribute("value"):
                self.click(d)

    def pick_group_size(self):
        # Buttons in this sections are ElementNotInteractableException, so I didn't find a pretty way
        # to click on them.
        self.click(group_pickers)
        adults_number_obj = self.wait_for_element_to_be_presence(adults_number)
        self.action_click(adults_minus_btn)

    def choose_package(self):
        counter = self.pick_the_first_available_date()
        self.scroll_to_center_of_element(packages_ul)
        all_packages = self.wait_for_elements_to_be_visible(packages_li)
        for package in all_packages:
            package_title = package.find_element(By.CSS_SELECTOR, "span[class='package-title']")
            if package_title.text == "4 hour trip":
                strong_elements = package.find_elements(By.TAG_NAME, "strong")
                for strong in strong_elements:
                    if strong.text == "Not Available":
                        self.pick_the_first_available_date(counter=counter)
                        self.choose_package()
                    elif strong.text == "":
                        book_btn = package.find_element(By.CSS_SELECTOR, "button[name='booking_package']")
                        self.click(book_btn)
                        break
                    else:
                        pass
                break
                # self.click(first_package_button)
                # break
