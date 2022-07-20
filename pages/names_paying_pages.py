from selenium.webdriver.common.by import By

# populate data
payment_method = (By.CSS_SELECTOR, "div[data-testid='new-credit-card-payment-method']")
# iframes
credit_card_iframe = "//iframe[contains(@id,'braintree-hosted-field-number')]"
expiry_date_iframe = "//iframe[contains(@id,'braintree-hosted-field-expirationDate')]"
security_code_iframe = "//iframe[contains(@id,'braintree-hosted-field-cvv')]"
name_on_card_iframe = "//iframe[contains(@id,'braintree-hosted-field-cardholderName')]"
zip_postal_iframe = "//iframe[contains(@id,'braintree-hosted-field-postalCode')]"
# input fields
credit_card_input = (By.ID, "credit-card-number")
expiry_date_input = (By.ID, "expiration")
security_code_input = (By.ID, "cvv")
name_on_card_input = (By.ID, "cardholder-name")
billing_country_input = (By.ID, "credit-card-number")
zip_postal_code_input = (By.ID, "postal-code")
request_to_book_btn = (By.CSS_SELECTOR, "button[type='submit']")