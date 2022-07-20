import time
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, time_out=10):
        self.wait_for_element_to_be_clickable(locator, time_out).click()

    def action_click(self, locator):
        element = self.wait_for_element_to_be_presence(locator)
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def input(self, text: str, locator, time_out=10):
        self.wait_for_element_to_be_presence(locator, time_out).send_keys(text)

    def get_visible_element_text(self, locator, time_out=10):
        """
        Method get WebElement text.
        """
        return self.wait_for_element_to_be_visible(locator, time_out).text

    def input_in_iframe_element(self, iframe_locator, locator, text):
        iframe = self.driver.find_element(By.XPATH, iframe_locator)
        self.driver.switch_to.frame(iframe)
        # element = self.wait_for_element_to_be_visible(locator)
        self.input(text, locator)
        self.driver.switch_to.default_content()

    def scroll_to_element(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to_center_of_element(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = self.driver.execute_script('return window.innerHeight')
        window_y = self.driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def wait_for_element_to_be_visible(self, locator, time_out=10):
        """
        Method check is WebElement visible.
        """
        try:
            return WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise Exception(
                "Couldn't find element that has locator: {} , for time period of: {} seconds.".format(locator[1],
                                                                                                      time_out))

    def wait_for_element_to_be_clickable(self, locator, time_out=10):
        """
        Method check is WebElement clickable.
        """
        try:
            return WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator))
        except Exception:
            raise Exception(
                "Couldn't find element that has locator: {} , for time period of: {} seconds.".format(locator[1],
                                                                                                      time_out))

    def wait_for_elements_to_be_visible(self, locator, time_out=10):
        """
        Method check is WebElement visible.
        """
        try:
            return WebDriverWait(self.driver, time_out).until(EC.visibility_of_all_elements_located(locator))
        except Exception:
            raise Exception(
                "Couldn't find element that has locator: {} , for time period of: {} seconds.".format(locator[1],
                                                                                                      time_out))

    def wait_for_element_to_be_presence(self, locator, time_out=10):
        """
        Method check if WebElement  is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        locator - used to find the element returns the WebElement once it is located
        """
        try:
            return WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator))
        except Exception:
            raise Exception("Couldn't find element that has locator: {} , for time period of: {} seconds.".format(locator[1], time_out))

    def wait_for_elements_to_be_presence(self, locator, time_out=10):
        """
        Method check if WebElements are present on the DOM
        of a page. This does not necessarily mean that the elements is visible.
        locator - used to find the elements returns the WebElement once it is located
        """
        try:
            return WebDriverWait(self.driver, time_out).until(EC.presence_of_all_elements_located(locator))
        except Exception:
            raise Exception("Couldn't find element that has locator: {} , for time period of: {} seconds.".format(locator[1], time_out))

