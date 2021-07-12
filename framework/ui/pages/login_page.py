from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage

from my_config import config


class LoginPage(BasePage):
    url = f"{config['base_url']}/login"
    page_name = "Sign in"

    USER_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input[data-disable-with='Loading...']")

    def login(self):
        self.type_user_input()
        self.type_password_input()
        self.click_sub_btn()
        return self

    def type_user_input(self):
        self.type(self.USER_INPUT, config['my_login']['username'])
        return self

    def type_password_input(self):
        self.type(self.PASSWORD_INPUT, config['my_login']['password'])
        return self

    def click_sub_btn(self):
        self.click_on(self.SUBMIT_BTN)
        return self
