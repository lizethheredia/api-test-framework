import pytest

from src.api.auth_client import AuthClient
from src.api.booking_client import BookingClient

@pytest.fixture(scope="session")
def token():
    return AuthClient().get_token()

@pytest.fixture(scope="session")
def booking_client(token):
    return BookingClient(token)

@pytest.fixture
def booking_payload():
    return {
        "firstname": "Liz",
        "lastname": "Heredia",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        "additionalneeds": "Breakfast"
    }
