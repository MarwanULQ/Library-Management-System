import sqlite3

DB_NAME = "library.db"

# Initialize the database 
def init_db():
    conn = sqlite3.connect(DB_NAME)
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

def get_db():
    return sqlite3.connect(DB_NAME)