from selenium.webdriver.common.by import By

# populate data
credit_card_input = (By.ID, "credit-card-number")
# expiry_date_input = (By.ID, "expiration")
expiry_date_input = (By.CSS_SELECTOR, "input[id='expiration']")
security_code_input = (By.ID, "cvv")
name_on_card_input = (By.ID, "cardholder-name")
billing_country_input = (By.ID, "credit-card-number")
zip_postal_code_input = (By.ID, "postal-code")
request_to_book_btn = (By.CSS_SELECTOR, "button[type='submit']")