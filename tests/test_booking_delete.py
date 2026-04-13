import pytest

class TestDeleteBooking:

    def test_delete_booking_returns_201(self, booking_client, booking_payload):
        """DELETE /booking/{id} should return 201"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        response = booking_client.delete_booking(booking_id)
        assert response.status_code == 201, \
            f"Expected 201 but got {response.status_code}"

    def test_delete_booking_not_found_after(self, booking_client, booking_payload):
        """Deleted booking should return 404 on GET"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        booking_client.delete_booking(booking_id)
        response = booking_client.get_booking(booking_id)
        assert response.status_code == 404, \
            f"Expected 404 after deletion but got {response.status_code}"

    def test_delete_nonexistent_booking(self, booking_client):
        """DELETE /booking/{id} on nonexistent id should return 405"""
        response = booking_client.delete_booking(999999)
        assert response.status_code == 405, \
            f"Expected 405 but got {response.status_code}"

    def test_delete_same_booking_twice(self, booking_client, booking_payload):
        """Deleting the same booking twice should return 405 on second attempt"""
        created = booking_client.create_booking(booking_payload)
        booking_id = created.json()["bookingid"]

        booking_client.delete_booking(booking_id)
        response = booking_client.delete_booking(booking_id)
        assert response.status_code == 405, \
            f"Expected 405 on second delete but got {response.status_code}"
        