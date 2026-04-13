import requests
from config.config import BASE_URL, USERNAME, PASSWORD

class AuthClient:
    def get_token(self):
        payload = {
            "username": USERNAME,
            "password": PASSWORD
        }
        response = requests.post(f"{BASE_URL}/auth", json=payload)
        return response.json()["token"]