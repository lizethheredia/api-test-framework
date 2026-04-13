import pytest

class TestCreateBooking:

    def test_create_booking_returns_200(self, booking_client, booking_payload):
        """POST /booking should return 200"""
        response = booking_client.create_booking(booking_payload)
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_create_booking_returns_id(self, booking_client, booking_payload):
        """Response should contain a bookingid"""
        response = booking_client.create_booking(booking_payload)
        data = response.json()
        assert "bookingid" in data, "Response missing bookingid field"
        assert isinstance(data["bookingid"], int), "bookingid should be an integer"

    def test_create_booking_firstname(self, booking_client, booking_payload):
        """Created booking should have correct firstname"""
        response = booking_client.create_booking(booking_payload)
        assert response.json()["booking"]["firstname"] == booking_payload["firstname"]

    def test_create_booking_lastname(self, booking_client, booking_payload):
        """Created booking should have correct lastname"""
        response = booking_client.create_booking(booking_payload)
        assert response.json()["booking"]["lastname"] == booking_payload["lastname"]

    def test_create_booking_totalprice(self, booking_client, booking_payload):
        """Created booking should have correct totalprice"""
        response = booking_client.create_booking(booking_payload)
        assert response.json()["booking"]["totalprice"] == booking_payload["totalprice"]

    def test_create_booking_depositpaid(self, booking_client, booking_payload):
        """Created booking should have correct depositpaid"""
        response = booking_client.create_booking(booking_payload)
        assert response.json()["booking"]["depositpaid"] == booking_payload["depositpaid"]

    def test_create_booking_dates(self, booking_client, booking_payload):
        """Created booking should have correct checkin and checkout dates"""
        response = booking_client.create_booking(booking_payload)
        booking = response.json()["booking"]
        assert booking["bookingdates"]["checkin"] == booking_payload["bookingdates"]["checkin"]
        assert booking["bookingdates"]["checkout"] == booking_payload["bookingdates"]["checkout"]

    def test_create_booking_additional_needs(self, booking_client, booking_payload):
        """Created booking should have correct additionalneeds"""
        response = booking_client.create_booking(booking_payload)
        assert response.json()["booking"]["additionalneeds"] == booking_payload["additionalneeds"]