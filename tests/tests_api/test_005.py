from framework.api.work_pkg_api import WorkPkgApi


def test_005():
    work_pkg_api = WorkPkgApi()
    work_package_id = 34

    expected_resp_code = 200
    expected_type = "Task"
    expected_subject = "My Task 1"

    work_pkg_api.get_work_package_by_id(work_package_id)

    assert work_pkg_api.response.status_code == expected_resp_code, f"expected response code-'{expected_resp_code}'"
    assert work_pkg_api.response.json["_embedded"]["type"]["name"] == expected_type, f"expected type-'{expected_type}'"
    assert work_pkg_api.response.json["subject"] == expected_subject, f"expected subject-'{expected_subject}'"
