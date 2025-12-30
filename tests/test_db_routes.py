import pytest
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

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

def test_create_book(client: TestClient):
    response = client.post(
        "/db/books",
        json={
            "book_name": "Test Book",
            "isbn": "123456789",
            "publication_year": 2023,
            "language": "Arabic"
        },
    )
    data = response.json()
    assert response.status_code == 200
    assert data["book_name"] == "Test Book"
    assert "book_id" in data

def test_list_books(client: TestClient):
    client.post(
        "/db/books",
        json={
            "book_name": "Book 1",
            "publication_year": 2020,
            "language": "EN"
        }
    )

    response = client.get("/db/books")
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1

def test_search_book(client: TestClient):
    client.post(
        "/db/books",
        json={
            "book_name": "Python Mastery",
            "publication_year": 2021,
            "language": "EN"
        }
    )

    response = client.get("/db/books/search/all?q=Python")
    data = response.json()
    assert response.status_code == 200
    assert any(book["book_name"] == "Python Mastery" for book in data)

def test_create_student(client: TestClient):
    response = client.post(
        "/db/students",
        json={
            "student_id": 1,
            "full_name": "Ali Khamis",
            "email": "ali@example.com"
        }
    )
    assert response.status_code == 200
    assert response.json()["full_name"] == "Ali Khamis"
