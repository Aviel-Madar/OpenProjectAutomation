import requests
from requests.auth import HTTPBasicAuth

from my_config import config

base_url = config['base_url']


class BasicAuth:
    def __init__(self):
        self.my_auth = HTTPBasicAuth(config['my_auth']['name'], config['my_auth']['api_key'])


class RestClient:
    def __init__(self):
        self.base_url = base_url
        self.basic_auth = BasicAuth().my_auth

    def get(self, path):
        url = self.base_url + path
        response = requests.get(url, auth=self.basic_auth, headers={'Content-Type': 'application/json'})
        return response

    def post(self, path, payload):
        url = self.base_url + path
        response = requests.post(url, json=payload, auth=self.basic_auth)
        return response

    def put(self, path, payload):
        url = self.base_url + path
        response = requests.put(url, json=payload, auth=self.basic_auth)
        return response

    def patch(self, path, payload):
        url = self.base_url + path
        response = requests.patch(url, json=payload, auth=self.basic_auth)
        return response

    def delete(self, path):
        url = self.base_url + path
        response = requests.delete(url, auth=self.basic_auth, headers={'Content-Type': 'application/json'})
        return response
