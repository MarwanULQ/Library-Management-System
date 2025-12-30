import unittest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from src.library_management.main import app
from src.library_management.services.database.db import get_db


sqlite_url = "sqlite://"
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


class TestLibraryAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        SQLModel.metadata.create_all(engine)

    @classmethod
    def tearDownClass(cls):
        SQLModel.metadata.drop_all(engine)

    def setUp(self):
        self.session = Session(engine)

        def get_session_override():
            return self.session

        app.dependency_overrides[get_db] = get_session_override
        self.client = TestClient(app)

    def tearDown(self):
        self.session.close()
        app.dependency_overrides.clear()

    def test_create_book(self):
        response = self.client.post(
            "/db/books",
            json={
                "book_name": "Test Book",
                "isbn": "123456789",
                "publication_year": 2023,
                "language": "Arabic"
            }
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["book_name"], "Test Book")
        self.assertIn("book_id", data)

    def test_list_books(self):
        self.client.post(
            "/db/books",
            json={
                "book_name": "Book 1",
                "publication_year": 2020,
                "language": "EN"
            }
        )

        response = self.client.get("/db/books")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(data), 1)

    def test_search_book(self):
        self.client.post(
            "/db/books",
            json={
                "book_name": "Python Mastery",
                "publication_year": 2021,
                "language": "EN"
            }
        )

        response = self.client.get("/db/books/search/all?q=Python")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            any(book["book_name"] == "Python Mastery" for book in data)
        )

    def test_create_student(self):
        response = self.client.post(
            "/db/students",
            json={
                "student_id": 1,
                "full_name": "Ali Khamis",
                "email": "ali@example.com"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["full_name"], "Ali Khamis")


if __name__ == "__main__":
    unittest.main()
