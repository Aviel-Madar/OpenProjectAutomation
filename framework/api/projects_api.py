from infra.rest_client import RestClient
import collections

RESPONSE = collections.namedtuple('Response', ['status_code', 'json'])


class ProjectsApi(RestClient):
    project_path = '/api/v3/projects'

    def __init__(self):
        super().__init__()
        self.response = None

    def get_project_by_id(self, project_id):
        current_response = self.get(f"{self.project_path}/{project_id}")
        self.response = RESPONSE(current_response.status_code, current_response.json())

    def update_project(self, project_id, payload):
        current_response = self.patch(f"{self.project_path}/{project_id}", payload)
        self.response = RESPONSE(current_response.status_code, current_response.json())

    def create_project(self, payload):
        current_response = self.post(self.project_path, payload)
        self.response = RESPONSE(current_response.status_code, current_response.json())

    def delete_project(self, project_id):
        current_response = self.delete(f"{self.project_path}/{project_id}")
        self.response = RESPONSE(current_response.status_code, None)
