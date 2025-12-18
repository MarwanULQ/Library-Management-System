import uuid
from datetime import datetime
from database import get_db
from password_utils import hash_password, verify_password

def signup(email: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT id FROM users WHERE email=?", (email,))
    if cur.fetchone():
        raise ValueError("Email already exists")

    user_id = str(uuid.uuid4())
    password_hash = hash_password(password)


    cur.execute("""
        INSERT INTO users (id, email, password_hash, is_verified, created_at)
        VALUES (?, ?, ?, 0, ?)
    """, (user_id, email, password_hash, datetime.utcnow()))

    db.commit()
    db.close()

    return user_id

def login(email: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute("""
        SELECT id, password_hash, is_verified
        FROM users WHERE email=?
    """, (email,))
    user = cur.fetchone()
    db.close()

    if not user:
        raise ValueError("Invalid credentials")

    user_id, password_hash, is_verified = user

    if not verify_password(password, password_hash):
        raise ValueError("Invalid credentials")
    
    return user_id