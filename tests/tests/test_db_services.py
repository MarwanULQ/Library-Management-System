import pytest
from sqlmodel import Session, SQLModel, create_engine, select
from src.library_management.services.database.db import Book, Student, Categories

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_and_read_book(session: Session):
    new_book = Book(
        book_name="Mastering Python",
        publication_year=2024,
        language="Arabic"
    )
    session.add(new_book)
    session.commit()

    statement = select(Book).where(Book.book_name == "Mastering Python")
    result = session.exec(statement).first()

    assert result is not None
    assert result.book_name == "Mastering Python"
    assert result.language == "Arabic"

def test_create_student(session: Session):
    student = Student(
        full_name="Ali Khamis",
        email="ali@test.com"
    )
    session.add(student)
    session.commit()

    statement = select(Student).where(Student.email == "ali@test.com")
    db_student = session.exec(statement).first()

    assert db_student.full_name == "Ali Khamis"

def test_create_category(session: Session):
    cat = Categories(category_name="Computer Science")
    session.add(cat)
    session.commit()

    assert cat.category_id is not None
