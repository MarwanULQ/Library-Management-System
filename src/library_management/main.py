from fastapi import FastAPI
from .routes.auth_routes import router as auth_router
from .routes.db_routes import router as db_router
import uvicorn
from .services.database.db import init_db
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Library Management API")

app.include_router(auth_router)
app.include_router(db_router)


root = Path(__file__).resolve().parent
covers_dir = root / "ui" / "assets" / "covers"
covers_dir.mkdir(exist_ok=True)
app.mount("/covers", StaticFiles(directory=covers_dir), name="covers")


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
