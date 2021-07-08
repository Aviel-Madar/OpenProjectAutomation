from infra.rest_client import RestClient
import collections

RESPONSE = collections.namedtuple('Response', ['status_code', 'json'])


class WorkPkgApi(RestClient):
    packages_path = '/api/v3/work_packages'

    def __init__(self):
        super().__init__()
        self.response = None

    def get_work_package_by_id(self, packages_id):
        current_response = self.get(f"{self.packages_path}/{packages_id}")
        self.response = RESPONSE(current_response.status_code, current_response.json())

    def update_work_package(self, packages_id, payload):
        current_response = self.patch(f"{self.packages_path}/{packages_id}", payload)
        self.response = RESPONSE(current_response.status_code, current_response.json())

    def create_work_package(self, payload):
        current_response = self.post(self.packages_path, payload)
        self.response = RESPONSE(current_response.status_code, current_response.json())

    def delete_work_package(self, packages_id):
        current_response = self.delete(f"{self.packages_path}/{packages_id}")
        self.response = RESPONSE(current_response.status_code, None)
