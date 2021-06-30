import requests
from requests.auth import HTTPBasicAuth

import main

my_auth = HTTPBasicAuth(main.config.my_auth['name'], ['api_key'])


class RestClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path):
        pass

    def post(self, path):
        pass

    def put(self, path):
        pass

    def patch(self, path):
        pass

    def delete(self, path):
        pass
