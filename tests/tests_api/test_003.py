from datetime import datetime

from framework.api.projects_api import ProjectsApi


def test_003():
    project_api = ProjectsApi()
    project_name = f"new project {datetime.now().strftime('%d/%m/%Y-%H:%M:%S')}"
    project_identifier = f"new_identifier{datetime.now().strftime('%d%m%Y%H%M%S')}"
    payload = {
        "name": project_name,
        "identifier": project_identifier
    }

    project_api.create_project(payload)

    assert project_api.response.json["name"] == project_name, f"new project name-'{project_name}'"
    assert project_api.response.json["identifier"] == project_identifier, f"new project identifier-{project_identifier}"
