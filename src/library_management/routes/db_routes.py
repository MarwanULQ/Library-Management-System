from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlmodel import SQLModel, Session, select
from typing import Optional, List
from sqlalchemy import func, sql
from datetime import datetime
from library_management.services.database.db import (
    Book,
    Authors,
    Categories,
    Copy,
    Book_Loan,
    Room_Reservation,
    StaffRole,
    Student,
    Staff,
    Room,
    RoomStatus,
    init_db
)

engine = init_db()
router = APIRouter(prefix="/db")

def get_session():
    with Session(engine) as session:
        yield session

class AuthorRead(SQLModel):
    author_id: int
    full_name: str

class CategoryRead(SQLModel):
    category_id: int
    category_name: str

class BookRead(SQLModel):
    book_id: int
    book_name: str
    isbn: Optional[str]
    publication_year: int
    language: str
    cover: Optional[str]
    authors: List[AuthorRead] = []
    category: List[CategoryRead] = []


@router.get("/books", response_model=list[BookRead])
def list_books(session: Session = Depends(get_session)):
    statement = select(Book)
    results = session.exec(statement).all()
    return results


@router.get("/books/{book_id}", response_model=BookRead)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

class BookCreate(SQLModel):
    book_name: str
    isbn: str | None = None
    publication_year: int
    language: str
    cover: str | None = None

@router.post("/books", response_model=BookRead)
def create_book(data: BookCreate, session: Session = Depends(get_session)):
    book = Book.from_orm(data)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@router.get("/books/search/all", response_model=list[BookRead])
def search(q: str, session: Session = Depends(get_session)):
    q = f"%{q.lower()}%"

    statement = (
        select(Book).distinct()
        .join(Book.authors, isouter=True)
        .join(Book.category, isouter=True)
        .where(
            func.lower(Book.book_name).like(q) |
            func.lower(Book.isbn).like(q) |
            func.lower(Authors.full_name).like(q) |
            func.lower(Categories.category_name).like(q)
        )
    )

    return session.exec(statement).all()

class StudentRead(SQLModel):
    student_id: int
    full_name: str
    email: str

@router.get("/students/{student_id}", response_model=StudentRead)
def get_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

class StudentCreate(SQLModel):
    full_name: str
    email: str

@router.post("/students", response_model=StudentRead)
def create_student(data: StudentCreate, session: Session = Depends(get_session)):
    student = Student.from_orm(data)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

class StaffRead(SQLModel):
    staff_id: int
    full_name: str
    email: str
    role: StaffRole

@router.get("/staff/{staff_id}", response_model=StaffRead)
def get_staff(staff_id: int, session: Session = Depends(get_session)):
    staff = session.get(Staff, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return staff

class StaffCreate(SQLModel):
    full_name: str
    email: str
    role: StaffRole

@router.post("/staff", response_model=StaffRead)
def create_staff(data: StaffCreate, session: Session = Depends(get_session)):
    staff = Staff.from_orm(data)
    session.add(staff)
    session.commit()
    session.refresh(staff)
    return staff


class RoomRead(SQLModel):
    room_id: int
    capacity: int
    floor: int

@router.get("/rooms", response_model=list[RoomRead])
def list_rooms(session: Session = Depends(get_session)):
    statement = select(Room)
    results = session.exec(statement).all()
    return results


@router.get("/rooms/{room_id}", response_model=RoomRead)
def get_room(room_id: int, session: Session = Depends(get_session)):
    room = session.get(Room, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

class ReservationRead(SQLModel):
    reservation_id: int
    student_id: int
    staff_id: int
    room_id: int
    status: RoomStatus
    requested_at: datetime
    approved_at: datetime
    start_time: datetime
    end_time: datetime 

@router.get("/room_reservations", response_model=list[ReservationRead])
def list_reservations(session: Session = Depends(get_session)):
    statement = select(Room_Reservation)
    results = session.exec(statement).all()
    return results

@router.get("/room_reservations/{reservation_id}", response_model=ReservationRead)
def get_reservation(reservation_id: int, session: Session = Depends(get_session)):
    reservation = session.get(Room_Reservation, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

class ReservationCreate(SQLModel):
    student_id: int
    room_id: int
    requested_at: datetime
    start_time: datetime
    end_time: datetime 


@router.post("/room_reservation/{reservation_id}", response_model=ReservationCreate)
def create_reservation(data: ReservationCreate, session: Session = Depends(get_session)):
    reservation = Room_Reservation.from_orm(data)
    session.add(reservation)
    session.commit()
    session.refresh(reservation)
    return reservation

class ReservationUpdate(SQLModel):
    status: Optional[str] = None
    staff_id: Optional[int] = None
    approved_at: Optional[datetime] = None

@router.patch("/room_reservation/{reservation_id}", response_model=ReservationRead)
def update_reservation(
    reservation_id: int,
    data: ReservationUpdate,
    session: Session = Depends(get_session)
):
    reservation = session.get(Room_Reservation, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(reservation, key, value)

    session.add(reservation)
    session.commit()
    session.refresh(reservation)
    return reservation

