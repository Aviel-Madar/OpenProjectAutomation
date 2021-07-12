from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage

from my_config import config


class HomePage(BasePage):
    url = f"{config['base_url']}/my/page"
    page_name = "My page"

    QUICK_ADD_MENU = (By.CSS_SELECTOR, ".icon-add.op-quick-add-menu--icon")
    NEW_PROJECT_BTN = (By.CSS_SELECTOR, "a[title='New project']")
    PROJECTS_MENU_BTN = (By.CSS_SELECTOR, "a#projects-menu>span")

    def click_new_project_btn(self):
        self.click_q_add_menu()
        self.click_on(self.NEW_PROJECT_BTN)
        return self

    def click_q_add_menu(self):
        self.click_on(self.QUICK_ADD_MENU)
        return self

    def select_project_from_menu(self, select_project):
        self.click_on(self.PROJECTS_MENU_BTN)
        select_this_project = (By.XPATH, f"//li//a[text()='{select_project}']")
        self.click_on(select_this_project)
        return self
