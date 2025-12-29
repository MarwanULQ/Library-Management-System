import uuid
from datetime import datetime
from .database.db import get_db
from .password_utils import hash_password, verify_password

def signup(email: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT id FROM Users WHERE email=?", (email,))
    if cur.fetchone():
        raise ValueError("Email already exists")

    password_hash = hash_password(password)

    cur.execute("""
        INSERT INTO Users (email, password_hash, created_at)
        VALUES (?, ?, ?)
    """, ( email, password_hash, datetime.utcnow().isoformat()))

    cur.execute("SELECT id FROM Users WHERE email=?", (email,))

    user_id = cur.fetchone()[0]

    db.commit()
    db.close()

    return user_id

def login(email: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute("""
        SELECT id, password_hash
        FROM Users WHERE email=?
    """, (email,))
    user = cur.fetchone()
    db.close()

    if not user:
        raise ValueError("Invalid credentials")

    user_id, password_hash = user

    if not verify_password(password, password_hash):
        raise ValueError("Invalid credentials")
    
    return user_id
