import requests
from config.config import BASE_URL

class BookingClient:
    def __init__(self, token):
        self.headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        self.base_url = BASE_URL

    def get_all_bookings(self):
        return requests.get(f"{self.base_url}/booking")

    def get_booking(self, booking_id):
        return requests.get(f"{self.base_url}/booking/{booking_id}")

    def create_booking(self, payload):
        return requests.post(
            f"{self.base_url}/booking",
            json=payload,
            headers=self.headers
        )

    def update_booking(self, booking_id, payload):
        return requests.put(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers=self.headers
        )

    def partial_update_booking(self, booking_id, payload):
        return requests.patch(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers=self.headers
        )

    def delete_booking(self, booking_id):
        return requests.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers=self.headers
        )