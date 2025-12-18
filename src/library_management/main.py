from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from services.database import init_db
import uvicorn

app = FastAPI(title="Library Management API")

app.include_router(auth_router)

# Inialize
init_db()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )