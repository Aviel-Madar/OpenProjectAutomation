from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage
from selenium.common.exceptions import TimeoutException

from my_config import config


class NewWorkPkgPage(BasePage):
    identifier = None
    url = f"{config['base_url']}/projects/{identifier}/work_packages/create_new"
    page_name = "New work package"

    FIRST_TYPE_TITLE = (By.CSS_SELECTOR,
                        "div[class='inline-edit--container status"
                        " wp-new-top-row--status -no-label'] div span[title='New']")
    LAST_TYPE_TITLE = (By.CSS_SELECTOR, "div[class='inline-edit--container type"
                                        " wp-new-top-row--type -no-label'] div span[title='Task']")

    SUBJECT_INPUT = (By.ID, "wp-new-inline-edit--field-subject")
    DESCRIPTION_INPUT = (By.XPATH, "//div[@role='textbox']")
    SAVE_BTN = (By.ID, "work-packages--edit-actions-save")
    CLOSE_INNER_WINDOW_BTN = (By.XPATH, "//span[@class='icon-context icon-close']")

    def get_type_title(self):
        first_type_title = self.get_text(self.FIRST_TYPE_TITLE)
        last_type_title = self.get_text(self.LAST_TYPE_TITLE)
        type_title = f"{first_type_title} {last_type_title}"
        return type_title

    def type_subject_input(self, subject):
        self.type(self.SUBJECT_INPUT, subject)
        return self

    def type_description_input(self, description):
        self.type(self.DESCRIPTION_INPUT, description)
        return self

    def click_save_btn(self):
        self.click_on(self.SAVE_BTN)
        self.wait_for_loader_to_disappear()
        try:
            self.click_on(self.CLOSE_INNER_WINDOW_BTN)
        except TimeoutException:
            return self
        return self
