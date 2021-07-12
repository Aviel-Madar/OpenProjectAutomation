from framework.api.work_pkg_api import WorkPkgApi

from generator_string import GeneratorString
from my_config import config


def test_006():
    work_pkg_api = WorkPkgApi()
    work_package_id = config['my_work_package_id']
    new_description = f"update description api {GeneratorString().get_unique_string()}"

    work_pkg_api.get_work_package_by_id(work_package_id)
    payload = {
        "lockVersion": work_pkg_api.response.json["lockVersion"],
        "description": {
            "raw": new_description
        }
    }

    work_pkg_api.update_work_package(work_package_id, payload)

    assert work_pkg_api.response.json["description"]["raw"] == new_description, f"new description-'{new_description}'"
