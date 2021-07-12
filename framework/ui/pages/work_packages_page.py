from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage

from my_config import config


class WorkPkgPage(BasePage):
    identifier = None
    url = f"{config['base_url']}/projects/{identifier}/work_packages"
    page_name = "All open"

    PROJECTS_MENU_BTN = (By.CSS_SELECTOR, "a#projects-menu>span")
    ROW_IN_TABLE = (By.XPATH, "(//span[@data-field-name='id'])")

    CREATE_NEW_PKG_BTN = (By.CSS_SELECTOR, "button[aria-label='Create new work package']")
    TASK_CREATE = (By.CSS_SELECTOR, "a[aria-label='Task'] span")
    MILESTONE_CREATE = (By.CSS_SELECTOR, "a[aria-label='Milestone'] span")
    PHASE_CREATE = (By.CSS_SELECTOR, "a[aria-label='Phase'] span")

    def get_project_menu_text(self):
        project_menu_text = self.get_text(self.PROJECTS_MENU_BTN)
        return project_menu_text

    def get_number_rows_table(self):
        try:
            self.click_on((By.XPATH, "//a[normalize-space()='100']"))
            self.wait_for_loader_to_disappear()
            number_rows = len(self.wait_and_get_elements(self.ROW_IN_TABLE))
            return number_rows
        except TimeoutException:
            pass

        try:
            number_rows = len(self.wait_and_get_elements(self.ROW_IN_TABLE))
            return number_rows
        except TimeoutException:
            number_rows = 0
            return number_rows

    def select_create_task(self):
        self.click_on(self.CREATE_NEW_PKG_BTN)
        self.click_on(self.TASK_CREATE)
        self.wait_for_loader_to_disappear()
        return self

    def select_create_milestone(self):
        self.click_on(self.CREATE_NEW_PKG_BTN)
        self.click_on(self.MILESTONE_CREATE)
        return self

    def select_create_phase(self):
        self.click_on(self.CREATE_NEW_PKG_BTN)
        self.click_on(self.PHASE_CREATE)
        return self

    def get_row_as_dict(self, row_index):
        row_as_dict = dict(id=self.get_text((By.XPATH, f"(//span[@data-field-name='id'])[{row_index}]")),
                           subject=self.get_text((By.XPATH, f"(//span[@data-field-name='subject'])[{row_index}]")),
                           type=self.get_text((By.XPATH, f"(//span[@data-field-name='type'])[{row_index}]")),
                           status=self.get_text((By.XPATH, f"(//span[@data-field-name='status'])[{row_index}]")),
                           assignee=self.get_text((By.XPATH, f"(//span[@data-field-name='assignee'])[{row_index}]")),
                           priority=self.get_text((By.XPATH, f"(//span[@data-field-name='priority'])[{row_index}]")))
        return row_as_dict
