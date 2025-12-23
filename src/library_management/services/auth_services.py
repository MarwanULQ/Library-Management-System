import uuid
from datetime import datetime
from services.database.db import get_db
from services.password_utils import hash_password, verify_password

def signup(email: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT id FROM Users WHERE email=?", (email,))
    if cur.fetchone():
        raise ValueError("Email already exists")

    user_id = str(uuid.uuid4())
    password_hash = hash_password(password)


    cur.execute("""
        INSERT INTO Users (id, email, password_hash, created_at)
        VALUES (?, ?, ?, ?)
    """, (user_id, email, password_hash, datetime.utcnow()))

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
