from tests.tests_ui.conftest import start_test_with_login, controller_pages

from generator_string import GeneratorString


def test_010():
    home_page = controller_pages(start_test_with_login())
    home_page.select_project_from_menu("TestProject1")

    project_overview_page = controller_pages(home_page)
    project_overview_page.click_menu_work_pkg_link()
    work_pkg_page = controller_pages(project_overview_page)

    current_table_rows = work_pkg_page.get_number_rows_table()

    work_pkg_page.select_create_task()

    new_work_pkg_page = controller_pages(work_pkg_page)

    expected_type_title = "New TASK"
    assert new_work_pkg_page.get_type_title() == expected_type_title, f"expected_type_title-{expected_type_title}"

    subject = GeneratorString().get_unique_string()
    description = GeneratorString().get_unique_string()

    new_work_pkg_page.type_subject_input(subject)
    new_work_pkg_page.type_description_input(description)

    new_work_pkg_page.click_save_btn()
    work_pkg_page = controller_pages(new_work_pkg_page)

    current_table_rows += 1
    assert work_pkg_page.get_number_rows_table() == current_table_rows, \
        f"current number of rows should be-'{current_table_rows}'"

    read_row_created = work_pkg_page.get_row_as_dict(current_table_rows)

    assert read_row_created["subject"] == subject, f"subject-'{subject}'"
    assert read_row_created["type"] == "TASK", "The TYPE should be 'TASK'"
