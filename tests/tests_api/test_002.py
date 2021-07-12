from framework.api.projects_api import ProjectsApi
from generator_string import GeneratorString

from my_config import config


def test_002():
    project_api = ProjectsApi()
    project_id = config['my_project_id']
    new_description = GeneratorString().get_unique_string()
    payload = {
        "description": {
            "raw": new_description
        }
    }

    project_api.update_project(project_id, payload)

    assert project_api.response.json["description"]["raw"] == new_description, f"new description-'{new_description}'"
