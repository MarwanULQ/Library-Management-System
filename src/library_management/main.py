from db.db import init_db

def create_app():
    connection = init_db()
    return connection
if __name__ == "__main__":
    create_app()
