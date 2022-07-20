from methods.basePage import BasePage
from pages.names_paying_pages import *


class PayingPage(BasePage):
    def populate_paying_data_and_book(self, card, expiry, cvv, cardname, zipcode):
        self.input_in_iframe_element(credit_card_iframe, credit_card_input, card)
        self.input_in_iframe_element(expiry_date_iframe, expiry_date_input, expiry)
        self.input_in_iframe_element(security_code_iframe, security_code_input, cvv)
        self.input_in_iframe_element(name_on_card_iframe, name_on_card_input, cardname)
        self.input_in_iframe_element(zip_postal_iframe, zip_postal_code_input, zipcode)
        self.click(request_to_book_btn)

    def choose_payment(self):
        self.scroll_to_center_of_element(payment_method)
        self.click(payment_method)
