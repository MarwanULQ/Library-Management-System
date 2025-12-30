import unittest
from unittest.mock import patch, MagicMock
from services.frontend.auth_service import AuthService
from services.frontend.books_service import BooksService
from services.frontend.room_reservation_service import RoomReservationService
from models.room_reservation_model import RoomStatus


class TestFrontendServices(unittest.TestCase):

    @patch('services.frontend.api_helper.ApiHelper.post')
    def test_login_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"userId": 1, "role": "Admin"}
        mock_post.return_value = mock_response

        user_id, role = AuthService.login("test@test.com", "password123")

        self.assertEqual(user_id, 1)
        self.assertEqual(role, "Admin")
        mock_post.assert_called_once()

    @patch('services.frontend.api_helper.ApiHelper.post')
    def test_login_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"detail": "Invalid credentials"}
        mock_post.return_value = mock_response

        with self.assertRaises(Exception) as context:
            AuthService.login("wrong@test.com", "wrong")

        self.assertIn("Login failed", str(context.exception))

    @patch('services.frontend.api_helper.ApiHelper.get')
    def test_get_all_books(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "book_id": 1,
                "book_name": "Python Clean Code",
                "publication_year": 2022,
                "language": "EN"
            }
        ]
        mock_get.return_value = mock_response

        books = BooksService.get_all_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].book_name, "Python Clean Code")

    @patch('services.frontend.api_helper.ApiHelper.patch')
    def test_update_room_reservation(self, mock_patch):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "reservation_id": 10,
            "status": "Approved",
            "student_id": 1,
            "room_id": 5,
            "requested_at": "2023-01-01T10:00:00",
            "start_time": "2023-01-01T12:00:00",
            "end_time": "2023-01-01T14:00:00"
        }
        mock_patch.return_value = mock_response

        result = RoomReservationService.update_room_reservation(
            10,
            status=RoomStatus.Approved
        )

        self.assertEqual(result.status, "Approved")
        mock_patch.assert_called()


if __name__ == "__main__":
    unittest.main()
