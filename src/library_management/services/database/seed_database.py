import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta
from pathlib import Path

fake = Faker()

root = Path(__file__).resolve().parent.parent.parent.parent.parent

DB_PATH = root / "data" / "library.db"

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

def insert_many(query, data):
    c.executemany(query, data)
    conn.commit()

print("Seeding database...")

# =========================
# USERS
# =========================
students = []
staff = []

for i in range(30):
    students.append((
        fake.unique.email(),
        "hashed_password",
        datetime.now().isoformat(),
        "Student"
    ))

for i in range(8):
    staff.append((
        fake.unique.email(),
        "hashed_password",
        datetime.now().isoformat(),
        "Staff"
    ))

insert_many("""
INSERT INTO Users (email, password_hash, created_at, role)
VALUES (?, ?, ?, ?)
""", students + staff)

# fetch ids
c.execute("SELECT id, role, email FROM Users")
users = c.fetchall()

student_users = [u for u in users if u[1] == "Student"]
staff_users = [u for u in users if u[1] == "Staff"]

# =========================
# STUDENTS / STAFF
# =========================
student_rows = [(fake.name(), u[2], u[0]) for u in student_users]
staff_rows = [(fake.name(), "Librarian", u[2], u[0]) for u in staff_users]

insert_many("""
INSERT INTO Student (full_name, email, user_id)
VALUES (?, ?, ?)
""", student_rows)

insert_many("""
INSERT INTO Staff (full_name, role, email, user_id)
VALUES (?, ?, ?, ?)
""", staff_rows)

print("Users / Students / Staff done")

# =========================
# REAL BOOKS (YOUR 10)
# =========================
real_books = [
("Voor Jou", "9789026138585", 2012, "Dutch", "1.jpg"),
("Cemetery Boys", "9781250250469", 2020, "English", "2.jpg"),
("The Beginning After The End Vol.10", "9781950912573", 2022, "English", "3.jpg"),
("Star Wars: The Han Solo Adventures", "9780345450553", 1992, "English", "4.jpg"),
("Berserk Deluxe Edition Vol.1", "9781506711980", 2019, "English", "5.jpg"),
("Berserk Vol.1", "9781593070205", 2003, "English", "6.jpg"),
("Harry Potter and The Cursed Child", "9781338216660", 2016, "English", "7.jpg"),
("Atomic Habits", "9780735211292", 2018, "English", "8.jpg"),
("Vinland Saga Vol.11", "9781612626796", 2014, "English", "9.jpg"),
("So I’m a Spider So What? Vol.1", "9780316553377", 2015, "English", "10.jpg")
]

insert_many("""
INSERT INTO Book (book_name, isbn, publication_year, language, cover)
VALUES (?, ?, ?, ?, ?)
""", real_books)

print("Inserted 10 fixed books with covers 1–10.jpg")

# =========================
# AUTHORS (fake-ish + known)
# =========================
authors = [
("Jojo Moyes", 1969, "UK"),
("Aiden Thomas", 1994, "USA"),
("TurtleMe", 1990, "USA"),
("Brian Daley", 1947, "USA"),
("Kentaro Miura", 1966, "Japan"),
("J.K. Rowling", 1965, "UK"),
("James Clear", 1986, "USA"),
("Makoto Yukimura", 1976, "Japan"),
("Okina Baba", 1980, "Japan")
]

insert_many("""
INSERT INTO Authors (full_name, birth_year, nationality)
VALUES (?, ?, ?)
""", authors)

c.execute("SELECT author_id FROM Authors")
author_ids = [row[0] for row in c.fetchall()]

# =========================
# CATEGORIES
# =========================
categories = [
("Fantasy",),
("Manga",),
("Self Help",),
("Science Fiction",),
("Drama",),
("Romance",)
]

insert_many("INSERT INTO Categories (category_name) VALUES (?)", categories)

c.execute("SELECT category_id FROM Categories")
category_ids = [row[0] for row in c.fetchall()]

# =========================
# RELATIONS
# =========================
c.execute("SELECT book_id FROM Book")
book_ids = [b[0] for b in c.fetchall()]

book_author_links = []
book_category_links = []

for b in book_ids:
    book_author_links.append((b, random.choice(author_ids)))
    book_category_links.append((b, random.choice(category_ids)))

insert_many("""
INSERT INTO Book_Authors (book_id, author_id) VALUES (?, ?)
""", book_author_links)

insert_many("""
INSERT INTO Book_Category (book_id, category_id) VALUES (?, ?)
""", book_category_links)

print("Books linked to Authors + Categories")

# =========================
# COPIES
# =========================
copies = []
for b in book_ids:
    for _ in range(random.randint(1,4)):
        copies.append((b, random.choice(["Available", "Available", "Loaned"])))

insert_many("""
INSERT INTO Copy (book_id, status)
VALUES (?, ?)
""", copies)

print("Copies created")

# =========================
# ROOMS
# =========================
rooms = [(random.randint(5,20), random.randint(1,3)) for _ in range(10)]
insert_many("INSERT INTO Rooms (capacity, floor) VALUES (?, ?)", rooms)

print("Rooms created")

# =========================
# RESERVATIONS
# =========================
c.execute("SELECT student_id FROM Student")
student_ids = [s[0] for s in c.fetchall()]

c.execute("SELECT staff_id FROM Staff")
staff_ids = [s[0] for s in c.fetchall()]

slots = ["Morning","Noon","Evening"]
statuses = ["Pending","Approved","Rejected","Active","Finished"]

reservations = []
for _ in range(20):
    student = random.choice(student_ids)
    staff = random.choice(staff_ids)
    date = (datetime.now() + timedelta(days=random.randint(-2,5))).date()

    reservations.append((
        student,
        random.randint(1,10),
        staff,
        random.choice(statuses),
        random.choice(slots),
        date.isoformat(),
        datetime.now().isoformat(),
        None
    ))

insert_many("""
INSERT INTO Room_Reservation
(student_id, room_id, staff_id, status, slot, date, requested_at, approved_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", reservations)

print("Room reservations created")

# =========================
# LOANS
# =========================
c.execute("SELECT copy_id FROM Copy WHERE status='Loaned'")
loanable = [x[0] for x in c.fetchall()]

loans = []
for copy_id in loanable[:15]:
    loans.append((
        copy_id,
        random.choice(student_ids),
        random.choice(staff_ids),
        random.choice(["Pending","Active","Returned","Rejected"]),
        datetime.now().isoformat(),
        None,
        None
    ))

insert_many("""
INSERT INTO Book_Loan (copy_id, student_id, staff_id, status, created_at, approved_at, returned_at)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", loans)

print("Loans created")

print("\n🎉 DATABASE SEEDED SUCCESSFULLY 🎉")
conn.close()

