from datetime import datetime

from framework.api.work_pkg_api import WorkPkgApi


def test_007():
    work_pkg_api = WorkPkgApi()
    work_subject = f"new project {datetime.now().strftime('%d/%m/%Y-%H:%M:%S')}"

    href_to_project_id = "/api/v3/projects/3"
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
