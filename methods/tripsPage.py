from methods.basePage import BasePage
from pages import names_trips_page as trips_p
from selenium.webdriver.common.by import By


class TripsPage(BasePage):
    def booking_trip(self, day="1"):
        self.scroll_to_center_of_element(trips_p.checker_form)
        self.pick_number_of_days(day)
        # self.pick_group_size()
        self.choose_package()

    def pick_the_first_available_date(self, counter=1):
        self.scroll_to_center_of_element(trips_p.booking_date_search)
        self.click(trips_p.booking_date_search)
        date_days = self.wait_for_elements_to_be_presence(trips_p.date_picker_li) + \
                    self.wait_for_elements_to_be_presence(trips_p.date_new_picker_li)
        self.click(date_days[counter])
        self.click(trips_p.check_availability_btn)
        counter += 1
        return counter

    def pick_number_of_days(self, day="1"):
        self.scroll_to_center_of_element(trips_p.day_picker)
        self.click(trips_p.day_picker)
        days_obj = self.wait_for_elements_to_be_presence(trips_p.days)
        for d in days_obj:
            if day == d.get_attribute("value"):
                self.click(d)

    def pick_group_size(self):
        # Buttons in this sections are ElementNotInteractableException, so I didn't find a pretty way
        # to click on them.
        self.click(trips_p.group_pickers)
        adults_number_obj = self.wait_for_element_to_be_presence(trips_p.adults_number)
        self.action_click(trips_p.adults_minus_btn)

    def choose_package(self):
        counter = self.pick_the_first_available_date()
        self.scroll_to_center_of_element(trips_p.packages_ul)
        all_packages = self.wait_for_elements_to_be_visible(trips_p.packages_li)
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
