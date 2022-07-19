from selenium.webdriver.common.by import By

# populate data
first_name_input = (By.CSS_SELECTOR, "input[data-testid='checkout-first-name-input']")
last_name_input = (By.CSS_SELECTOR, "input[data-testid='checkout-last-name-input']")
email_input = (By.CSS_SELECTOR, "input[data-testid='checkout-email-input']")
phone_input = (By.CSS_SELECTOR, "input[type='tel']")
special_request_input = (By.CSS_SELECTOR, "textarea[data-testid='special-requests-textarea']")
# continue button
continue_button = (By.CSS_SELECTOR, "button[type='submit']")