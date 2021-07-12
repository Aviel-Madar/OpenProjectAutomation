from tests.tests_ui.conftest import start_test_with_login, controller_pages

from generator_string import GeneratorString


def test_009():
    home_page = controller_pages(start_test_with_login())
    home_page.click_new_project_btn()

    new_project_page = controller_pages(home_page)
    project_name = f"project created automatically {GeneratorString().get_unique_string()}ABC123,/#@$%"
    new_project_page.project_name_input(project_name)

    new_project_page.click_advanced_settings_btn()
    assert new_project_page.check_if_more_options_are_revealed(), "More options need to be revealed."

    new_project_page.description_input(" some text to the description text box")

    new_project_page.select_on_track()

    new_project_page.click_create_btn()

    project_overview_page = controller_pages(new_project_page)
    project_overview_page.click_menu_work_pkg_link()
    work_pkg_page = controller_pages(project_overview_page)

    assert work_pkg_page.get_project_menu_text() == project_name, f"The name created project should be-'{project_name}'"
