from fastapi import FastAPI
from routes.auth_routes import router as auth_router
import uvicorn
from services.database.db import init_db

app = FastAPI(title="Library Management API")

app.include_router(auth_router)

def create_connection():
    connection = init_db()
    return connection

if __name__ == "__main__":
    # Inialize
    connection = create_connection()

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )