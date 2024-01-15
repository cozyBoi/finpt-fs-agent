import requests

class request_agent:
    api_key = 0
    params = {}
    def __init__(self, _api_key):
        self.api_key=_api_key
    
    def add_param(self, _key, _value):
        self.params[_key] = _value

    def post(self, url):
        self.params["crtfc_key"] = self.api_key
        return requests.post(url, params=self.params)
    
    def get(self, url):
        self.params["crtfc_key"] = self.api_key
        return requests.get(url, params=self.params)