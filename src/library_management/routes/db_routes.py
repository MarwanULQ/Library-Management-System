from fastapi import  Depends, HTTPException, APIRouter, Request
from sqlmodel import SQLModel, Session, select
from typing import Optional, List
from sqlalchemy import func
from datetime import datetime
from zoneinfo import ZoneInfo
from ..services.database.db import (
    Book,
    Authors,
    Categories,
    Copy,
    Book_Loan,
    LoanStatus,
    CopyStatus,
    Room_Reservation,
    StaffRole,
    Student,
    Staff,
    Rooms,
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

class BookCreate(SQLModel):
    book_name: str
    isbn: str | None = None
    publication_year: int
    language: str
    cover: str | None = None


@router.post("/authors", response_model=AuthorRead)
def create_author(name: str, session: Session = Depends(get_session)):
    author = Authors(full_name=name) 
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

@router.get("/authors", response_model=list[AuthorRead])
def list_authors(session: Session = Depends(get_session)):
    authors = session.exec(select(Authors)).all()
    return authors


@router.post("/categories", response_model=CategoryRead)
def create_category(name: str, session: Session = Depends(get_session)):
    category = Categories(category_name=name)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

@router.get("/catagories", response_model=list[CategoryRead])
def list_categories(session: Session=Depends(get_session)):
    categories =  session.exec(select(Categories)).all()
    return categories


@router.get("/books", response_model=list[BookRead])
def list_books(request: Request, session: Session = Depends(get_session)):
    base = str(request.base_url).rstrip("/")
    books = session.exec(select(Book)).all()

    for book in books:
        if book.cover:
            book.cover = f"{base}/covers/{book.cover}"
    return books


@router.get("/books/{book_id}", response_model=BookRead)
def get_book(book_id: int, request: Request, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    base = str(request.base_url).rstrip("/")

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.cover:
        book.cover = f"{base}/covers/{book.cover}"

    return book

@router.post("/books", response_model=BookRead)
def create_book(data: BookCreate, session: Session = Depends(get_session)):
    book = Book.model_validate(data)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@router.get("/books/search/all", response_model=list[BookRead])
def search(q: str,request: Request, session: Session = Depends(get_session)):
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

    books = session.exec(statement).all()
    base = str(request.base_url).rstrip("/")

    for book in books:
        if book.cover:
            book.cover = f"{base}/covers/{book.cover}"

    return books

@router.patch("/books/{book_id}/authors/{author_id}")
def add_author_to_book(book_id: int, author_id: int, session: Session=Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException("Error 404: Book not found")
    author = session.get(Authors, author_id)
    if not author:
        raise HTTPException("Error 404: Author not found")

    if author in book.authors:
        return {"Status: author already exists in book"}
    
    book.authors.append(author)
    session.add(book)
    session.commit()
    session.refresh(book)
    return {"Operation Successful: Author added to book"}

@router.patch("/books/{book_id}/categories/{category_id}")
def add_category_to_book(book_id: int, category_id: int, session: Session=Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException("Error 404: Book not found")
    category = session.get(Categories, category_id)
    if not category:
        raise HTTPException("Error 404: Category not found")

    if category in book.category:
        return {"Status: Category already in book"}

    book.category.append(category)
    session.add(book)
    session.commit()
    session.refresh(book)
    return {"Operation Successful: Category added to book"}

@router.post("/copies")
def create_copy(book_id: int, session: Session = Depends(get_session)):
    copy = Copy(book_id=book_id, status=CopyStatus.Available)
    session.add(copy)
    session.commit()
    session.refresh(copy)
    return copy

class LoanRead(SQLModel):
    loan_id: int
    student_id: int
    copy_id: int
    staff_id: int | None
    status: LoanStatus 
    created_at: datetime
    approved_at: datetime | None
    returned_at: datetime | None

@router.get("/loans", response_model=list[LoanRead])
def list_loans(session: Session = Depends(get_session)):
    loans = session.exec(select(Book_Loan)).all()
    return loans

@router.post("/loans", response_model=LoanRead)
def create_loan(book_id: int, student_id: int, session: Session = Depends(get_session)):
    copy = session.exec(select(Copy).where(
        (Copy.book_id == book_id) &
        (Copy.status == "Available")
    )).first()

    if not copy:
        raise HTTPException("Error 400: No Available copies")
    #copy.status = "Loaned"
    #session.add(copy)

    loan = Book_Loan(
        student_id= student_id,
        copy_id= copy.copy_id,
        created_at=datetime.now(ZoneInfo("Africa/Cairo"))
    )
    session.add(loan)

    session.commit()
    session.refresh(loan)

    return loan


@router.patch("/loans/{loan_id}/accept", response_model=LoanRead)
def accept_loan(loan_id: int, session: Session = Depends(get_session)):
    loan = session.get(Book_Loan, loan_id)

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    if loan.status != LoanStatus.Pending:
        raise HTTPException(
            status_code=409,
            detail=f"Cannot accept a loan in '{loan.status}' state"
        )

    copy = session.get(Copy, loan.copy_id)
    if copy.status != CopyStatus.Available:
        raise HTTPException(
            status_code=409,
            detail="Copy is no longer available"
        )

    # update states
    loan.status = LoanStatus.Active
    loan.approved_at = datetime.now(ZoneInfo("Africa/Cairo"))
    copy.status = CopyStatus.Loaned

    session.add_all([loan, copy])
    session.commit()
    session.refresh(loan)

    return loan

@router.patch("/loans/{loan_id}/reject", response_model=LoanRead)
def reject_loan(loan_id: int, session: Session = Depends(get_session)):
    loan = session.get(Book_Loan, loan_id)

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    if loan.status != LoanStatus.Pending:
        raise HTTPException(
            status_code=409,
            detail=f"Cannot reject a loan in '{loan.status}' state"
        )

    loan.status = LoanStatus.Rejected
    session.add(loan)
    session.commit()
    session.refresh(loan)

    return loan

@router.patch("/loans/{loan_id}/return", response_model=LoanRead)
def return_loan(loan_id: int, session: Session = Depends(get_session)):
    loan = session.get(Book_Loan, loan_id)

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    if loan.status != LoanStatus.Active:
        raise HTTPException(
            status_code=409,
            detail=f"Cannot reject a loan in '{loan.status}' state"
        )

    copy = session.get(Copy, loan.copy_id)

    loan.status = LoanStatus.Returned
    copy.status = CopyStatus.Available

    session.add_all([loan, copy])
    session.commit()
    session.refresh(loan)
    return loan
    


class StudentModel(SQLModel):
    student_id: int
    full_name: str
    email: str

@router.get("/students/{student_id}", response_model=StudentModel)
def get_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/students", response_model=StudentModel)
def create_student(data: StudentModel, session: Session = Depends(get_session)):
    student = Student.model_validate(data)
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
    staff = Staff.model_validate(data)
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
    statement = select(Rooms)
    results = session.exec(statement).all()
    return results


@router.get("/rooms/{room_id}", response_model=RoomRead)
def get_room(room_id: int, session: Session = Depends(get_session)):
    room = session.get(Rooms, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

class RoomCreate(SQLModel):
    capacity: int
    floor: int

#Added the ability to create rooms for testing
@router.post("/rooms", response_model=RoomRead)
def create_room(data: RoomCreate, session: Session = Depends(get_session)):
    room = Rooms.model_validate(data)
    session.add(room)
    session.commit()
    session.refresh(room)
    return room

class ReservationRead(SQLModel):
    reservation_id: int
    student_id: int
    staff_id: int | None
    room_id: int
    status: RoomStatus
    requested_at: datetime
    approved_at: datetime | None
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


@router.post("/room_reservation", response_model=ReservationCreate)
def create_reservation(data: ReservationCreate, session: Session = Depends(get_session)):
    reservation = Room_Reservation.model_validate(data)
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

