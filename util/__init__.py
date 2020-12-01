import requests
import json


class Request:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }

    def post(self, route, data):
        try:
            requests.post(url=self.url + route, data=json.dumps(
                data), headers=self.headers)

        except:
            return False

    def get(self, route):
        try:
            return requests.get(url=self.url + route, headers=self.headers)
        except:
            return False
