import pytest

class TestGetBooking:

    def test_get_all_bookings_returns_200(self, booking_client):
        """GET /booking should return 200"""
        response = booking_client.get_all_bookings()
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_get_all_bookings_returns_list(self, booking_client):
        """GET /booking should return a list"""
        response = booking_client.get_all_bookings()
        assert isinstance(response.json(), list), "Response should be a list"

    def test_get_all_bookings_not_empty(self, booking_client):
        """GET /booking should return at least one booking"""
        response = booking_client.get_all_bookings()
        assert len(response.json()) > 0, "Booking list should not be empty"

    def test_get_all_bookings_contain_ids(self, booking_client):
        """Each item in list should have a bookingid"""
        response = booking_client.get_all_bookings()
        for item in response.json():
            assert "bookingid" in item, f"Missing bookingid in item: {item}"

    def test_get_specific_booking_returns_200(self, booking_client, booking_payload):
        """GET /booking/{id} should return 200 for existing booking"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.get_booking(booking_id)
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_get_specific_booking_firstname(self, booking_client, booking_payload):
        """GET /booking/{id} should return correct firstname"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.get_booking(booking_id)
        assert response.json()["firstname"] == booking_payload["firstname"]

    def test_get_specific_booking_totalprice(self, booking_client, booking_payload):
        """GET /booking/{id} should return correct totalprice"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.get_booking(booking_id)
        assert response.json()["totalprice"] == booking_payload["totalprice"]

    def test_get_nonexistent_booking_returns_404(self, booking_client):
        """GET /booking/{id} should return 404 for nonexistent booking"""
        response = booking_client.get_booking(999999)
        assert response.status_code == 404, \
            f"Expected 404 but got {response.status_code}"