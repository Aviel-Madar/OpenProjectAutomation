from framework.api.projects_api import ProjectsApi


def test_fake_basic_auth():
    project_api = ProjectsApi()
    project_api.basic_auth.password = 'fake auth'
    project_id = 3

    project_api.get_project_by_id(project_id)

    assert project_api.response.status_code == 401, "Should be 401, no good connection with API services"


def test_001():
    project_api = ProjectsApi()
    project_id = 3

    expected_resp_code = 200
    expected_name = "TestProject1"
    expected_descr = "This is the first test project"

    project_api.get_project_by_id(project_id)

    assert project_api.response.status_code == expected_resp_code, f"expected response code-'{expected_resp_code}'"
    assert project_api.response.json["name"] == expected_name, f"expected name-'{expected_name}'"
    assert project_api.response.json["description"]["raw"] == expected_descr, f"expected description-'{expected_descr}'"
