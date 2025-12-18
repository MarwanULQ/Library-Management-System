# __init__.py

import sqlite3


# Initialize the database 
def init_db():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    # Create users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()