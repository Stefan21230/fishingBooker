import os
from methods.basePage import BasePage
from pages.names_finalize_booking import *
from resources.pathData import *


class FinalizeBookingPage(BasePage):
    def save_booking_number(self):
        self.click(create_pass_close_btn, time_out=60)
        booking_number_obj = self.get_visible_element_text(booking_number).replace(".", "")
        self.write_text_in_file(booking_number_obj)

    @staticmethod
    def write_text_in_file(text):
        is_exist = os.path.exists(Path(booking_number_path))
        if not is_exist:
            os.makedirs(Path(booking_number_path))
        with open(str(Path(booking_number_path)) + '/booking_number.txt', 'w') as f:
            f.write(text)

