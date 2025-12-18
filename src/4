import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent.parent.parent.parent
db_dir = root / "data"
db = db_dir / "library.db"
schema_path = root / "src" / "library_management" / "db" / "schema.sql"

def get_connection():
    return sqlite3.connect(db)

def init_db():
    # Makes the db directory 
    # exists_ok is True to make sure the function does not panic if directory already exists 
    db_dir.mkdir(exist_ok=True)

    # Checks if the db already exists
    db_exist = db.exists()

    # connect to the db and creates it first if needed
    connection = sqlite3.connect(db)

    # if the db did not exists before connecting -> excute the schema
    if not db_exist:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema_sql = f.read()
        connection.executescript(schema_sql)
        connection.commit()
    return connection
