import unittest
from sqlmodel import Session, SQLModel, create_engine, select
from src.library_management.services.database.db import Book, Student, Categories


class TestDatabaseModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite:///:memory:")
        SQLModel.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        SQLModel.metadata.drop_all(cls.engine)

    def setUp(self):
        self.session = Session(self.engine)

    def tearDown(self):
        self.session.close()

    def test_create_and_read_book(self):
        new_book = Book(
            book_name="Mastering Python",
            publication_year=2024,
            language="Arabic"
        )
        self.session.add(new_book)
        self.session.commit()

        statement = select(Book).where(Book.book_name == "Mastering Python")
        result = self.session.exec(statement).first()

        self.assertIsNotNone(result)
        self.assertEqual(result.book_name, "Mastering Python")
        self.assertEqual(result.language, "Arabic")

    def test_create_student(self):
        student = Student(
            full_name="Ali Khamis",
            email="ali@test.com"
        )
        self.session.add(student)
        self.session.commit()

        statement = select(Student).where(Student.email == "ali@test.com")
        db_student = self.session.exec(statement).first()

        self.assertEqual(db_student.full_name, "Ali Khamis")

    def test_create_category(self):
        cat = Categories(category_name="Computer Science")
        self.session.add(cat)
        self.session.commit()

        self.assertIsNotNone(cat.category_id)


if __name__ == "__main__":
    unittest.main()
