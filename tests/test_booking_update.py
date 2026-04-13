import pytest

class TestUpdateBooking:

    def test_full_update_returns_200(self, booking_client, booking_payload):
        """PUT /booking/{id} should return 200"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        updated_payload = {
            "firstname": "Jane",
            "lastname": "Doe",
            "totalprice": 200,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2026-02-01",
                "checkout": "2026-02-10"
            },
            "additionalneeds": "Lunch"
        }
        response = booking_client.update_booking(booking_id, updated_payload)
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_full_update_firstname(self, booking_client, booking_payload):
        """PUT /booking/{id} should update firstname"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        updated_payload = {**booking_payload, "firstname": "Jane"}
        response = booking_client.update_booking(booking_id, updated_payload)
        assert response.json()["firstname"] == "Jane"

    def test_full_update_totalprice(self, booking_client, booking_payload):
        """PUT /booking/{id} should update totalprice"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        updated_payload = {**booking_payload, "totalprice": 999}
        response = booking_client.update_booking(booking_id, updated_payload)
        assert response.json()["totalprice"] == 999

    def test_full_update_dates(self, booking_client, booking_payload):
        """PUT /booking/{id} should update booking dates"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        updated_payload = {
            **booking_payload,
            "bookingdates": {
                "checkin": "2026-06-01",
                "checkout": "2026-06-10"
            }
        }
        response = booking_client.update_booking(booking_id, updated_payload)
        assert response.json()["bookingdates"]["checkin"] == "2026-06-01"
        assert response.json()["bookingdates"]["checkout"] == "2026-06-10"

    def test_partial_update_returns_200(self, booking_client, booking_payload):
        """PATCH /booking/{id} should return 200"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.partial_update_booking(
            booking_id, {"firstname": "Updated"}
        )
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_partial_update_firstname(self, booking_client, booking_payload):
        """PATCH /booking/{id} should update only firstname"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.partial_update_booking(
            booking_id, {"firstname": "Patched"}
        )
        assert response.json()["firstname"] == "Patched"

    def test_partial_update_preserves_other_fields(self, booking_client, booking_payload):
        """PATCH /booking/{id} should not modify other fields"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.partial_update_booking(
            booking_id, {"firstname": "Patched"}
        )
        assert response.json()["lastname"] == booking_payload["lastname"]
        assert response.json()["totalprice"] == booking_payload["totalprice"]