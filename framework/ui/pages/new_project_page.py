from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage

from my_config import config


class NewProjectPage(BasePage):
    url = f"{config['base_url']}/projects/new"
    page_name = "New project | OpenProject"

    PROJECT_NAME_INPUT = (By.ID, "formly_3_textInput_name_0")
    ADVANCED_SETTINGS_BTN = (By.XPATH, "//button[normalize-space()='Advanced settings']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "#formly_9_formattableInput_description_1"
                                          " > div > op-ckeditor > div > div.document-editor__editable-container > div")
    STATUS_SELECT_BTN = (By.CSS_SELECTOR, "ng-select[id='formly_9_selectProjectStatusInput__links.status_4']"
                                          " span[class='ng-arrow-wrapper']")
    SELECT_ON_TRACK = (By.XPATH, "//span[text()='On track']")
    SELECT_AT_RISK = (By.XPATH, "//span[text()='At risk']")
    SELECT_OFF_TRACK = (By.XPATH, "//span[text()='Off track']")
    CREATE_PROJECT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def project_name_input(self, project_name):
        self.type(self.PROJECT_NAME_INPUT, project_name)
        return self

    def click_advanced_settings_btn(self):
        self.click_on(self.ADVANCED_SETTINGS_BTN)
        return self

    def check_if_more_options_are_revealed(self):
        more_options_are_revealed = not (self.check_if_element_is_invisible(self.DESCRIPTION_INPUT, 2))
        return more_options_are_revealed

    def description_input(self, description):
        self.click_on(self.DESCRIPTION_INPUT)
        self.type(self.DESCRIPTION_INPUT, description)
        return self

    def click_status_select(self):
        self.click_on(self.STATUS_SELECT_BTN)
        return self

    def select_on_track(self):
        self.click_status_select()
        self.click_on(self.SELECT_ON_TRACK)
        return self

    def select_off_track(self):
        self.click_status_select()
        self.click_on(self.SELECT_OFF_TRACK)
        return self

    def select_at_risk(self):
        self.click_status_select()
        self.click_on(self.SELECT_AT_RISK)
        return self

    def click_create_btn(self):
        self.click_on(self.CREATE_PROJECT_BTN)
        self.wait_for_loader_to_disappear()
        return self
