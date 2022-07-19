from methods.basePage import BasePage
from pages.names_paying_pages import *


class PayingPage(BasePage):
    def populate_paying_data(self, card, expiry, cvv, cardname, zipcode):
        self.scroll_to_center_of_element(expiry_date_input)
        self.input(card, credit_card_input)
        self.input(expiry, expiry_date_input)
        self.scroll_to_center_of_element(name_on_card_input)
        self.input(cvv, security_code_input)
        self.input(cardname, name_on_card_input)
        self.input(zipcode, zip_postal_code_input)
        self.scroll_to_center_of_element(request_to_book_btn)