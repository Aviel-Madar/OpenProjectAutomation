import time

from framework.api.projects_api import ProjectsApi

from generator_string import GeneratorString


def test_004():
    project_api = ProjectsApi()
    project_name = f"project created api {GeneratorString().get_unique_string()}"
    project_identifier = f"new_identifier{GeneratorString().get_unique_string()}"
    payload = {
        "name": project_name,
        "identifier": project_identifier
    }

    project_api.create_project(payload)

    time.sleep(2)
    new_project_id = project_api.response.json["id"]

    project_api.delete_project(new_project_id)
    time.sleep(4)

    expected_resp_code = 404
    project_api.get_project_by_id(new_project_id)

    assert project_api.response.status_code == expected_resp_code, f"expected response code-'{expected_resp_code}'"
