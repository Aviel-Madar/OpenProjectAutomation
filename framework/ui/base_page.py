from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from infra.web_driver_extensions import WebDriverExtensions


class BasePage(WebDriverExtensions):

    url = None
    page_name = "Unknown page"
    LOADER = (By.CSS_SELECTOR, "div[class*='ui-async-content__spinner']")

    def navigate(self):
        self.driver.get(self.url)
        return self

    def click_on(self, locator):
        self.wait_for_element_and_click(locator)

    def type(self, locator, text):
        self.wait_for_element_and_send_text(locator, text)

    def get_text(self, locator):
        return self.wait_for_element_and_get_text(locator)

    def visibility_of_element(self, locator):
        return self.check_if_element_is_visible(locator)

    def compare_url(self):
        if self.driver.current_url == self.url:
            return True
        else:
            return False

    def wait_for_redirect(self, timeout=4):
        WebDriverWait(self.driver, timeout).until(lambda driver: self.driver.current_url == self.url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_element(self, element, timeout):
        return self.wait_and_get_element(element, timeout)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def is_loaded(self, element, timeout=2):
        el = self.wait_and_get_element(element, timeout)
        if el is not None:
            return True
        else:
            return False

    def wait_for_loader_to_disappear(self):
        if self.fast_check_if_element_exist(self.LOADER):
            loader_element = self.wait_and_get_element(self.LOADER)
            if loader_element.is_displayed():
                self.wait_for_element_until_invisible(self.LOADER)
