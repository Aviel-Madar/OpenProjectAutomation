from selenium.webdriver.common.by import By
from framework.ui.base_page import BasePage

from my_config import config


class ProjectOverviewPage(BasePage):
    identifier = None
    url = f"{config['base_url']}/projects/{identifier}"
    page_name = "Overview"

    MENU_WORK_PKG_LINK = (By.CSS_SELECTOR, "a#main-menu-work-packages>span>span")

    def click_menu_work_pkg_link(self):
        self.click_on(self.MENU_WORK_PKG_LINK)
        self.wait_for_loader_to_disappear()
        return self
