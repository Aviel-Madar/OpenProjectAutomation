from framework.api.projects_api import ProjectsApi

from generator_string import GeneratorString


def test_003():
    project_api = ProjectsApi()
    project_name = f"project created api {GeneratorString().get_unique_string()}"
    project_identifier = f"new_identifier{GeneratorString().get_unique_string()}"
    payload = {
        "name": project_name,
        "identifier": project_identifier
    }

    project_api.create_project(payload)

    assert project_api.response.json["name"] == project_name, f"new project name-'{project_name}'"
    assert project_api.response.json["identifier"] == project_identifier, f"new project identifier-{project_identifier}"
