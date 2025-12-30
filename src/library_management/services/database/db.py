from datetime import datetime
import sqlite3
from enum import Enum
from pathlib import Path
from pydantic.types import T
from sqlalchemy import engine
from sqlalchemy.engine.base import OptionEngine
from sqlmodel import Relationship, SQLModel, create_engine, Field, table
from typing import Optional

root = Path(__file__).resolve().parent.parent.parent.parent.parent
db_dir = root / "data"
db = db_dir / "library.db"
schema_path = root / "src" / "library_management" / "services" / "database" / "schema.sql"

def get_db():
    return sqlite3.connect(db)

def init_db():
    # Makes the db directory 
    # exists_ok is True to make sure the function does not panic if directory already exists 
    db_dir.mkdir(exist_ok=True)

    # Checks if the db already exists
    db_exist = db.exists()

    # connect to the db and creates it first if needed
    engine = create_engine(
        f"sqlite:///{db}",
        echo=True,
        connect_args={"check_same_thread": False}
    )

    # if the db did not exists before connecting -> excute the schema
    if not db_exist:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema_sql = f.read()

        statements = [
            stmt.strip()
            for stmt in schema_sql.split(";")
            if stmt.strip()
        ]

        with engine.begin() as conn:
            conn.exec_driver_sql("PRAGMA foreign_keys = ON;")
            for stmt in statements:
                conn.exec_driver_sql(stmt)
    return engine



#Relationship tables
class Book_Authors(SQLModel, table=True):
    __tablename__ = "Book_Authors"
    book_id: int = Field(foreign_key="Book.book_id", primary_key=True)
    author_id: int = Field(foreign_key="Authors.author_id", primary_key=True)

class Book_Category(SQLModel, table=True):
    __tablename__ = "Book_Category"

    book_id: int = Field(foreign_key="Book.book_id", primary_key=True)
    category_id: int = Field(foreign_key="Categories.category_id", primary_key=True)

class Copy_Loan(SQLModel, table=True):
    __tablename__ = "Copy_Loan"
    copy_id: int = Field(foreign_key="Copy.copy_id", primary_key=True)
    loan_id: int = Field(foreign_key="Book_Loan.loan_id", primary_key=True)

class Book(SQLModel, table=True):
    __tablename__ = "Book"
    # Defining columns and their data types
    # Optional[int] basicaaly means that if you don't give it a value it will auto increment
    book_id: Optional[int] = Field(default=None, primary_key=True)
    book_name: str
    isbn: Optional[str] = Field(default=None)
    publication_year: int
    language: str
    cover: Optional[str] = Field(default=None)

    # This creates an attribute for authors by getting it from the relationship table
    authors: list["Authors"] = Relationship(
        back_populates="books",
        link_model=Book_Authors
    )

    category: list["Categories"] = Relationship(
        back_populates="books",
        link_model=Book_Category
    )

class Authors(SQLModel, table=True):
    __tablename__ = "Authors"
    author_id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    birth_year: Optional[int] = Field(default=None)
    nationality: Optional[str] = None

    books: list[Book] = Relationship(
        back_populates="authors",
        link_model=Book_Authors
    )

class Categories(SQLModel, table=True):
    __tablename__ = "Categories"
    category_id: Optional[int] = Field(default=None, primary_key=True)
    category_name: str

    books: list[Book] = Relationship(
        back_populates="category",
        link_model=Book_Category
    )


class StaffRole(str, Enum):
    Librarian = "Librarian"
    Admin = "Admin"

class Staff(SQLModel, table=True):
    __tablename__ = "Staff"
    staff_id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    role: StaffRole
    email: str = Field(unique=True)

class Student(SQLModel, table=True):
    __tablename__ = "Student"
    student_id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(unique=True)

class CopyStatus(str, Enum):
    Available = "Available"
    Loaned = "Loaned"

class Copy(SQLModel, table=True):
    __tablename__ = "Copy"
    copy_id: Optional[int] = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="Book.book_id")
    status: CopyStatus
    loans: list["Book_Loan"] = Relationship(back_populates="copy")

class LoanStatus(str, Enum):
    Pending = "Pending"
    Rejected = "Rejected"
    Active = "Active"
    Returned = "Returned"

class Book_Loan(SQLModel, table=True):
    __tablename__ = "Book_Loan"
    loan_id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="Student.student_id")
    copy_id: int = Field(foreign_key="Copy.copy_id")
    staff_id: Optional[int] = Field(default=None,foreign_key="Staff.staff_id")
    status: Optional[LoanStatus] = Field(default="Pending")
    created_at: datetime
    approved_at: Optional[datetime] = Field(default=None)
    returned_at: Optional[datetime] = Field(default=None)
    copy: "Copy" = Relationship(back_populates="loans")


class Rooms(SQLModel, table=True):
    __tablename__ = "Rooms"
    room_id: Optional[int] = Field(default=None, primary_key=True)
    capacity: int
    floor: int

class RoomStatus(str, Enum):
    Pending = "Pending"
    Approved = "Approved"
    Rejected = "Rejected"
    Active = "Active"
    Finished = "Finished"
    
class Room_Reservation(SQLModel, table=True):
    __tablename__ = "Room_Reservation"
    reservation_id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="Student.student_id")
    staff_id: Optional[int] = Field(default=None, foreign_key="Staff.staff_id")
    room_id: int = Field(foreign_key="Rooms.room_id")
    status: RoomStatus = Field(default=RoomStatus.Pending)
    requested_at: datetime
    approved_at: Optional[datetime] = Field(default=None)
    start_time: datetime
    end_time: datetime
