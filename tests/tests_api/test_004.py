import time
from datetime import datetime

from framework.api.projects_api import ProjectsApi


def test_004():
    project_api = ProjectsApi()
    project_name = f"new project {datetime.now().strftime('%d/%m/%Y-%H:%M:%S')}"
    project_identifier = f"newIdentifier{datetime.now().strftime('%d%m%Y%H%M%S')}"
    payload = {
        "name": project_name,
        "identifier": project_identifier
    }

    project_api.create_project(payload)

    new_project_id = project_api.response.json["id"]

    project_api.delete_project(new_project_id)
    time.sleep(4)

    expected_resp_code = 404
    project_api.get_project_by_id(new_project_id)

    assert project_api.response.status_code == expected_resp_code, f"expected response code-'{expected_resp_code}'"
