from framework.api.work_pkg_api import WorkPkgApi

from generator_string import GeneratorString
from my_config import config


def test_007():
    work_pkg_api = WorkPkgApi()
    work_subject = f"work pkg created api {GeneratorString().get_unique_string()}"

    href_to_project_id = f"/api/v3/projects/{config['my_project_id']}"
    name_project = "TestProject1"
    payload = {
        "subject": work_subject,
        "_links": {
            "project": {
                "href": href_to_project_id,
                "title": name_project
            },
            "type": {"href": "/api/v3/types/1", "title": "Task"},
            "assignee": {"href": None},
        }
    }

    work_pkg_api.create_work_package(payload)

    assert work_pkg_api.response.json["subject"] == work_subject, f"work subject-'{work_subject}'"
