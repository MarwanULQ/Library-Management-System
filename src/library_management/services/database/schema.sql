PRAGMA foreign_keys = ON;

-- =====================
-- Book
-- =====================
CREATE TABLE Book (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT NOT NULL,
    isbn TEXT UNIQUE,
    publication_year INTEGER NOT NULL,
    language TEXT NOT NULL,
    cover TEXT
);

-- =====================
-- Authors
-- =====================
CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER,
    nationality TEXT
);

-- =====================
-- Categories
-- =====================
CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL
);

-- =====================
-- Staff
-- =====================
CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('Librarian', 'Admin')),
    email TEXT NOT NULL UNIQUE
);

-- =====================
-- Student
-- =====================
CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- =====================
-- Copy
-- =====================
CREATE TABLE Copy (
    copy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'Available'
        CHECK (status IN ('Available','Loaned')),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

-- =====================
-- Book ↔ Authors (M:N)
-- =====================
CREATE TABLE Book_Authors (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- =====================
-- Book ↔ Categories (M:N)
-- =====================
CREATE TABLE Book_Category (
    book_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- =====================
-- Book Loan
-- =====================
CREATE TABLE Book_Loan (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    copy_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    staff_id INTEGER,
    status TEXT NOT NULL DEFAULT 'Pending'
        CHECK (status IN ('Pending','Rejected','Active','Returned')),
    created_at TEXT NOT NULL,
    approved_at TEXT,
    returned_at TEXT,
    FOREIGN KEY (copy_id) REFERENCES Copy(copy_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);


-- =====================
-- Rooms
-- =====================
CREATE TABLE Rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    capacity INTEGER NOT NULL,
    floor INTEGER NOT NULL
);

-- =====================
-- Room Reservation
-- =====================
CREATE TABLE Room_Reservation (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    staff_id INTEGER,
    status TEXT NOT NULL DEFAULT 'Pending'
        CHECK (status IN ('Pending','Approved','Rejected','Active','Finished')),
    requested_at TEXT NOT NULL,
    approved_at TEXT,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

-- =====================
-- Auth Users
-- =====================
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TEXT
)
