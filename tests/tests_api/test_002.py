from datetime import datetime

from framework.api.projects_api import ProjectsApi


def test_002():
    project_api = ProjectsApi()
    project_id = 3
    new_description = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    payload = {
        "description": {
            "raw": new_description
        }
    }

    project_api.update_project(project_id, payload)

    assert project_api.response.json["description"]["raw"] == new_description, f"new description-'{new_description}'"
