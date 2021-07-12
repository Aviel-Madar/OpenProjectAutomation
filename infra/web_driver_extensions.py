from webdriver_manager import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from my_config import config


class WebDriverExtensions(object):

    def __init__(self, web_driver):
        self.driver = web_driver

    timeout = config['DEFAULT_TIMEOUT']

    def wait_and_get_element(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        return self.driver.find_element(*element)

    def wait_for_element_and_click(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        WebDriverWait(self, time).until(EC.element_to_be_clickable(element), "Element is not clickable")
        self.driver.find_element(*element).click()

    def wait_for_element_and_send_text(self, element, text, time=timeout):
        WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(text)

    def wait_for_element_and_get_text(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        return self.driver.find_element(*element).text

    def wait_for_element_and_get_text_from_input(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        return self.driver.find_element(*element).get_attribute("value")

    def check_if_element_is_visible(self, element, time=timeout):
        self.wait_for_element(element, time)
        elements = self.driver.find_elements(*element)
        if len(elements) > 0:
            return True
        else:
            return False

    def check_if_element_is_invisible(self, element, time=timeout):
        try:
            WebDriverWait(self, time).until(EC.invisibility_of_element_located(element), "Element is not invisible")
            return True
        except TimeoutException:
            return False

    def wait_for_element(self, element, time=timeout):
        try:
            WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        except TimeoutException:
            pass

    def wait_for_element_until_invisible(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.invisibility_of_element_located(element), "Element is not invisible")

    def wait_for_element_until_visible(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.visibility_of_element_located(element), "Element is not visible")

    def fast_check_if_element_exist(self, element):
        elements = self.driver.find_elements(*element)
        if len(elements) > 0:
            return True
        else:
            return False

    def wait_and_get_elements(self, element, time=timeout):
        WebDriverWait(self, time).until(EC.presence_of_element_located(element), "Element is not present")
        return self.driver.find_elements(*element)

    def check_visible_of_elements(self, elements, time=timeout):
        for element in elements:
            self.wait_for_element(time)
            searched_elements = self.driver.find_elements(*element)
            if len(searched_elements) < 1:
                return False
        return True

    @property
    def actions(self):
        return ActionChains(driver)
