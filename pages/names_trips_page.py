from selenium.webdriver.common.by import By

checker_form = (By.ID, "charter-trips")
packages_container = (By.ID, "packages-container")
# date picker
booking_date_search = (By.ID, "booking_date_availability_form_search")
date_picker_table = "//div[@class='datepicker-days']//table[@class='table-condensed']"
date_picker_li = (By.XPATH, date_picker_table + "//tbody//tr//td[@class='day']")
date_active_picker_li = (By.XPATH, date_picker_table + "//tbody//tr//td[@class='active day']")
date_new_picker_li = (By.XPATH, date_picker_table + "//tbody//tr//td[@class='new day']")
# days picker
day_picker = (By.ID, "booking_days")
days = (By.XPATH, "//select[@id='booking_days']//option")
# group size picker
group_pickers = (By.CSS_SELECTOR, "div[data-events-category='Availability search']")
adults_number = (By.CSS_SELECTOR, "strong[class='adults-number']")
children_number = (By.CSS_SELECTOR, "strong[class='children-number']")
adults_minus_btn = (By.XPATH, "//strong[@class='adults-number']/parent::td/parent::tr/child::td/child::button")
# locators which aren't work
# adults_minus_btn = (By.CSS_SELECTOR, "button[class='fbkr-button white adults-children-btn adults-minus']")
# adults_minus_btn = (By.CSS_SELECTOR, ".button.fbkr-button.white.adults-children-btn.adults-minus")
# adults_minus_btn = (By.XPATH, "//button[contains(class(), 'adults-minus')]")

# check availability
check_availability_btn = (By.ID, "check-availability-btn")
# packages
packages_ul = (By.CSS_SELECTOR, "ul[class='list-unstyled']")
packages_li = (By.XPATH, "//div[@class='charter-item-tabs']//li")
package_type = (By.CSS_SELECTOR, "span[class='package-title']")
first_package_button = (By.ID, "bookbtn-0")

