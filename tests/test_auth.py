import requests
from src.api.auth_client import AuthClient
from config.config import BASE_URL

class TestAuth:

    def test_get_token_success(self):
        token = AuthClient().get_token()
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0

    def test_token_is_string(self):
        token = AuthClient().get_token()
        assert isinstance(token, str)

    def test_invalid_credentials_returns_reason(self):
        response = requests.post(
            f"{BASE_URL}/auth",
            json={"username": "wrong", "password": "wrong"}
        )
        assert response.status_code == 200
        assert "reason" in response.json()

    def test_missing_credentials(self):
        response = requests.post(
            f"{BASE_URL}/auth",
            json={"username": "", "password": ""}
        )
        assert response.status_code == 200
        assert "reason" in response.json()

    def test_auth_endpoint_responds(self):
        response = requests.post(
            f"{BASE_URL}/auth",
            json={"username": "admin", "password": "password123"}
        )
        assert response.status_code == 200