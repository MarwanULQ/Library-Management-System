import sqlite3

DB_NAME = "library.db"

def get_db():
    return sqlite3.connect(DB_NAME)