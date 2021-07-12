from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

from framework.ui.pages.home_page import HomePage
from framework.ui.pages.login_page import LoginPage
from framework.ui.pages.new_project_page import NewProjectPage
from framework.ui.pages.new_work_packages_page import NewWorkPkgPage
from framework.ui.pages.project_overview_page import ProjectOverviewPage
from framework.ui.pages.work_packages_page import WorkPkgPage


def get_driver():
    options = ChromeOptions()
    options.headless = False
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(4)
    return driver


def start_test_with_login():
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login()
    return login_page


def controller_pages(current_page):

    if LoginPage.page_name in current_page.get_title():
        return LoginPage(current_page.driver)

    elif HomePage.page_name in current_page.get_title():
        return HomePage(current_page.driver)

    elif NewProjectPage.page_name in current_page.get_title():
        return NewProjectPage(current_page.driver)

    elif NewWorkPkgPage.page_name in current_page.get_title():
        return NewWorkPkgPage(current_page.driver)

    elif ProjectOverviewPage.page_name in current_page.get_title():
        return ProjectOverviewPage(current_page.driver)

    elif WorkPkgPage.page_name in current_page.get_title():
        return WorkPkgPage(current_page.driver)

    else:
        print("Something went wrong..")
