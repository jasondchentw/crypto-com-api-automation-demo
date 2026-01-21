import requests

class RestClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def public_post(self, method: str, params: dict):
        payload = {
            "method": method,
            "params": params,
            "id": 123456,
            "api_key": ""  # public 不需要
        }
        response = requests.post(f"{self.base_url}/public", json=payload)
        response.raise_for_status()
        return response.json()