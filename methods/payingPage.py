from methods.basePage import BasePage
from pages import names_paying_pages as paying_p


class PayingPage(BasePage):
    def populate_paying_data_and_book(self, card, expiry, cvv, cardname, zipcode):
        self.input_in_iframe_element(paying_p.credit_card_iframe, paying_p.credit_card_input, card)
        self.input_in_iframe_element(paying_p.expiry_date_iframe, paying_p.expiry_date_input, expiry)
        self.input_in_iframe_element(paying_p.security_code_iframe, paying_p.security_code_input, cvv)
        self.input_in_iframe_element(paying_p.name_on_card_iframe, paying_p.name_on_card_input, cardname)
        self.input_in_iframe_element(paying_p.zip_postal_iframe, paying_p.zip_postal_code_input, zipcode)
        self.click(paying_p.request_to_book_btn)

    def choose_payment(self):
        self.scroll_to_center_of_element(paying_p.payment_method)
        self.click(paying_p.payment_method)
